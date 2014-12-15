# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qvibeplot.ui'
#
# Created: Wed Dec 17 12:51:38 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftVLayout = QtWidgets.QVBoxLayout()
        self.leftVLayout.setObjectName("leftVLayout")
        self.moleculeGB = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moleculeGB.sizePolicy().hasHeightForWidth())
        self.moleculeGB.setSizePolicy(sizePolicy)
        self.moleculeGB.setMinimumSize(QtCore.QSize(250, 0))
        self.moleculeGB.setObjectName("moleculeGB")
        self.formLayout_3 = QtWidgets.QFormLayout(self.moleculeGB)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.fontSizeLabel = QtWidgets.QLabel(self.moleculeGB)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fontSizeLabel)
        self.fontSizeComboBox = QtWidgets.QComboBox(self.moleculeGB)
        self.fontSizeComboBox.setObjectName("fontSizeComboBox")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(0, "6")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(1, "8")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(2, "10")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(3, "12")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(4, "14")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(5, "18")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(6, "20")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(7, "24")
        self.fontSizeComboBox.addItem("")
        self.fontSizeComboBox.setItemText(8, "32")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fontSizeComboBox)
        self.lineWidthLabel = QtWidgets.QLabel(self.moleculeGB)
        self.lineWidthLabel.setObjectName("lineWidthLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineWidthLabel)
        self.lineWidthComboBox = QtWidgets.QComboBox(self.moleculeGB)
        self.lineWidthComboBox.setObjectName("lineWidthComboBox")
        self.lineWidthComboBox.addItem("")
        self.lineWidthComboBox.addItem("")
        self.lineWidthComboBox.addItem("")
        self.lineWidthComboBox.addItem("")
        self.lineWidthComboBox.addItem("")
        self.lineWidthComboBox.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineWidthComboBox)
        self.colorLabelLabel = QtWidgets.QLabel(self.moleculeGB)
        self.colorLabelLabel.setObjectName("colorLabelLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.colorLabelLabel)
        self.colorLabelCheckBox = QtWidgets.QCheckBox(self.moleculeGB)
        self.colorLabelCheckBox.setEnabled(True)
        self.colorLabelCheckBox.setText("")
        self.colorLabelCheckBox.setObjectName("colorLabelCheckBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.colorLabelCheckBox)
        self.leftVLayout.addWidget(self.moleculeGB)
        self.vibrationGB = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vibrationGB.sizePolicy().hasHeightForWidth())
        self.vibrationGB.setSizePolicy(sizePolicy)
        self.vibrationGB.setMinimumSize(QtCore.QSize(250, 0))
        self.vibrationGB.setObjectName("vibrationGB")
        self.formLayout_2 = QtWidgets.QFormLayout(self.vibrationGB)
        self.formLayout_2.setObjectName("formLayout_2")
        self.bondlengthFilterLabel = QtWidgets.QLabel(self.vibrationGB)
        self.bondlengthFilterLabel.setObjectName("bondlengthFilterLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bondlengthFilterLabel)
        self.bondlengthFilter = QtWidgets.QSpinBox(self.vibrationGB)
        self.bondlengthFilter.setSuffix(" pm")
        self.bondlengthFilter.setMaximum(100)
        self.bondlengthFilter.setSingleStep(5)
        self.bondlengthFilter.setProperty("value", 0)
        self.bondlengthFilter.setObjectName("bondlengthFilter")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bondlengthFilter)
        self.angleFilterLabel = QtWidgets.QLabel(self.vibrationGB)
        self.angleFilterLabel.setObjectName("angleFilterLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.angleFilterLabel)
        self.angleFilter = QtWidgets.QSpinBox(self.vibrationGB)
        self.angleFilter.setMaximum(90)
        self.angleFilter.setSingleStep(5)
        self.angleFilter.setProperty("value", 0)
        self.angleFilter.setObjectName("angleFilter")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.angleFilter)
        self.torsionFilterLabel = QtWidgets.QLabel(self.vibrationGB)
        self.torsionFilterLabel.setObjectName("torsionFilterLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.torsionFilterLabel)
        self.torsionFilter = QtWidgets.QSpinBox(self.vibrationGB)
        self.torsionFilter.setMaximum(180)
        self.torsionFilter.setSingleStep(10)
        self.torsionFilter.setProperty("value", 0)
        self.torsionFilter.setObjectName("torsionFilter")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.torsionFilter)
        self.leftVLayout.addWidget(self.vibrationGB)
        self.spectrumGB = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrumGB.sizePolicy().hasHeightForWidth())
        self.spectrumGB.setSizePolicy(sizePolicy)
        self.spectrumGB.setMinimumSize(QtCore.QSize(250, 0))
        self.spectrumGB.setObjectName("spectrumGB")
        self.formLayout = QtWidgets.QFormLayout(self.spectrumGB)
        self.formLayout.setObjectName("formLayout")
        self.broadeningLabel = QtWidgets.QLabel(self.spectrumGB)
        self.broadeningLabel.setObjectName("broadeningLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.broadeningLabel)
        self.broadeningComboBox = QtWidgets.QComboBox(self.spectrumGB)
        self.broadeningComboBox.setObjectName("broadeningComboBox")
        self.broadeningComboBox.addItem("")
        self.broadeningComboBox.addItem("")
        self.broadeningComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.broadeningComboBox)
        self.fwhmLabel = QtWidgets.QLabel(self.spectrumGB)
        self.fwhmLabel.setObjectName("fwhmLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fwhmLabel)
        self.fwhmDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.spectrumGB)
        self.fwhmDoubleSpinBox.setDecimals(1)
        self.fwhmDoubleSpinBox.setMaximum(40.0)
        self.fwhmDoubleSpinBox.setProperty("value", 8.0)
        self.fwhmDoubleSpinBox.setObjectName("fwhmDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fwhmDoubleSpinBox)
        self.leftVLayout.addWidget(self.spectrumGB)
        self.spectrumTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrumTable.sizePolicy().hasHeightForWidth())
        self.spectrumTable.setSizePolicy(sizePolicy)
        self.spectrumTable.setMinimumSize(QtCore.QSize(250, 0))
        self.spectrumTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.spectrumTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.spectrumTable.setColumnCount(2)
        self.spectrumTable.setObjectName("spectrumTable")
        self.spectrumTable.setRowCount(0)
        self.spectrumTable.horizontalHeader().setVisible(True)
        self.spectrumTable.horizontalHeader().setStretchLastSection(True)
        self.leftVLayout.addWidget(self.spectrumTable)
        self.horizontalLayout_2.addLayout(self.leftVLayout)
        self.rightVLayout = QtWidgets.QVBoxLayout()
        self.rightVLayout.setObjectName("rightVLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.svgWidget = QSvgWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.svgWidget.sizePolicy().hasHeightForWidth())
        self.svgWidget.setSizePolicy(sizePolicy)
        self.svgWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.svgWidget.setObjectName("svgWidget")
        self.horizontalLayout.addWidget(self.svgWidget)
        self.moleculeCanvas = MplCanvas(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moleculeCanvas.sizePolicy().hasHeightForWidth())
        self.moleculeCanvas.setSizePolicy(sizePolicy)
        self.moleculeCanvas.setMinimumSize(QtCore.QSize(200, 0))
        self.moleculeCanvas.setObjectName("moleculeCanvas")
        self.horizontalLayout.addWidget(self.moleculeCanvas)
        self.rightVLayout.addLayout(self.horizontalLayout)
        self.spectrumCanvas = MplCanvas(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.spectrumCanvas.sizePolicy().hasHeightForWidth())
        self.spectrumCanvas.setSizePolicy(sizePolicy)
        self.spectrumCanvas.setMinimumSize(QtCore.QSize(0, 200))
        self.spectrumCanvas.setObjectName("spectrumCanvas")
        self.rightVLayout.addWidget(self.spectrumCanvas)
        self.horizontalLayout_2.addLayout(self.rightVLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 757, 19))
        self.menuBar.setObjectName("menuBar")
        self.fileMenu = QtWidgets.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.viewMenu = QtWidgets.QMenu(self.menuBar)
        self.viewMenu.setObjectName("viewMenu")
        self.helpMenu = QtWidgets.QMenu(self.menuBar)
        self.helpMenu.setObjectName("helpMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.saveImageAction = QtWidgets.QAction(MainWindow)
        self.saveImageAction.setObjectName("saveImageAction")
        self.saveImageAsAction = QtWidgets.QAction(MainWindow)
        self.saveImageAsAction.setObjectName("saveImageAsAction")
        self.aboutOrbiMolAction = QtWidgets.QAction(MainWindow)
        self.aboutOrbiMolAction.setObjectName("aboutOrbiMolAction")
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.setObjectName("quitAction")
        self.showIndexAction = QtWidgets.QAction(MainWindow)
        self.showIndexAction.setCheckable(True)
        self.showIndexAction.setObjectName("showIndexAction")
        self.showSkeletonAction = QtWidgets.QAction(MainWindow)
        self.showSkeletonAction.setObjectName("showSkeletonAction")
        self.aboutOpenBabelAction = QtWidgets.QAction(MainWindow)
        self.aboutOpenBabelAction.setObjectName("aboutOpenBabelAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.aboutMplAction = QtWidgets.QAction(MainWindow)
        self.aboutMplAction.setObjectName("aboutMplAction")
        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.viewMenu.menuAction())
        self.menuBar.addAction(self.helpMenu.menuAction())
        self.fontSizeLabel.setBuddy(self.fontSizeComboBox)
        self.lineWidthLabel.setBuddy(self.lineWidthComboBox)
        self.colorLabelLabel.setBuddy(self.colorLabelCheckBox)
        self.bondlengthFilterLabel.setBuddy(self.bondlengthFilter)
        self.angleFilterLabel.setBuddy(self.angleFilter)
        self.torsionFilterLabel.setBuddy(self.torsionFilter)
        self.broadeningLabel.setBuddy(self.broadeningComboBox)
        self.fwhmLabel.setBuddy(self.fwhmDoubleSpinBox)

        self.retranslateUi(MainWindow)
        self.fontSizeComboBox.setCurrentIndex(3)
        self.lineWidthComboBox.setCurrentIndex(3)
        self.broadeningComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QVibeplot"))
        self.moleculeGB.setTitle(_translate("MainWindow", "Molecule"))
        self.fontSizeLabel.setText(_translate("MainWindow", "Font Size"))
        self.lineWidthLabel.setText(_translate("MainWindow", "Linewidth"))
        self.lineWidthComboBox.setItemText(0, _translate("MainWindow", "0.0"))
        self.lineWidthComboBox.setItemText(1, _translate("MainWindow", "0.2"))
        self.lineWidthComboBox.setItemText(2, _translate("MainWindow", "0.5"))
        self.lineWidthComboBox.setItemText(3, _translate("MainWindow", "1.0"))
        self.lineWidthComboBox.setItemText(4, _translate("MainWindow", "2.0"))
        self.lineWidthComboBox.setItemText(5, _translate("MainWindow", "4.0"))
        self.colorLabelLabel.setText(_translate("MainWindow", "Black Labels"))
        self.vibrationGB.setTitle(_translate("MainWindow", "Vibration filter"))
        self.bondlengthFilterLabel.setText(_translate("MainWindow", "Bondlength"))
        self.angleFilterLabel.setText(_translate("MainWindow", "Angle"))
        self.angleFilter.setSuffix(_translate("MainWindow", "º"))
        self.torsionFilterLabel.setText(_translate("MainWindow", "Torsion"))
        self.torsionFilter.setSuffix(_translate("MainWindow", "º"))
        self.spectrumGB.setTitle(_translate("MainWindow", "Spectrum broadening"))
        self.broadeningLabel.setText(_translate("MainWindow", "Function"))
        self.broadeningComboBox.setItemText(0, _translate("MainWindow", "none"))
        self.broadeningComboBox.setItemText(1, _translate("MainWindow", "lorentzian"))
        self.broadeningComboBox.setItemText(2, _translate("MainWindow", "gaussian"))
        self.fwhmLabel.setText(_translate("MainWindow", "FWHM"))
        self.fileMenu.setTitle(_translate("MainWindow", "File"))
        self.viewMenu.setTitle(_translate("MainWindow", "View"))
        self.helpMenu.setTitle(_translate("MainWindow", "Help"))
        self.openAction.setText(_translate("MainWindow", "Open"))
        self.saveImageAction.setText(_translate("MainWindow", "Save image"))
        self.saveImageAsAction.setText(_translate("MainWindow", "Save image as..."))
        self.aboutOrbiMolAction.setText(_translate("MainWindow", "About OrbiMol..."))
        self.quitAction.setText(_translate("MainWindow", "Quit"))
        self.showIndexAction.setText(_translate("MainWindow", "Show index"))
        self.showSkeletonAction.setText(_translate("MainWindow", "Show skeleton"))
        self.aboutOpenBabelAction.setText(_translate("MainWindow", "About Open Babel"))
        self.aboutAction.setText(_translate("MainWindow", "About"))
        self.aboutMplAction.setText(_translate("MainWindow", "About Matplotlib"))

from mpl_canvas import MplCanvas
from svg_widget import QSvgWidget
