#!/usr/bin/env python
# Copyright (c) 2011, Mathias Laurin
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""Qt graphical user interface (GUI) to vibeplot."""

import sys
import os.path
from glob import glob
from functools import partial

import sip
for qtype in "QString QTextStream QVariant".split():
    sip.setapi(qtype, 2)

# Import Qt and matplotlib modules
import matplotlib as mpl
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtSvg import QSvgWidget
    mpl.rcParams["backend"] = "Qt4Agg"
    from matplotlib.backends.backend_qt4agg import (NavigationToolbar2QT
                                                    as NavigationToolbar)
except ImportError:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import QPalette, QColor, QKeySequence
    from PyQt5.QtCore import *
    from PyQt5.QtSvg import QSvgWidget
    mpl.rcParams["backend"] = "Qt5Agg"
    from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT
                                                    as NavigationToolbar)

import openbabel as ob

from qvibeplot_ui import Ui_MainWindow
import vibeplot.plotter as plotter


class QVibeplot(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(QVibeplot, self).__init__()
        self.setupUi(self)

        self.toolbar = NavigationToolbar(self.moleculeCanvas, self, False)
        self.rightVLayout.insertWidget(
            self.rightVLayout.indexOf(self.moleculeCanvas) + 1, self.toolbar)

        self.svgWidget = QSvgWidget()
        palette = QPalette(self.svgWidget.palette())
        palette.setColor(palette.Window, QColor("white"))
        self.svgWidget.setPalette(palette)

        self.moleculePlotter = plotter.MoleculePlotter(
            self.moleculeCanvas.figure.add_subplot(111))
        self.spectrumPlotter = plotter.SpectrumPlotter(
            self.spectrumCanvas.figure.add_subplot(111))

        self._settings = QSettings("Mathias Laurin", "QVibePlot")
        for setting in "imagePath dataPath".split():
            if not self._settings.contains(setting):
                self._settings.setValue(setting, QDir.homePath())
        self._imageFile = None

        # Connect widgets
        self.fontSizeComboBox.currentIndexChanged[str].connect(
            self.moleculePlotter.set_fontsize)
        self.lineWidthComboBox.currentIndexChanged[str].connect(
            self.moleculePlotter.set_linewidth)
        self.colorLabelCheckBox.stateChanged.connect(
            lambda checked:
            self.moleculePlotter.set_black_labels(checked==Qt.Checked))
        self.bondlengthFilter.valueChanged.connect(self._drawVibration)
        self.angleFilter.valueChanged.connect(self._drawVibration)
        self.torsionFilter.valueChanged.connect(self._drawVibration)
        self.broadeningComboBox.currentIndexChanged[str].connect(
            self.spectrumPlotter.set_broadening_function)
        self.fwhmDoubleSpinBox.valueChanged.connect(
            self.spectrumPlotter.set_fwhm)
        self.frequencyList.currentTextChanged.connect(
            self.spectrumPlotter.set_vibration)
        self.frequencyList.currentRowChanged.connect(self._drawVibration)
        # Create actions
        self.spectrumCanvas.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.spectrumCanvas.addAction(
            QAction(u"save spectrum", self.spectrumCanvas,
                    triggered=self._saveSpectrum))
        # File menu
        self.fileMenu.addActions((
            QAction(u"Open", self.fileMenu,
                    shortcut=QKeySequence.Open,
                    triggered=self._loadFile),
            QAction(u"Save image", self.fileMenu,
                    shortcut=QKeySequence.Save,
                    triggered=self._saveImage),
            QAction(u"Save image as...", self.fileMenu,
                    shortcut=QKeySequence.SaveAs,
                    triggered=self._saveImageAs),
            QAction(u"Quit", self.fileMenu,
                    shortcut=QKeySequence.Quit,
                    triggered=self.close),
        ))
        # File > OrbiMol menu
        self.orbiMolDbMenu = QMenu(u"OrbiMol DB molecules")
        self.orbiMolDbMenu.addActions([
            QAction(os.path.splitext(os.path.basename(filename))[0],  # text
                    self.orbiMolDbMenu,
                    triggered=partial(self._loadFile, filename, "g03"))
            for filename in glob("data/orbimol/*.freq")])
        self.orbiMolDbMenu.addSeparator()
        self.orbiMolDbMenu.addAction(
            QAction(u"About OrbiMol", self.orbiMolDbMenu,
                    triggered=partial(QMessageBox.about, self, u"About OrbiMol",
                                      " ".join((
            u"""
            <p>OrbiMol is a free molecular orbital database by Patrick
            Chaquin and Franck Fuster. Laboratoire de Chimie
            Th&eacute;orique, UPMC Univ Paris 06, UMR CNRS 7616, Paris.</p>

            <p>For more information, see
            <a href="http://www.lct.jussieu.fr/pagesperso/orbimol/">OrbiMol
            </a> or Chaquin, P.; Fuster, F. Enseigner la chimie organique
            avec les orbitales Pr&eacute;sentation d'une base de
            donn&eacute;es d'orbitales mol&eacute;culaires. <i>L'Act.
            Chim.</i> <b>2012</b>, <i>369</i>, 37-44.

            """).splitlines()))))
        self.fileMenu.addSeparator()
        self.fileMenu.addMenu(self.orbiMolDbMenu)
        # View menu
        self.viewMenu.addActions((
            QAction(u"Atom index", self.viewMenu, checkable=True,
                    triggered=self.moleculePlotter.show_atom_index),
            QAction(u"Show skeleton", self.viewMenu,
                    triggered=self.svgWidget.show),
        ))
        # Help menu
        self.helpMenu.addActions((
            QAction(u"About", self.helpMenu, triggered=partial(
                QMessageBox.about,
                self, "About QVibePlot", " ".join((
            u"""
            QVibePlot visualizes vibrational analysis performed by
            density functional theory calculations (DFT) in terms of
            changes of internal coordinates.
            <p>QVibePlot is written in Python and depends on matplotlib
            for the graphics and numpy for the maths. The GUI is
            written using PyQt4.</p>
            <p>Copyright (c) 2011-2013
            <a href="mailto:Mathias.Laurin+vibeplot@gmail.com"> Mathias
            Laurin</a></p>
            <p>QVibePlot 0.14 is available under the modified BSD
            License.</p>
            <p>Support the program by citing: Laurin, M.  QVibeplot: A
            Program To Visualize Molecular Vibrations in Two
            Dimensions. <i>J. Chem. Educ.</i> <b>2013</b>
            <a href="http://dx.doi.org/10.1021/ed300554z">DOI:
            10.1021/ed300554z</a>.</p>

            """).splitlines()))),
            QAction(u"About Qt", self.helpMenu,
                    triggered=partial(QMessageBox.aboutQt, self)),
            QAction(u"About Open Babal", self.helpMenu,
                    triggered=partial(QMessageBox.about, self,
                                      u"About Open Babel", " ".join((
            u"""
            <P>This program uses Open Babel.</P>
            <P>Open Babel is a chemical toolbox designed to speak the
            many languages of chemical data. It's an open,
            collaborative project allowing anyone to search, convert,
            analyze, or store data from molecular modeling, chemistry,
            solid-state materials, biochemistry, or related areas.</P>
            <P>Open Babel is released under the GNU GPL.</P>
            <P>See <a href="http://openbabel.org">openbabel.org</a> for
            more information.</P>

            """).splitlines()))),
            QAction(u"About Matplotlib", self.helpMenu,
                    triggered=partial(QMessageBox.about, self,
                                      u"About Matplotlib", " ".join((
            u"""
            <P>This program uses Matplotlib {0}.</P>
            <P>Matplotlib is a python 2D plotting library which
            produces publication quality figures in a variety of
            hardcopy formats and interactive environments across
            platforms.</P>
            <P>Matplotlib is released under the
            <a href="http://matplotlib.org/users/license.html">
            Matplotlib License</a>.</P>
            <P>See <a href="http://matplotlib.org">matplotlib.org</a>
            for more information.</P>

            """.format(mpl.__version__)).splitlines())))
        ))

    def _drawVibration(self):
        self.moleculePlotter.draw_vibration(
            self.frequencyList.currentRow(),
            self.bondlengthFilter.value(),
            self.angleFilter.value(),
            self.torsionFilter.value())

    def _loadFile(self, filename=None, inFormat=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(
                self,
                u"Open file",
                self._settings.value("dataPath"),
                ";;".join((
                    " ".join(("Common formats (",
                              "*.moldem *.mold *.molf",
                              "*.gal *.g92 *.g94 *.g98 *.g03 *.g09",
                              "*.acesout *.gukout *.nwo",
                              "CONTCAR POSCAR *.vasp", ")")),
                    "molden (*.molden *.mold *.molf)",
                    "Gaussian (*.gal *.g92 *.g94 *.g98 *.g03 *.g09)",
                    "ACES output (*.acesout)",
                    "GAMESS-UK (*.gukout)",
                    "NWChem output (*.nwo)",
                    "VASP (CONTCAR POSCAR *.vasp)",
                    "all files (*)")))
        try:
            filename, __ = filename  # PyQt5
        except ValueError:
            pass  # PyQt4
        if filename:
            self._settings.setValue("dataPath", os.path.dirname(filename))
        else:
            return

        if inFormat is None:
            inFormat = str(os.path.splitext(filename)[1][1:])
        if not inFormat and os.path.basename(filename).lower() in (
                "poscar", "contcar"):
            inFormat = "vasp"

        # load data
        mol = ob.OBMol()
        obconv = ob.OBConversion()
        obconv.SetInFormat(inFormat)
        obconv.ReadFile(mol, str(filename))
        if not mol.NumAtoms():
            self.statusBar().showMessage(
                "".join((
                    "Extension or file format '%s' unknown, ",
                    "see http://openbabel.org for the list of ",
                    "supported files.")) % inFormat)
        vibData = (ob.toVibrationData(mol.GetData(ob.VibrationData))
                   if mol.HasData(ob.VibrationData) else
                   ob.OBVibrationData())
        self.moleculePlotter.set_vibration_data(vibData)
        self.moleculePlotter.set_molecule(mol)
        self.moleculePlotter.draw_molecule(
            lw=str(self.lineWidthComboBox.currentText()),
            fontsize=str(self.fontSizeComboBox.currentText())
        )
        self.spectrumPlotter.set_vibration_data(vibData)
        self.spectrumPlotter.draw_spectrum()

        # reset
        self._imageFile = None

        # populate frequencyList
        self.frequencyList.clear()
        for freq in vibData.GetFrequencies():
            item = QListWidgetItem()
            item.setData(Qt.DisplayRole, freq)
            self.frequencyList.addItem(item)

        # window title
        obconv.SetOutFormat("smi")
        self.setWindowTitle(obconv.WriteString(mol))

        # SVG representation
        obconv.SetOutFormat("svg")
        obconv.AddOption("C", obconv.OUTOPTIONS)  # implicit carbons
        obconv.AddOption("d", obconv.OUTOPTIONS)  # no molecule name
        obconv.AddOption("d", obconv.GENOPTIONS)  # implicit hydrogens
        self.svgWidget.load(QByteArray(obconv.WriteString(mol)))

    def _saveImage(self):
        if not self._imageFile:
            self._saveImageAs()
        self.moleculePlotter.axes.figure.savefig(self._imageFile, dpi=300)

    def _saveImageAs(self):
        self._imageFile = QFileDialog.getSaveFileName(
            self,
            u"Save image",
            self._settings.value("imagePath"),
            ";;".join(("pdf files (*.pdf)",
                       "raster images (*.png *.jpeg *.tiff)",
                       "vector images (*.pdf *.eps *.ps)",
                       "all files (*)",)))
        if not self._imageFile:
            return
        if "." not in self._imageFile:
            self._imageFile += ".pdf"
        self._settings.setValue("imagePath", os.path.dirname(self._imageFile))
        self._saveImage()

    def _saveSpectrum(self):
        imageFile = QFileInfo(self._settings.value("imageFile"))
        filename = QFileDialog.getSaveFileName(
            self,
            u"Save spectrum values",
            imageFile.path() \
                    if imageFile.isFile() else imageFile.filePath(),
            "plain text (*.txt)")
        if not filename: return
        if "." not in filename:
            filename += ".txt"
        self.spectrumPlotter.save_spectrum(filename)

    def setWindowTitle(self, text=""):
        super(QVibeplot, self).setWindowTitle(
            'QVibeplot' if not text else
            '%s - QVibeplot' % os.path.basename(text))


def main():
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)
    window = QVibeplot()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
