# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Toolbox.ui'

# Import stuff
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import os
import cv2
from datetime import datetime
import math
import xml.etree.ElementTree as ET
from xml.dom import minidom
from PIL import Image, ImageFilter, ImageDraw, ImageChops
import random
import numpy as np
import subprocess, sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 951)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("HTX logo square.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1001, 951))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(160, 10, 741, 121))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_47 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout_9.addWidget(self.label_47, 0, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.gridLayout_9.addWidget(self.label_48, 1, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout_9.addWidget(self.label_49, 2, 0, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.gridLayout_9.addWidget(self.label_50, 3, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.tab)
        self.label_51.setGeometry(QtCore.QRect(30, 10, 101, 121))
        self.label_51.setObjectName("label_51")
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_5.setGeometry(QtCore.QRect(30, 150, 871, 151))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_56 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.gridLayout_10.addWidget(self.label_56, 3, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.gridLayout_10.addWidget(self.label_54, 2, 0, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.gridLayout_10.addWidget(self.label_52, 0, 0, 1, 2)
        self.overlayObjectInputBtn = QtWidgets.QToolButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.overlayObjectInputBtn.setFont(font)
        self.overlayObjectInputBtn.setObjectName("overlayObjectInputBtn")
        self.gridLayout_10.addWidget(self.overlayObjectInputBtn, 1, 2, 1, 1)
        self.overlayOutput = QtWidgets.QLineEdit(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.overlayOutput.setFont(font)
        self.overlayOutput.setReadOnly(True)
        self.overlayOutput.setObjectName("overlayOutput")
        self.gridLayout_10.addWidget(self.overlayOutput, 3, 1, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.gridLayout_10.addWidget(self.label_53, 1, 0, 1, 1)
        self.overlayOutputBtn = QtWidgets.QToolButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.overlayOutputBtn.setFont(font)
        self.overlayOutputBtn.setObjectName("overlayOutputBtn")
        self.gridLayout_10.addWidget(self.overlayOutputBtn, 3, 2, 1, 1)
        self.overlayBGInput = QtWidgets.QLineEdit(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.overlayBGInput.setFont(font)
        self.overlayBGInput.setReadOnly(True)
        self.overlayBGInput.setObjectName("overlayBGInput")
        self.gridLayout_10.addWidget(self.overlayBGInput, 2, 1, 1, 1)
        self.overlayObjectInput = QtWidgets.QLineEdit(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.overlayObjectInput.setFont(font)
        self.overlayObjectInput.setReadOnly(True)
        self.overlayObjectInput.setObjectName("overlayObjectInput")
        self.gridLayout_10.addWidget(self.overlayObjectInput, 1, 1, 1, 1)
        self.overlayBGInputBtn = QtWidgets.QToolButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.overlayBGInputBtn.setFont(font)
        self.overlayBGInputBtn.setObjectName("overlayBGInputBtn")
        self.gridLayout_10.addWidget(self.overlayBGInputBtn, 2, 2, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.tab)
        self.label_62.setGeometry(QtCore.QRect(30, 500, 479, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_62.setFont(font)
        self.label_62.setText("")
        self.label_62.setObjectName("label_62")
        self.OverlayStatusReportBox = QtWidgets.QPlainTextEdit(self.tab)
        self.OverlayStatusReportBox.setGeometry(QtCore.QRect(190, 780, 631, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.OverlayStatusReportBox.setFont(font)
        self.OverlayStatusReportBox.setReadOnly(True)
        self.OverlayStatusReportBox.setPlainText("")
        self.OverlayStatusReportBox.setOverwriteMode(True)
        self.OverlayStatusReportBox.setObjectName("OverlayStatusReportBox")
        self.OverlayRunProgBtn = QtWidgets.QPushButton(self.tab)
        self.OverlayRunProgBtn.setGeometry(QtCore.QRect(310, 720, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.OverlayRunProgBtn.setFont(font)
        self.OverlayRunProgBtn.setObjectName("OverlayRunProgBtn")
        self.label_60 = QtWidgets.QLabel(self.tab)
        self.label_60.setGeometry(QtCore.QRect(621, 351, 189, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_60.setFont(font)
        self.label_60.setText("")
        self.label_60.setObjectName("label_60")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 550, 461, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_64 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.gridLayout_22.addWidget(self.label_64, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.overlayObjMax = QtWidgets.QSpinBox(self.layoutWidget)
        self.overlayObjMax.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayObjMax.setFont(font)
        self.overlayObjMax.setMinimum(1)
        self.overlayObjMax.setMaximum(10)
        self.overlayObjMax.setProperty("value", 5)
        self.overlayObjMax.setObjectName("overlayObjMax")
        self.gridLayout_13.addWidget(self.overlayObjMax, 1, 2, 1, 1)
        self.overlayRotationMin = QtWidgets.QSpinBox(self.layoutWidget)
        self.overlayRotationMin.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayRotationMin.setFont(font)
        self.overlayRotationMin.setMinimum(0)
        self.overlayRotationMin.setMaximum(360)
        self.overlayRotationMin.setSingleStep(10)
        self.overlayRotationMin.setProperty("value", 0)
        self.overlayRotationMin.setObjectName("overlayRotationMin")
        self.gridLayout_13.addWidget(self.overlayRotationMin, 2, 1, 1, 1)
        self.overlayRotationMax = QtWidgets.QSpinBox(self.layoutWidget)
        self.overlayRotationMax.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayRotationMax.setFont(font)
        self.overlayRotationMax.setMinimum(0)
        self.overlayRotationMax.setMaximum(360)
        self.overlayRotationMax.setSingleStep(10)
        self.overlayRotationMax.setProperty("value", 360)
        self.overlayRotationMax.setObjectName("overlayRotationMax")
        self.gridLayout_13.addWidget(self.overlayRotationMax, 2, 2, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.gridLayout_13.addWidget(self.label_68, 2, 0, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.gridLayout_13.addWidget(self.label_66, 0, 2, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.gridLayout_13.addWidget(self.label_67, 1, 0, 1, 1)
        self.overlayObjMin = QtWidgets.QSpinBox(self.layoutWidget)
        self.overlayObjMin.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayObjMin.setFont(font)
        self.overlayObjMin.setMinimum(1)
        self.overlayObjMin.setMaximum(10)
        self.overlayObjMin.setProperty("value", 1)
        self.overlayObjMin.setObjectName("overlayObjMin")
        self.gridLayout_13.addWidget(self.overlayObjMin, 1, 1, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.gridLayout_13.addWidget(self.label_65, 0, 1, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_13, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 330, 903, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_55 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.gridLayout_21.addWidget(self.label_55, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_58 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_58.setMinimumSize(QtCore.QSize(650, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.gridLayout_11.addWidget(self.label_58, 0, 0, 1, 1)
        self.overlayNumObjSlider = QtWidgets.QSlider(self.layoutWidget1)
        self.overlayNumObjSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.overlayNumObjSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.overlayNumObjSlider.setMinimum(1)
        self.overlayNumObjSlider.setMaximum(300)
        self.overlayNumObjSlider.setSingleStep(50)
        self.overlayNumObjSlider.setPageStep(50)
        self.overlayNumObjSlider.setProperty("value", 100)
        self.overlayNumObjSlider.setSliderPosition(100)
        self.overlayNumObjSlider.setOrientation(QtCore.Qt.Horizontal)
        self.overlayNumObjSlider.setInvertedAppearance(False)
        self.overlayNumObjSlider.setInvertedControls(False)
        self.overlayNumObjSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.overlayNumObjSlider.setObjectName("overlayNumObjSlider")
        self.gridLayout_11.addWidget(self.overlayNumObjSlider, 0, 1, 2, 1)
        self.overlayNumObjBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.overlayNumObjBox.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayNumObjBox.setFont(font)
        self.overlayNumObjBox.setMinimum(1)
        self.overlayNumObjBox.setMaximum(300)
        self.overlayNumObjBox.setSingleStep(50)
        self.overlayNumObjBox.setProperty("value", 100)
        self.overlayNumObjBox.setProperty("currNumThreat", 0)
        self.overlayNumObjBox.setObjectName("overlayNumObjBox")
        self.gridLayout_11.addWidget(self.overlayNumObjBox, 0, 2, 2, 1)
        self.label_59 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_59.setMinimumSize(QtCore.QSize(650, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.gridLayout_11.addWidget(self.label_59, 1, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_57 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout_12.addWidget(self.label_57, 0, 0, 1, 1)
        self.overlayClass = QtWidgets.QLineEdit(self.layoutWidget1)
        self.overlayClass.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayClass.setFont(font)
        self.overlayClass.setText("")
        self.overlayClass.setObjectName("overlayClass")
        self.gridLayout_12.addWidget(self.overlayClass, 0, 1, 2, 1)
        self.label_61 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_61.setMinimumSize(QtCore.QSize(600, 0))
        self.label_61.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.gridLayout_12.addWidget(self.label_61, 1, 0, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_63.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.gridLayout_12.addWidget(self.label_63, 2, 0, 1, 1)
        self.OverlayOpenFolderCheckbox = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OverlayOpenFolderCheckbox.setFont(font)
        self.OverlayOpenFolderCheckbox.setIconSize(QtCore.QSize(16, 16))
        self.OverlayOpenFolderCheckbox.setChecked(True)
        self.OverlayOpenFolderCheckbox.setObjectName("OverlayOpenFolderCheckbox")
        self.gridLayout_12.addWidget(self.OverlayOpenFolderCheckbox, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(580, 590, 351, 101))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_92 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        self.gridLayout_5.addWidget(self.label_92, 0, 0, 1, 1)
        self.overlayBgThreshold = QtWidgets.QSpinBox(self.widget)
        self.overlayBgThreshold.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayBgThreshold.setFont(font)
        self.overlayBgThreshold.setMinimum(1)
        self.overlayBgThreshold.setMaximum(255)
        self.overlayBgThreshold.setProperty("value", 250)
        self.overlayBgThreshold.setObjectName("overlayBgThreshold")
        self.gridLayout_5.addWidget(self.overlayBgThreshold, 0, 1, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.gridLayout_5.addWidget(self.label_69, 1, 0, 1, 1)
        self.overlayMagRatio = QtWidgets.QDoubleSpinBox(self.widget)
        self.overlayMagRatio.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayMagRatio.setFont(font)
        self.overlayMagRatio.setMaximum(2.0)
        self.overlayMagRatio.setSingleStep(0.25)
        self.overlayMagRatio.setProperty("value", 1.5)
        self.overlayMagRatio.setObjectName("overlayMagRatio")
        self.gridLayout_5.addWidget(self.overlayMagRatio, 1, 1, 1, 1)
        self.overlayWhitespaceOnlyCheck = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.overlayWhitespaceOnlyCheck.setFont(font)
        self.overlayWhitespaceOnlyCheck.setIconSize(QtCore.QSize(16, 16))
        self.overlayWhitespaceOnlyCheck.setChecked(True)
        self.overlayWhitespaceOnlyCheck.setObjectName("overlayWhitespaceOnlyCheck")
        self.gridLayout_5.addWidget(self.overlayWhitespaceOnlyCheck, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(160, 10, 741, 121))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 3, 0, 1, 1)
        self.AutoCropCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.AutoCropCheckbox.setGeometry(QtCore.QRect(290, 350, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AutoCropCheckbox.setFont(font)
        self.AutoCropCheckbox.setIconSize(QtCore.QSize(16, 16))
        self.AutoCropCheckbox.setChecked(True)
        self.AutoCropCheckbox.setObjectName("AutoCropCheckbox")
        self.AutoCropStatus = QtWidgets.QPlainTextEdit(self.tab_2)
        self.AutoCropStatus.setGeometry(QtCore.QRect(140, 470, 701, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AutoCropStatus.setFont(font)
        self.AutoCropStatus.setReadOnly(True)
        self.AutoCropStatus.setPlainText("")
        self.AutoCropStatus.setOverwriteMode(True)
        self.AutoCropStatus.setObjectName("AutoCropStatus")
        self.AutoCropRunBtn = QtWidgets.QPushButton(self.tab_2)
        self.AutoCropRunBtn.setGeometry(QtCore.QRect(290, 400, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.AutoCropRunBtn.setFont(font)
        self.AutoCropRunBtn.setObjectName("AutoCropRunBtn")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 170, 861, 151))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_29.addWidget(self.label_21, 0, 0, 1, 2)
        self.AutoCropInput = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AutoCropInput.setFont(font)
        self.AutoCropInput.setReadOnly(True)
        self.AutoCropInput.setObjectName("AutoCropInput")
        self.gridLayout_29.addWidget(self.AutoCropInput, 0, 2, 1, 1)
        self.AutoCropInputBtn = QtWidgets.QToolButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AutoCropInputBtn.setFont(font)
        self.AutoCropInputBtn.setObjectName("AutoCropInputBtn")
        self.gridLayout_29.addWidget(self.AutoCropInputBtn, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_29.addWidget(self.label_25, 1, 0, 1, 2)
        self.AutoCropXMLInput = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AutoCropXMLInput.setFont(font)
        self.AutoCropXMLInput.setReadOnly(True)
        self.AutoCropXMLInput.setObjectName("AutoCropXMLInput")
        self.gridLayout_29.addWidget(self.AutoCropXMLInput, 1, 2, 1, 1)
        self.AutoCropXMLInputBtn = QtWidgets.QToolButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AutoCropXMLInputBtn.setFont(font)
        self.AutoCropXMLInputBtn.setObjectName("AutoCropXMLInputBtn")
        self.gridLayout_29.addWidget(self.AutoCropXMLInputBtn, 1, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_29.addWidget(self.label_28, 2, 0, 1, 4)
        self.AutoCropOutputBtn = QtWidgets.QToolButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AutoCropOutputBtn.setFont(font)
        self.AutoCropOutputBtn.setObjectName("AutoCropOutputBtn")
        self.gridLayout_29.addWidget(self.AutoCropOutputBtn, 3, 3, 1, 1)
        self.AutoCropOutput = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AutoCropOutput.setFont(font)
        self.AutoCropOutput.setReadOnly(True)
        self.AutoCropOutput.setObjectName("AutoCropOutput")
        self.gridLayout_29.addWidget(self.AutoCropOutput, 3, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_29.addWidget(self.label_27, 3, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(30, 10, 101, 121))
        self.label_36.setObjectName("label_36")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 30, 741, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_30.addWidget(self.label_31, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_30.addWidget(self.label_3, 0, 0, 1, 1)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(40, 150, 861, 131))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.VideoExtInputBtn = QtWidgets.QToolButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VideoExtInputBtn.setFont(font)
        self.VideoExtInputBtn.setObjectName("VideoExtInputBtn")
        self.gridLayout_31.addWidget(self.VideoExtInputBtn, 0, 3, 1, 1)
        self.VideoExtInput = QtWidgets.QLineEdit(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VideoExtInput.setFont(font)
        self.VideoExtInput.setReadOnly(True)
        self.VideoExtInput.setObjectName("VideoExtInput")
        self.gridLayout_31.addWidget(self.VideoExtInput, 0, 2, 1, 1)
        self.VideoExtOutputBtn = QtWidgets.QToolButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VideoExtOutputBtn.setFont(font)
        self.VideoExtOutputBtn.setObjectName("VideoExtOutputBtn")
        self.gridLayout_31.addWidget(self.VideoExtOutputBtn, 1, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_31.addWidget(self.label_29, 0, 0, 1, 2)
        self.VideoExtOutput = QtWidgets.QLineEdit(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VideoExtOutput.setFont(font)
        self.VideoExtOutput.setReadOnly(True)
        self.VideoExtOutput.setObjectName("VideoExtOutput")
        self.gridLayout_31.addWidget(self.VideoExtOutput, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_31.addWidget(self.label_34, 1, 0, 1, 2)
        self.VideoExtRunBtn = QtWidgets.QPushButton(self.tab_3)
        self.VideoExtRunBtn.setGeometry(QtCore.QRect(300, 510, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.VideoExtRunBtn.setFont(font)
        self.VideoExtRunBtn.setObjectName("VideoExtRunBtn")
        self.VideoExtStatus = QtWidgets.QPlainTextEdit(self.tab_3)
        self.VideoExtStatus.setGeometry(QtCore.QRect(150, 580, 701, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VideoExtStatus.setFont(font)
        self.VideoExtStatus.setReadOnly(True)
        self.VideoExtStatus.setPlainText("")
        self.VideoExtStatus.setOverwriteMode(True)
        self.VideoExtStatus.setObjectName("VideoExtStatus")
        self.VideoExtCheckbox = QtWidgets.QCheckBox(self.tab_3)
        self.VideoExtCheckbox.setGeometry(QtCore.QRect(300, 460, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VideoExtCheckbox.setFont(font)
        self.VideoExtCheckbox.setIconSize(QtCore.QSize(16, 16))
        self.VideoExtCheckbox.setChecked(True)
        self.VideoExtCheckbox.setObjectName("VideoExtCheckbox")
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setGeometry(QtCore.QRect(30, 10, 101, 121))
        self.label_37.setObjectName("label_37")
        self.widget1 = QtWidgets.QWidget(self.tab_3)
        self.widget1.setGeometry(QtCore.QRect(170, 310, 631, 111))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_35 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 0, 0, 1, 1)
        self.VideoExtSlider = QtWidgets.QSlider(self.widget1)
        self.VideoExtSlider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.VideoExtSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VideoExtSlider.setMinimum(1)
        self.VideoExtSlider.setMaximum(100)
        self.VideoExtSlider.setSingleStep(10)
        self.VideoExtSlider.setProperty("value", 1)
        self.VideoExtSlider.setSliderPosition(1)
        self.VideoExtSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VideoExtSlider.setInvertedAppearance(False)
        self.VideoExtSlider.setInvertedControls(False)
        self.VideoExtSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.VideoExtSlider.setObjectName("VideoExtSlider")
        self.gridLayout.addWidget(self.VideoExtSlider, 1, 0, 1, 1)
        self.VideoExtSliderBox = QtWidgets.QSpinBox(self.widget1)
        self.VideoExtSliderBox.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VideoExtSliderBox.setFont(font)
        self.VideoExtSliderBox.setMinimum(1)
        self.VideoExtSliderBox.setMaximum(100)
        self.VideoExtSliderBox.setSingleStep(10)
        self.VideoExtSliderBox.setProperty("value", 1)
        self.VideoExtSliderBox.setProperty("currNumThreat", 0)
        self.VideoExtSliderBox.setObjectName("VideoExtSliderBox")
        self.gridLayout.addWidget(self.VideoExtSliderBox, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget_8 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_8.setGeometry(QtCore.QRect(150, 10, 741, 121))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.layoutWidget_8)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_73 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout_16.addWidget(self.label_73, 0, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.gridLayout_16.addWidget(self.label_74, 1, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.gridLayout_16.addWidget(self.label_75, 2, 0, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.gridLayout_16.addWidget(self.label_76, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 121))
        self.label.setObjectName("label")
        self.statusReportBox = QtWidgets.QPlainTextEdit(self.tab_4)
        self.statusReportBox.setGeometry(QtCore.QRect(170, 790, 631, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusReportBox.setFont(font)
        self.statusReportBox.setReadOnly(True)
        self.statusReportBox.setPlainText("")
        self.statusReportBox.setOverwriteMode(True)
        self.statusReportBox.setObjectName("statusReportBox")
        self.RunProgBtn = QtWidgets.QPushButton(self.tab_4)
        self.RunProgBtn.setGeometry(QtCore.QRect(310, 730, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.RunProgBtn.setFont(font)
        self.RunProgBtn.setObjectName("RunProgBtn")
        self.layoutWidget_11 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_11.setGeometry(QtCore.QRect(30, 150, 861, 181))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.layoutWidget_11)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_86 = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.gridLayout_19.addWidget(self.label_86, 0, 0, 1, 2)
        self.label_87 = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.gridLayout_19.addWidget(self.label_87, 1, 0, 1, 1)
        self.selectThreatFilesInput = QtWidgets.QLineEdit(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.selectThreatFilesInput.setFont(font)
        self.selectThreatFilesInput.setReadOnly(True)
        self.selectThreatFilesInput.setObjectName("selectThreatFilesInput")
        self.gridLayout_19.addWidget(self.selectThreatFilesInput, 1, 1, 1, 1)
        self.selectThreatFilesBtn = QtWidgets.QToolButton(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectThreatFilesBtn.setFont(font)
        self.selectThreatFilesBtn.setObjectName("selectThreatFilesBtn")
        self.gridLayout_19.addWidget(self.selectThreatFilesBtn, 1, 2, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.gridLayout_19.addWidget(self.label_88, 2, 0, 1, 1)
        self.selectContainerFilesInput = QtWidgets.QLineEdit(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.selectContainerFilesInput.setFont(font)
        self.selectContainerFilesInput.setReadOnly(True)
        self.selectContainerFilesInput.setObjectName("selectContainerFilesInput")
        self.gridLayout_19.addWidget(self.selectContainerFilesInput, 2, 1, 1, 1)
        self.selectContainerFilesBtn = QtWidgets.QToolButton(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectContainerFilesBtn.setFont(font)
        self.selectContainerFilesBtn.setObjectName("selectContainerFilesBtn")
        self.gridLayout_19.addWidget(self.selectContainerFilesBtn, 2, 2, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.gridLayout_19.addWidget(self.label_89, 3, 0, 1, 1)
        self.selectContainerXMLInput = QtWidgets.QLineEdit(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.selectContainerXMLInput.setFont(font)
        self.selectContainerXMLInput.setReadOnly(True)
        self.selectContainerXMLInput.setObjectName("selectContainerXMLInput")
        self.gridLayout_19.addWidget(self.selectContainerXMLInput, 3, 1, 1, 1)
        self.selectContainerXMLBtn = QtWidgets.QToolButton(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectContainerXMLBtn.setFont(font)
        self.selectContainerXMLBtn.setObjectName("selectContainerXMLBtn")
        self.gridLayout_19.addWidget(self.selectContainerXMLBtn, 3, 2, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.gridLayout_19.addWidget(self.label_90, 4, 0, 1, 1)
        self.selectOutputDirInput = QtWidgets.QLineEdit(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.selectOutputDirInput.setFont(font)
        self.selectOutputDirInput.setReadOnly(True)
        self.selectOutputDirInput.setObjectName("selectOutputDirInput")
        self.gridLayout_19.addWidget(self.selectOutputDirInput, 4, 1, 1, 1)
        self.selectOutputDirBtn = QtWidgets.QToolButton(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectOutputDirBtn.setFont(font)
        self.selectOutputDirBtn.setObjectName("selectOutputDirBtn")
        self.gridLayout_19.addWidget(self.selectOutputDirBtn, 4, 2, 1, 1)
        self.layoutWidget_12 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_12.setGeometry(QtCore.QRect(594, 370, 301, 131))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.layoutWidget_12)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.objClassField = QtWidgets.QLineEdit(self.layoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.objClassField.setFont(font)
        self.objClassField.setText("")
        self.objClassField.setObjectName("objClassField")
        self.gridLayout_20.addWidget(self.objClassField, 1, 0, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.layoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.gridLayout_20.addWidget(self.label_91, 0, 0, 1, 1)
        self.openFolderCheckbox = QtWidgets.QCheckBox(self.layoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openFolderCheckbox.setFont(font)
        self.openFolderCheckbox.setIconSize(QtCore.QSize(16, 16))
        self.openFolderCheckbox.setChecked(True)
        self.openFolderCheckbox.setObjectName("openFolderCheckbox")
        self.gridLayout_20.addWidget(self.openFolderCheckbox, 2, 0, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 360, 461, 151))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_83 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.gridLayout_23.addWidget(self.label_83, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.numContainersSlider = QtWidgets.QSlider(self.layoutWidget4)
        self.numContainersSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numContainersSlider.setMinimum(1)
        self.numContainersSlider.setMaximum(20)
        self.numContainersSlider.setSingleStep(5)
        self.numContainersSlider.setProperty("value", 1)
        self.numContainersSlider.setSliderPosition(1)
        self.numContainersSlider.setOrientation(QtCore.Qt.Horizontal)
        self.numContainersSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.numContainersSlider.setTickInterval(0)
        self.numContainersSlider.setObjectName("numContainersSlider")
        self.gridLayout_15.addWidget(self.numContainersSlider, 1, 1, 1, 1)
        self.numContainersBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.numContainersBox.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numContainersBox.setFont(font)
        self.numContainersBox.setMinimum(1)
        self.numContainersBox.setMaximum(20)
        self.numContainersBox.setProperty("value", 1)
        self.numContainersBox.setObjectName("numContainersBox")
        self.gridLayout_15.addWidget(self.numContainersBox, 1, 2, 1, 1)
        self.numThreatsSlider = QtWidgets.QSlider(self.layoutWidget4)
        self.numThreatsSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numThreatsSlider.setMinimum(1)
        self.numThreatsSlider.setMaximum(20)
        self.numThreatsSlider.setSingleStep(5)
        self.numThreatsSlider.setProperty("value", 1)
        self.numThreatsSlider.setSliderPosition(1)
        self.numThreatsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.numThreatsSlider.setInvertedAppearance(False)
        self.numThreatsSlider.setInvertedControls(False)
        self.numThreatsSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.numThreatsSlider.setObjectName("numThreatsSlider")
        self.gridLayout_15.addWidget(self.numThreatsSlider, 0, 1, 1, 1)
        self.numThreatsBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.numThreatsBox.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numThreatsBox.setFont(font)
        self.numThreatsBox.setMinimum(1)
        self.numThreatsBox.setMaximum(20)
        self.numThreatsBox.setProperty("value", 1)
        self.numThreatsBox.setProperty("currNumThreat", 0)
        self.numThreatsBox.setObjectName("numThreatsBox")
        self.gridLayout_15.addWidget(self.numThreatsBox, 0, 2, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.gridLayout_15.addWidget(self.label_70, 1, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout_15.addWidget(self.label_71, 2, 0, 1, 1)
        self.numImagesOutSlider = QtWidgets.QSlider(self.layoutWidget4)
        self.numImagesOutSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numImagesOutSlider.setMinimum(1)
        self.numImagesOutSlider.setMaximum(1000)
        self.numImagesOutSlider.setSingleStep(50)
        self.numImagesOutSlider.setProperty("value", 1)
        self.numImagesOutSlider.setSliderPosition(1)
        self.numImagesOutSlider.setOrientation(QtCore.Qt.Horizontal)
        self.numImagesOutSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.numImagesOutSlider.setTickInterval(0)
        self.numImagesOutSlider.setObjectName("numImagesOutSlider")
        self.gridLayout_15.addWidget(self.numImagesOutSlider, 2, 1, 1, 1)
        self.numImagesOutBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.numImagesOutBox.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numImagesOutBox.setFont(font)
        self.numImagesOutBox.setMinimum(1)
        self.numImagesOutBox.setMaximum(1000)
        self.numImagesOutBox.setSingleStep(10)
        self.numImagesOutBox.setProperty("value", 1)
        self.numImagesOutBox.setObjectName("numImagesOutBox")
        self.gridLayout_15.addWidget(self.numImagesOutBox, 2, 2, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout_15.addWidget(self.label_72, 0, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 540, 461, 147))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_77 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.gridLayout_24.addWidget(self.label_77, 0, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_78 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.gridLayout_17.addWidget(self.label_78, 0, 1, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.gridLayout_17.addWidget(self.label_79, 0, 2, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.gridLayout_17.addWidget(self.label_80, 1, 0, 1, 1)
        self.threatMin = QtWidgets.QSpinBox(self.layoutWidget5)
        self.threatMin.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threatMin.setFont(font)
        self.threatMin.setMinimum(1)
        self.threatMin.setMaximum(20)
        self.threatMin.setProperty("value", 1)
        self.threatMin.setObjectName("threatMin")
        self.gridLayout_17.addWidget(self.threatMin, 1, 1, 1, 1)
        self.threatMax = QtWidgets.QSpinBox(self.layoutWidget5)
        self.threatMax.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threatMax.setFont(font)
        self.threatMax.setMinimum(1)
        self.threatMax.setMaximum(20)
        self.threatMax.setProperty("value", 5)
        self.threatMax.setObjectName("threatMax")
        self.gridLayout_17.addWidget(self.threatMax, 1, 2, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.gridLayout_17.addWidget(self.label_81, 2, 0, 1, 1)
        self.rotationMin = QtWidgets.QSpinBox(self.layoutWidget5)
        self.rotationMin.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rotationMin.setFont(font)
        self.rotationMin.setMinimum(0)
        self.rotationMin.setMaximum(360)
        self.rotationMin.setSingleStep(10)
        self.rotationMin.setProperty("value", 0)
        self.rotationMin.setObjectName("rotationMin")
        self.gridLayout_17.addWidget(self.rotationMin, 2, 1, 1, 1)
        self.rotationMax = QtWidgets.QSpinBox(self.layoutWidget5)
        self.rotationMax.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rotationMax.setFont(font)
        self.rotationMax.setMinimum(0)
        self.rotationMax.setMaximum(360)
        self.rotationMax.setSingleStep(10)
        self.rotationMax.setProperty("value", 360)
        self.rotationMax.setObjectName("rotationMax")
        self.gridLayout_17.addWidget(self.rotationMax, 2, 2, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.gridLayout_17.addWidget(self.label_82, 3, 0, 1, 1)
        self.bgMin = QtWidgets.QSpinBox(self.layoutWidget5)
        self.bgMin.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bgMin.setFont(font)
        self.bgMin.setMinimum(0)
        self.bgMin.setMaximum(255)
        self.bgMin.setProperty("value", 240)
        self.bgMin.setObjectName("bgMin")
        self.gridLayout_17.addWidget(self.bgMin, 3, 1, 1, 1)
        self.bgMax = QtWidgets.QSpinBox(self.layoutWidget5)
        self.bgMax.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bgMax.setFont(font)
        self.bgMax.setMinimum(0)
        self.bgMax.setMaximum(255)
        self.bgMax.setProperty("value", 243)
        self.bgMax.setObjectName("bgMax")
        self.gridLayout_17.addWidget(self.bgMax, 3, 2, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_17, 1, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.tab_4)
        self.widget2.setGeometry(QtCore.QRect(540, 600, 351, 71))
        self.widget2.setObjectName("widget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.minBboxSize = QtWidgets.QSpinBox(self.widget2)
        self.minBboxSize.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minBboxSize.setFont(font)
        self.minBboxSize.setMinimum(100)
        self.minBboxSize.setMaximum(500)
        self.minBboxSize.setSingleStep(10)
        self.minBboxSize.setProperty("value", 300)
        self.minBboxSize.setObjectName("minBboxSize")
        self.gridLayout_3.addWidget(self.minBboxSize, 1, 1, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.gridLayout_3.addWidget(self.label_84, 0, 0, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.gridLayout_3.addWidget(self.label_85, 1, 0, 1, 1)
        self.magRatio = QtWidgets.QDoubleSpinBox(self.widget2)
        self.magRatio.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.magRatio.setFont(font)
        self.magRatio.setMaximum(3.0)
        self.magRatio.setSingleStep(0.25)
        self.magRatio.setProperty("value", 1.5)
        self.magRatio.setObjectName("magRatio")
        self.gridLayout_3.addWidget(self.magRatio, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.VideoExtSlider.valueChanged['int'].connect(self.VideoExtSliderBox.setValue)
        self.VideoExtSliderBox.valueChanged['int'].connect(self.VideoExtSlider.setValue)
        self.overlayNumObjSlider.valueChanged['int'].connect(self.overlayNumObjBox.setValue)
        self.overlayNumObjBox.valueChanged['int'].connect(self.overlayNumObjSlider.setValue)
        self.numThreatsSlider.valueChanged['int'].connect(self.numThreatsBox.setValue)
        self.numThreatsBox.valueChanged['int'].connect(self.numThreatsSlider.setValue)
        self.numContainersSlider.valueChanged['int'].connect(self.numContainersBox.setValue)
        self.numContainersBox.valueChanged['int'].connect(self.numContainersSlider.setValue)
        self.numImagesOutSlider.valueChanged['int'].connect(self.numImagesOutBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        ###### MY OWN CODE - EVENT LISTENERS FOR BUTTONS ######

        ## AutoCrop Event Listeners
        # File selection buttons
        self.AutoCropInputBtn.clicked.connect(self.AutoCropInputBtnFn)
        self.AutoCropXMLInputBtn.clicked.connect(self.AutoCropXMLInputBtnFn)
        self.AutoCropOutputBtn.clicked.connect(self.AutoCropOutputBtnFn)

        # Generate button
        self.AutoCropRunBtn.clicked.connect(self.crop_from_manual_XML)


        ## Video Extractor Event Listeners
        # File selection buttons
        self.VideoExtInputBtn.clicked.connect(self.VideoExtInputBtnFn)
        self.VideoExtOutputBtn.clicked.connect(self.VideoExtOutputBtnFn)

        # Generate button
        self.VideoExtRunBtn.clicked.connect(self.capture_video)


        ## AutoOverlay Event Listeners
        # File selection buttons
        self.overlayObjectInputBtn.clicked.connect(self.overlayObjectInputBtnFn)
        self.overlayBGInputBtn.clicked.connect(self.overlayBGInputBtnFn)
        self.overlayOutputBtn.clicked.connect(self.overlayOutputBtnFn)

        # Generate button
        self.OverlayRunProgBtn.clicked.connect(self.mainFx_Overlay)


        ## TIP Event Listeners & Dynamic Code
        self.numContainersSlider.valueChanged['int'].connect(self.numImagesOutBox.setMinimum)
        self.numContainersSlider.valueChanged['int'].connect(self.numImagesOutSlider.setMinimum)
        self.numContainersBox.valueChanged['int'].connect(self.numImagesOutBox.setMinimum)
        self.numContainersBox.valueChanged['int'].connect(self.numImagesOutSlider.setMinimum)

        # File selection buttons
        self.selectThreatFilesBtn.clicked.connect(self.selectThreatFileFx)
        self.selectContainerFilesBtn.clicked.connect(self.selectContainerFileFx)
        self.selectContainerXMLBtn.clicked.connect(self.selectContainerXMLFx)
        self.selectOutputDirBtn.clicked.connect(self.selectOutputDirFx)

        # Generate button
        self.RunProgBtn.clicked.connect(self.mainFx)

        ###### MY OWN CODE END ######



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Processing Toolbox"))
        self.label_47.setText(_translate("MainWindow", "Auto Object Overlay (Staged Scene Generator)"))
        self.label_48.setText(_translate("MainWindow", "Automatically overlays objects onto empty spaces of a given image."))
        self.label_49.setText(_translate("MainWindow", "Used to rapidly create staged scenes for AI training. Generates PascalVOC format XML annotations."))
        self.label_50.setText(_translate("MainWindow", "by Wang Jiale, Jul/Aug 2021"))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"HTX logo.png\" width=\"100\"/></p></body></html>"))
        self.label_56.setText(_translate("MainWindow", "Output Directory:"))
        self.label_54.setText(_translate("MainWindow", "Background Images:"))
        self.label_52.setText(_translate("MainWindow", "Step 1: Select Directories"))
        self.overlayObjectInputBtn.setText(_translate("MainWindow", "..."))
        self.overlayOutput.setText(_translate("MainWindow", "C:/ ..."))
        self.label_53.setText(_translate("MainWindow", "Object Images:"))
        self.overlayOutputBtn.setText(_translate("MainWindow", "..."))
        self.overlayBGInput.setText(_translate("MainWindow", "C:/ ..."))
        self.overlayObjectInput.setText(_translate("MainWindow", "C:/ ..."))
        self.overlayBGInputBtn.setText(_translate("MainWindow", "..."))
        self.OverlayRunProgBtn.setText(_translate("MainWindow", "Generate Overlay Images!"))
        self.label_64.setText(_translate("MainWindow", "Step 3: Advanced Settings (Optional)"))
        self.label_68.setText(_translate("MainWindow", "Rotation Range (Degs):"))
        self.label_66.setText(_translate("MainWindow", "Max"))
        self.label_67.setText(_translate("MainWindow", "Objects per Image:"))
        self.label_65.setText(_translate("MainWindow", "Min"))
        self.label_55.setText(_translate("MainWindow", "Step 2: Specify Parameters"))
        self.label_58.setText(_translate("MainWindow", "Max no. of times to try and place objects on a single image:"))
        self.label_59.setText(_translate("MainWindow", "(Large number = slower programme. Recommended: 100)"))
        self.label_57.setText(_translate("MainWindow", "Type of Object (Class):"))
        self.overlayClass.setPlaceholderText(_translate("MainWindow", "Name of Class"))
        self.label_61.setText(_translate("MainWindow", "Give a name for object (e.g \"parcel\"). Type \"multiple\" for multiple classes."))
        self.label_63.setText(_translate("MainWindow", "Multiple class names extracted from filename, e.g. cat_2.jpg = \"cat\" class"))
        self.OverlayOpenFolderCheckbox.setText(_translate("MainWindow", "Open Output Folder afterwards"))
        self.label_92.setText(_translate("MainWindow", "Background removal threshold:"))
        self.label_69.setText(_translate("MainWindow", "Max. Times of Magnification:"))
        self.overlayWhitespaceOnlyCheck.setText(_translate("MainWindow", "Put in Empty Space Only?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "AutoOverlay"))
        self.label_2.setText(_translate("MainWindow", "Auto Image Cropper"))
        self.label_22.setText(_translate("MainWindow", "Given any image and its associated PascalVOC format XML label, this programme crops"))
        self.label_24.setText(_translate("MainWindow", "out the objects for you, according to their Bounding Boxes.  Supports .jpg, .png, .tiff, .tif"))
        self.label_20.setText(_translate("MainWindow", "by Wang Jiale, Jul/Aug 2021"))
        self.AutoCropCheckbox.setText(_translate("MainWindow", "Open Output Folder afterwards"))
        self.AutoCropRunBtn.setText(_translate("MainWindow", "Generate Cropped Images!"))
        self.label_21.setText(_translate("MainWindow", "Images to Crop (Folder):"))
        self.AutoCropInput.setText(_translate("MainWindow", "C:/ ..."))
        self.AutoCropInputBtn.setText(_translate("MainWindow", "..."))
        self.label_25.setText(_translate("MainWindow", "XML Annotations (Folder):"))
        self.AutoCropXMLInput.setText(_translate("MainWindow", "C:/ ..."))
        self.AutoCropXMLInputBtn.setText(_translate("MainWindow", "..."))
        self.label_28.setText(_translate("MainWindow", "Note: XML files must be the same name as the images. Must be in PASCAL VOC format!"))
        self.AutoCropOutputBtn.setText(_translate("MainWindow", "..."))
        self.AutoCropOutput.setText(_translate("MainWindow", "C:/ ..."))
        self.label_27.setText(_translate("MainWindow", "Output Directory:"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"HTX logo.png\" width=\"100\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "AutoCropper"))
        self.label_31.setText(_translate("MainWindow", "by Wang Jiale, Jul/Aug 2021"))
        self.label_3.setText(_translate("MainWindow", "Extract Images from Video"))
        self.VideoExtInputBtn.setText(_translate("MainWindow", "..."))
        self.VideoExtInput.setText(_translate("MainWindow", "C:/ ..."))
        self.VideoExtOutputBtn.setText(_translate("MainWindow", "..."))
        self.label_29.setText(_translate("MainWindow", "Select Video:"))
        self.VideoExtOutput.setText(_translate("MainWindow", "C:/ ..."))
        self.label_34.setText(_translate("MainWindow", "Output Directory:"))
        self.VideoExtRunBtn.setText(_translate("MainWindow", "Extract Images!"))
        self.VideoExtCheckbox.setText(_translate("MainWindow", "Open Output Folder afterwards"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"HTX logo.png\" width=\"100\"/></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "Frequency of Image Extraction (seconds)"))
        self.label_32.setText(_translate("MainWindow", "Note: Do not exceed the total length of the video! Will cause error."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Video Extractor"))
        self.label_73.setText(_translate("MainWindow", "Threat Image Projection (TIP) - Smuggling Simulator"))
        self.label_74.setText(_translate("MainWindow", "This programme automatically superimposes grayscale X-ray scans of objects onto another X-ray image."))
        self.label_75.setText(_translate("MainWindow", "Used to produce large datasets for training X-ray Object Detection ML models."))
        self.label_76.setText(_translate("MainWindow", "by Wang Jiale, Jul 2021"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"HTX logo.png\" width=\"100\"/></p></body></html>"))
        self.RunProgBtn.setText(_translate("MainWindow", "Generate Images!"))
        self.label_86.setText(_translate("MainWindow", "Step 1: Select Directories"))
        self.label_87.setText(_translate("MainWindow", "Object Images:"))
        self.selectThreatFilesInput.setText(_translate("MainWindow", "C:/ ..."))
        self.selectThreatFilesBtn.setText(_translate("MainWindow", "..."))
        self.label_88.setText(_translate("MainWindow", "Background Images:"))
        self.selectContainerFilesInput.setText(_translate("MainWindow", "C:/ ..."))
        self.selectContainerFilesBtn.setText(_translate("MainWindow", "..."))
        self.label_89.setText(_translate("MainWindow", "Background Images\' \n"
"PascalVOC XML Labels:"))
        self.selectContainerXMLInput.setText(_translate("MainWindow", "C:/ ..."))
        self.selectContainerXMLBtn.setText(_translate("MainWindow", "..."))
        self.label_90.setText(_translate("MainWindow", "Output Directory:"))
        self.selectOutputDirInput.setText(_translate("MainWindow", "C:/ ..."))
        self.selectOutputDirBtn.setText(_translate("MainWindow", "..."))
        self.objClassField.setPlaceholderText(_translate("MainWindow", "Name of Class"))
        self.label_91.setText(_translate("MainWindow", "Type of Object (Class):"))
        self.openFolderCheckbox.setText(_translate("MainWindow", "Open Output Folder afterwards"))
        self.label_83.setText(_translate("MainWindow", "Step 2: Specify Parameters"))
        self.label_70.setText(_translate("MainWindow", "No. of Containers to use:"))
        self.label_71.setText(_translate("MainWindow", "No. of Images to Generate:"))
        self.label_72.setText(_translate("MainWindow", "No. of Threats to use:"))
        self.label_77.setText(_translate("MainWindow", "Step 3: Advanced Settings (Optional)"))
        self.label_78.setText(_translate("MainWindow", "Min"))
        self.label_79.setText(_translate("MainWindow", "Max"))
        self.label_80.setText(_translate("MainWindow", "Threats per Image:"))
        self.label_81.setText(_translate("MainWindow", "Rotation Range (Degs):"))
        self.label_82.setText(_translate("MainWindow", "Background Removal Threshold:"))
        self.label_84.setText(_translate("MainWindow", "Max. Times of Magnification:"))
        self.label_85.setText(_translate("MainWindow", "Minimum Container Size (px):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Threat Image Projection"))



    ###### MY OWN CODE ######

    ### AutoCrop Logic
    def AutoCropInputBtnFn(self):
        self.autocrop_image_dir = QFileDialog.getExistingDirectory()
        self.AutoCropInput.setText(self.autocrop_image_dir)

    def AutoCropXMLInputBtnFn(self):
        self.autocrop_xml_folder = QFileDialog.getExistingDirectory()
        self.AutoCropXMLInput.setText(self.autocrop_xml_folder)

    def AutoCropOutputBtnFn(self):
        self.autocrop_output_dir = QFileDialog.getExistingDirectory()
        self.AutoCropOutput.setText(self.autocrop_output_dir)

    def printLog_AutoCrop(self, textToPrint):
        """
        Status Report printing
        """
        self.AutoCropStatus.appendPlainText(textToPrint)
        self.AutoCropStatus.repaint()

    def crop_from_manual_XML(self):
        """
        Given a PascalVOC XML annotation file and the asociated image, this script
        automatically crops out the objects enclosed within the bounding boxes and saves
        them as standalone images.
        """
        # Clear output box
        self.AutoCropStatus.setPlainText('')

        xml_folder_dir = self.autocrop_xml_folder
        crop_images_output_dir = os.path.join(self.autocrop_output_dir, 'cropped_images',
                                              f'autocropper_{datetime.now().strftime("%Y_%m_%d-%H-%M-%S")}')

        # Create new crop folder in output
        if not os.path.exists(crop_images_output_dir):
            os.makedirs(crop_images_output_dir)

        # Get full list of XML files
        xml_list = [name for name in os.listdir(xml_folder_dir) if
                    os.path.isfile(os.path.join(xml_folder_dir, name))]

        for i, xml_file in enumerate(xml_list):
            # Get name of XML file
            xml_filename_noext = os.path.splitext(xml_file)[0]

            # Read XML file
            tree = ET.parse(os.path.join(xml_folder_dir, xml_file))
            my_root = tree.getroot()

            # Open relevant image from main dataset
            curr_img = cv2.imread(os.path.join(self.autocrop_image_dir, f'{xml_filename_noext}.png'))
            if curr_img is None:
                curr_img = cv2.imread(os.path.join(self.autocrop_image_dir, f'{xml_filename_noext}.jpg'))
                if curr_img is None:
                    curr_img = cv2.imread(os.path.join(self.autocrop_image_dir, f'{xml_filename_noext}.tiff'))
                    if curr_img is None:
                        curr_img = cv2.imread(os.path.join(self.autocrop_image_dir, f'{xml_filename_noext}.tif'))
                        if curr_img is None:
                            self.printLog_AutoCrop(
                                f"Skipped {xml_filename_noext} as image not found or not of right format. XML label must be the same name as image!")
                            continue

            # Extract bbox coords
            name_dict = {}  # Dictionary containing class names and their num of appearances (for generating filenames)
            for member in my_root.findall('object'):

                values = (int(member[4][0].text),
                          int(member[4][1].text),
                          int(member[4][2].text),
                          int(member[4][3].text),
                          member[0].text
                          )

                # Create dictionary of names
                if name_dict.get(values[4]) == None:
                    name_dict[values[4]] = 1
                else:
                    name_dict[values[4]] += 1

                # Crop image
                crop_img = curr_img[values[1]:values[3], values[0]:values[2]]

                # Choose unique filename that also reveals the classname
                filename = f"{xml_filename_noext}_{values[4]}_{name_dict[values[4]]}.png"

                # Save image
                cv2.imwrite(os.path.join(crop_images_output_dir, filename), crop_img)

            # Counter
            if (i + 1) % 2 == 0 or i == (len(xml_list) - 1):
                self.printLog_AutoCrop(f"{i + 1}/{len(xml_list)} processed!")

        self.printLog_AutoCrop("Success! Images cropped. See 'cropped_images' folder")

        # Opens output folder if checkbox is checked
        if self.AutoCropCheckbox.isChecked():
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, crop_images_output_dir])


    ### Video Extractor Logic
    def VideoExtInputBtnFn(self):
        self.vid_videoFile = QFileDialog.getOpenFileName()[0]
        self.VideoExtInput.setText(self.vid_videoFile)

    def VideoExtOutputBtnFn(self):
        self.vid_outputFolder = QFileDialog.getExistingDirectory()
        self.VideoExtOutput.setText(self.vid_outputFolder)

    def printLog_VideoCrop(self, textToPrint):
        """
        Status Report printing
        """
        self.VideoExtStatus.appendPlainText(textToPrint)
        self.VideoExtStatus.repaint()

    def capture_video(self):
        # Clear output box
        self.VideoExtStatus.setPlainText('Running Script\n')
        self.VideoExtStatus.repaint()

        # Get value from box
        self.captureFreq = self.VideoExtSliderBox.value()

        # Capture video
        cap = cv2.VideoCapture(self.vid_videoFile)

        # Calc frame capture rate
        frameRate = self.captureFreq * math.ceil(cap.get(5))

        # Create output file
        full_output_dir = os.path.join(self.vid_outputFolder,
                                       f'vidOutput_{datetime.now().strftime("%Y_%m_%d-%H.%M.%S")}')
        if not os.path.exists(full_output_dir):
            os.makedirs(full_output_dir)

        while (cap.isOpened()):
            frameId = cap.get(1)  # current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate) == 0):
                filename = full_output_dir + "/image_" + str(int(frameId // math.floor(frameRate))) + ".jpg"
                cv2.imwrite(filename, frame)
                if (frameId % 10) == 0:
                    self.printLog_VideoCrop(f"Taking frame at {int(frameId // math.floor(cap.get(5)))} seconds")

        cap.release()
        self.printLog_VideoCrop("Done!")

        # Opens output folder if checkbox is checked
        if self.VideoExtCheckbox.isChecked():
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, full_output_dir])


    ### AutoOverlay Logic
    def overlayObjectInputBtnFn(self):
        self.overlay_obj_dir = QFileDialog.getExistingDirectory()
        self.overlayObjectInput.setText(self.overlay_obj_dir)

    def overlayBGInputBtnFn(self):
        self.overlay_bg_dir = QFileDialog.getExistingDirectory()
        self.overlayBGInput.setText(self.overlay_bg_dir)

    def overlayOutputBtnFn(self):
        self.overlay_output_dir = QFileDialog.getExistingDirectory()
        self.overlayOutput.setText(self.overlay_output_dir)

    def printLog_Overlay(self, textToPrint):
        """
        Status Report printing
        """
        self.OverlayStatusReportBox.appendPlainText(textToPrint)
        self.OverlayStatusReportBox.repaint()

    # Main Function for overlay
    def mainFx_Overlay(self):

        # Clear textbox
        self.OverlayStatusReportBox.setPlainText('')
        self.OverlayStatusReportBox.repaint()

        # Generate output folder name
        self.overlay_out_dir_full = os.path.join(self.overlay_output_dir, "overlay_output", datetime.now().strftime("%Y_%m_%d-%H.%M.%S"))

        # Assign variables based on input value
        self.overlay_MAX_ATTEMPTS = self.overlayNumObjBox.value()
        self.overlay_obj_class = 'Untitled' if self.overlayClass.text()=='' else self.overlayClass.text()

        self.overlay_rotation_range = [self.overlayRotationMin.value(), self.overlayRotationMax.value()]
        self.overlay_number_objects_per_image = [self.overlayObjMin.value(), self.overlayObjMax.value()]

        self.overlay_max_magnification = self.overlayMagRatio.value()
        self.overlay_bg_removal_threshold = self.overlayBgThreshold.value()

        self.overlay_white_space_hunter = self.overlayWhitespaceOnlyCheck.isChecked()

        # Run everything
        self.generate_images()

        # Open folder if needed
        if self.OverlayOpenFolderCheckbox.isChecked():
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.overlay_out_dir_full])


    # Overlay Helpers
    def generate_images(self):
        """
        Main function
        """
        # Output Directory
        out_dir_full = self.overlay_out_dir_full
        os.makedirs(out_dir_full)
        os.makedirs(os.path.join(out_dir_full, "images"))
        os.makedirs(os.path.join(out_dir_full, "annotations"))

        # Get list of files
        obj_files_list = [file for file in os.listdir(self.overlay_obj_dir)
                          if os.path.isfile(os.path.join(self.overlay_obj_dir, file))]
        bg_files_list = [file for file in os.listdir(self.overlay_bg_dir)
                         if os.path.isfile(os.path.join(self.overlay_bg_dir, file))]

        self.printLog_Overlay(f"Processing {len(bg_files_list)} images...\n")
        # Iteratively take bgs and start pasting stuff
        for im_indx, bg in enumerate(bg_files_list):

            # Counter to count number of attempts spent on this image
            attempt_count = 0
            obj_count = 0

            # Decide number of objects to put
            obj_to_place = \
            np.random.randint(self.overlay_number_objects_per_image[0], self.overlay_number_objects_per_image[1] + 1,
                              size=1)[0]

            # Open background image & Get dimensions
            image_bg = cv2.imread(os.path.join(self.overlay_bg_dir, bg))
            height_bg, width_bg, _ = image_bg.shape
            img_name_noext = os.path.splitext(bg)[0]

            # Creates XML annotations file
            xml_annotation = self.create_xml_backbone_overlay(f"overlay_{img_name_noext}.jpg",
                                                         os.path.join(out_dir_full, "annotations"),
                                                         width_bg, height_bg)

            # Keep placing objects until run out of iterations or number to place is reached!
            while attempt_count < self.overlay_MAX_ATTEMPTS and obj_count < obj_to_place:

                #             self.printLog_Overlay("\nPlacing objects now...")
                fail_flag = True

                while fail_flag:

                    # Choose object & rotate & magnify
                    chosen_obj = random.choice(obj_files_list)
                    rotate_angle = \
                    np.random.randint(self.overlay_rotation_range[0], self.overlay_rotation_range[1], size=1)[0]
                    mag_factor_d = np.random.uniform(low=0, high=1, size=1)[0]

                    # Open, rotate, and crop object
                    image_obj_PIL = Image.open(os.path.join(self.overlay_obj_dir, chosen_obj)).convert('RGB')
                    image_obj_CV = self.rotate_and_crop(image_obj_PIL, rotate_angle, mag_factor_d)

                    # Get dimensions of object
                    height_obj, width_obj, _ = image_obj_CV.shape

                    # Get coords to place object (x,y)
                    placement_coords, try_count = self.determine_random_coords_overlay(image_bg, height_obj, width_obj, height_bg,
                                                                          width_bg)

                    # Update counter
                    attempt_count += try_count

                    # Place 1 object
                    if placement_coords != None:
                        obj_count += 1
                        fail_flag = False
                        # Place object onto background
                        #                     self.printLog_Overlay("One object placed...")

                        # Iterate thru pixels in object image, remove white bg
                        for x, row in enumerate(image_obj_CV):
                            for y, entry in enumerate(row):
                                if np.mean(entry) <= self.overlay_bg_removal_threshold:
                                    image_bg[placement_coords[1] + x, placement_coords[0] + y] = image_obj_CV[x, y]

                        # Update XML annotation
                        xml_annotation = self.update_bbox_in_XML_overlay(xml_annotation, os.path.splitext(chosen_obj)[0],
                                                                    placement_coords,
                                                                    width_obj, height_obj)

                    if attempt_count >= self.overlay_MAX_ATTEMPTS:
                        break

            # Save image
            cv2.imwrite(os.path.join(out_dir_full, "images", f"overlay_{img_name_noext}.jpg"), image_bg)

            # Status message
            if len(bg_files_list) < 30:
                self.printLog_Overlay(f"{obj_count} objects placed onto {bg}. Staged image Saved.")
                if obj_count == 0:
                    self.printLog_Overlay(
                        f"No objects placed due to inability to find suitable spot within self.overlay_MAX_ATTEMPTS={self.overlay_MAX_ATTEMPTS}")
                self.printLog_Overlay("XML Label saved.")
            elif im_indx % 10 == 0 and im_indx != 0:
                self.printLog_Overlay(f"{im_indx}/{len(bg_files_list)} images processed.")

            # Write and save XML
            dom = minidom.parseString(ET.tostring(xml_annotation))
            xml_out = dom.toprettyxml(indent='\t')
            with open(os.path.join(out_dir_full, "annotations", f"overlay_{img_name_noext}.xml"), "w") as f:
                f.write(xml_out)

        self.printLog_Overlay("\nAll done!")

    def determine_random_coords_overlay(self, image_bg, height_obj, width_obj, height_bg, width_bg):
        """
        Generate a random coordinate to place object
        Checks that it is against white background!

        Inputs:


        Output:
            1. Placement_coords (2x1 tuple) OR None if no suitable coords found!
               - Random coordinates to place object at (x,y)
            2. try_count
                - Number of iterations within current run
        """
        # Get coords of background
        xmin, ymin = (0, 0)
        xmax, ymax = (width_bg, height_bg)

        # Generate placement coords & compute max coords and checks
        # 1. if threat image lies outside container (not allowed)
        # 2. that entire placement area is white
        pass_flag = False
        try_count = 0

        while not pass_flag:
            try_count += 1

            # Generate (x,y) coords and max_coords
            placement_coords = [np.random.randint(low=xmin, high=xmax, size=1)[0],
                                np.random.randint(low=ymin, high=ymax, size=1)[0]]
            max_coords = [placement_coords[0] + width_obj, placement_coords[1] + height_obj]

            #         self.printLog_Overlay(max_coords)

            # Check if slice within image
            is_within_image = (self.check_within_box(xmin, ymin, xmax, ymax, placement_coords[0], placement_coords[1])
                               and self.check_within_box(xmin, ymin, xmax, ymax, max_coords[0], max_coords[1]))

            #         self.printLog_Overlay(f"Within img = {is_within_image}")

            # Check if proposed placement region is white (if required) and within image
            if is_within_image:
                if self.overlay_white_space_hunter:
                    image_slice = image_bg[placement_coords[1]:placement_coords[1] + height_obj,
                                  placement_coords[0]:placement_coords[0] + width_obj]

                    region_is_white = self.all_white_pixels(image_slice)
                #             self.printLog_Overlay(image_slice)
                else:
                    region_is_white = True

            else:
                region_is_white = False

            # Check if proposed coords passes the test
            pass_flag = (is_within_image and region_is_white)
            #         pass_flag = (is_within_image or region_is_white)

            # Stop trying if no suitable spot found
            if try_count >= 100:
                return None, try_count

        return placement_coords, try_count  # (x,y)

    def check_within_box(self, xmin, ymin, xmax, ymax, x, y):
        """
        Helper function: Check if coords (x,y) within bounding box

        True if within box
        """
        return (x > xmin and x < xmax and y > ymin and y < ymax)

    def rotate_and_crop(self, img_PIL, rotation_deg=0, mag_factor_d=1):
        """
        Rotates image and crops it

        Input:
            1. img_PIL: PIL Object

        Output:
            1. img_cv: OpenCV Object
        """
        # Magnify
        (width, height) = (img_PIL.width, img_PIL.height)
        mag_factor = 1 + mag_factor_d * (self.overlay_max_magnification - 1)
        img_PIL = img_PIL.resize((int(round(width * mag_factor)), int(round(height * mag_factor))))

        # Rotate
        img_PIL = img_PIL.rotate(angle=rotation_deg, expand=1, fillcolor=(255, 255, 255))

        # Crop
        img_PIL = self.trim(img_PIL)

        # Convert to OpenCV object
        img_cv = np.array(img_PIL)
        img_cv = img_cv[:, :, ::-1].copy()  # Convert RGB to BGR

        return img_cv

    def trim(self, im):
        """
        Automatically trims away the excess whitespace in a gun image to get a tighter bounding box.

        Input:
            1. im (PIL Object)
                - Background layer of im MUST be set to L=255

        Output:
            1. im_cropped (PIL Object)
               - Cropped image
        """
        #     # Iterate thru pixels in object image, remove white bg
        #     im_np = np.array(im)
        #     for x, row in enumerate(im_np):
        #         for y, entry in enumerate(row):
        #             if np.mean(entry)>=self.overlay_bg_removal_threshold:
        #                 im_np[x,y]=[255,255,255]
        #     im=Image.fromarray(im_np)

        # Create bg mask of only white colour
        bg = Image.new(im.mode, im.size, 255)

        # Pixel by pixel comparison of image and background. All pixels with 255 on image should have value 0 in "diff"
        diff = ImageChops.difference(im, bg)

        # adds two images, dividing the result by scale and adding the offset
        diff = ImageChops.add(diff, diff, scale=1.0, offset=0)

        # Gets non-zero bounding box of image (ie crops image)
        bbox = diff.getbbox()

        # Crop image according to bounding box
        im_cropped = im.crop(bbox)

        return im_cropped

    def all_white_pixels(self, image):
        """
        Returns True if all white pixels or False if not all white
        """
        white_flag = True

        H, W = image.shape[:2]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        for pixel in gray:
            if np.mean(pixel) <= 245:
                white_flag = False

        return white_flag

    def update_bbox_in_XML_overlay(self, xml_annotation, selected_threat, placement_coords,
                                   threat_width, threat_height):
        """
        Adds bounding box info "Object Node" into XML labels file

        Inputs:
            1. xml_annotation (XML ElementTree Object)
            2. selected_threat (Name without file extension)
            3. placement_coords (Tuple in x,y format)
            4. threat_width (x)
            5. threat_height (y)

        Returns:
            1.  xml_annotation (XML ElementTree Object)
        """
        myObject = ET.SubElement(xml_annotation, "object")

        # Get threat class
        #### UNCOMMENT THIS FOR CUSTOMISABLE THREAT CLASS, ELSE ALL SET AS "RIFLE" ######

        #   threat_tree = ET.parse(os.path.join(root, threats_dir, "annotations", f"{selected_threat}.xml"))
        #   threat_class = threat_tree.find("object").find("name").text

        if self.overlay_obj_class == "multiple":
            object_class = selected_threat.split('_')[0]
        else:
            object_class = self.overlay_obj_class

        # Object child nodes
        ET.SubElement(myObject, "name").text = str(object_class)
        ET.SubElement(myObject, "pose").text = "Unspecified"
        ET.SubElement(myObject, "truncated").text = "0"
        ET.SubElement(myObject, "difficult").text = "0"
        bndbox = ET.SubElement(myObject, "bndbox")

        # bndbox child nodes
        ET.SubElement(bndbox, "xmin").text = str(placement_coords[0])
        ET.SubElement(bndbox, "ymin").text = str(placement_coords[1])
        ET.SubElement(bndbox, "xmax").text = str(placement_coords[0] + threat_width)
        ET.SubElement(bndbox, "ymax").text = str(placement_coords[1] + threat_height)

        return xml_annotation

    def create_xml_backbone_overlay(self, curr_filename, save_dir, img_width, img_height):
        """
        PascalVOC Format
        Creates backbone of XML label file, populating tree with everything except object bounding box labels

        Returns:
            1. xml_annotation (ElementTree Object)
        """
        # Main node
        xml_annotation = ET.Element("annotation")

        # Primary nodes
        ET.SubElement(xml_annotation, "folder").text = "images"
        ET.SubElement(xml_annotation, "filename").text = str(curr_filename)
        ET.SubElement(xml_annotation, "path").text = str(save_dir)
        source = ET.SubElement(xml_annotation, "source")
        size = ET.SubElement(xml_annotation, "size")
        ET.SubElement(xml_annotation, "segmented").text = "0"

        # Source child node
        ET.SubElement(source, "database").text = "Unknown"

        # Size child nodes
        ET.SubElement(size, "width").text = str(img_width)
        ET.SubElement(size, "height").text = str(img_height)
        ET.SubElement(size, "depth").text = "1"

        return xml_annotation



    ### TIP Logic

    # Main Function that runs everything
    def mainFx(self):

        # Clear textbox
        self.statusReportBox.setPlainText('')
        self.statusReportBox.repaint()

        # Assign variables based on input value
        self.NUM_THREATS = self.numThreatsBox.value()
        self.NUM_CONTAINERS = self.numContainersBox.value()
        self.NUM_TIP_OUTPUTS = self.numImagesOutBox.value()

        self.threats_per_image = [self.threatMin.value(), self.threatMax.value()]
        self.rotation_range = [self.rotationMin.value(), self.rotationMax.value()]
        self.bg_threshold_range = [self.bgMin.value(), self.bgMax.value()]

        self.FAR_NEAR_RATIO = self.magRatio.value()  # Ratio of length of object at far end vs near end of container
        self.MIN_BBOX_SIZE = self.minBboxSize.value()  # Min bounding box size in px

        self.OBJ_CLASS = 'Untitled' if self.objClassField.text()=='' else self.objClassField.text()

        # Run everything
        self.run_TIP_process()


    # File Selection
    def selectThreatFileFx(self):
        self.threats_dir = QFileDialog.getExistingDirectory()

        # Count number of files & update slider
        if os.path.exists(self.threats_dir):
            # Count
            self.num_threat_files = len([name for name in os.listdir(self.threats_dir)
                                        if os.path.isfile(os.path.join(self.threats_dir, name))])

            if self.num_threat_files==0:
                self.selectThreatFilesInput.setText("Directory is empty! Will cause crash. Try Again.")
            else:
                # Set text
                self.selectThreatFilesInput.setText(self.threats_dir)
                self.numThreatsSlider.setMaximum(self.num_threat_files)
                self.numThreatsBox.setMaximum(self.num_threat_files)


    def selectContainerFileFx(self):
        self.container_dir = QFileDialog.getExistingDirectory()

        # Count number of files & update slider
        if os.path.exists(self.container_dir):
            # Count
            self.num_container_files = len([name for name in os.listdir(self.container_dir)
                                        if os.path.isfile(os.path.join(self.container_dir, name))])

            if self.num_container_files==0:
                self.selectContainerFilesInput.setText("Directory is empty! Will cause crash. Try Again.")
            else:
                # Set text
                self.selectContainerFilesInput.setText(self.container_dir)
                self.numContainersSlider.setMaximum(self.num_container_files)
                self.numContainersBox.setMaximum(self.num_container_files)


    def selectContainerXMLFx(self):
        self.container_xml_dir = QFileDialog.getExistingDirectory()
        self.selectContainerXMLInput.setText(self.container_xml_dir)

    def selectOutputDirFx(self):
        self.output_dir = QFileDialog.getExistingDirectory()
        self.selectOutputDirInput.setText(self.output_dir)

    # Status Report printing
    def printLog(self, textToPrint):
        """
        Status Report printing
        """
        self.statusReportBox.appendPlainText(textToPrint)
        self.statusReportBox.repaint()


    ## TIP Helper

    def run_TIP_process(self):
        # Randomly pick container images & threat images & assign to index
        (threat_imgs, container_imgs) = self.randomly_pick_files()

        if threat_imgs == None or container_imgs == None:
            self.printLog(str("Ending current run due to error"))
            return None

        # Creates output folder
        output_dir = self.create_output_folder()

        # Generate one TIP image with one or more threats
        CONTAINER_REPEATS = self.NUM_TIP_OUTPUTS // self.NUM_CONTAINERS  # Count no of times to use each container
        LAST_CONTAINER_REPEAT = self.NUM_TIP_OUTPUTS - (
                (self.NUM_CONTAINERS - 1) * CONTAINER_REPEATS)  # Number of times to use the last container

        # For loop for all containers
        count = 0
        self.printLog(str(f"\nCurrently generating {self.NUM_TIP_OUTPUTS} TIP images... Pls Wait"))
        for i, container in enumerate(container_imgs):
            repetitions = LAST_CONTAINER_REPEAT if i == (len(container_imgs) - 1) else CONTAINER_REPEATS
            for j in range(repetitions):
                self.generate_one_TIP(container, threat_imgs, output_dir, count)

                # Increment count and print progress
                count += 1
                if count % 10 == 0:
                    self.printLog(str(f"{count}/{self.NUM_TIP_OUTPUTS} TIPs generated!"))

        # Success statement
        self.printLog(str(f"\nSuccess! :)) TIP images and labels saved to {output_dir}"))

        # Opens output folder if requested
        if self.openFolderCheckbox.isChecked():
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, output_dir])

        return os.path.basename(os.path.normpath(output_dir))

    def generate_one_TIP(self, container, threat_imgs, output_dir, count):
        """
        Generates a single TIP using 1x container image and 1 or more threat images.

        Input:
        1. Container image filename
        2. List of threat image filenames
        3. output_dir


        Ouput:
        1. Completed TIP image (PIL Object) saved in output_dir/images
        2. XML label in output_dir/annotations

        Returns:
        NIL
        """
        # Open container image
        container_img = Image.open(os.path.join(self.container_dir, container))

        # Decide number of threats to place in this TIP
        num_threats_to_place = np.random.randint(low=self.threats_per_image[0], high=self.threats_per_image[1], size=1)[
            0]

        # Define image save directory
        curr_filename = f"myTIP_{count}.jpg"
        curr_filename_bbox = f"myTIP_{count}_boxed.jpg"
        save_dir = os.path.join(output_dir, "images", curr_filename)

        # Create XML file with labels
        xml_annotation = self.create_xml_backbone(curr_filename, save_dir, container_img.width, container_img.height)

        for i in range(num_threats_to_place):
            selected_threat = random.choice(threat_imgs)

            # Decide random variables to augment threat
            rotation_deg = np.random.randint(low=self.rotation_range[0], high=self.rotation_range[1], size=1)[0]
            magnification_d = np.random.uniform(low=0, high=1, size=1)[0]  # Fixed "d" in formulae
            bg_threshold = np.random.randint(low=self.bg_threshold_range[0], high=self.bg_threshold_range[1], size=1)[0]

            # Open threat image & perform augmentation
            threat_img = Image.open(os.path.join(self.threats_dir, selected_threat))
            output_threat = self.rotate_and_magnify(threat_img, rotation_deg, magnification_d)

            # Remove background
            output_threat = self.remove_bg_then_blending(output_threat, bg_threshold)

            # Crop threat image and normalise pixel values to [0:1]
            threat_array = self.trim_and_normalise(output_threat)

            # Determine coordinate for TIP
            # (0,0) is at the top left corner.
            placement_coords = self.determine_random_coords(threat_array.shape, os.path.splitext(container)[0])

            # Place threat onto image!
            container_img = self.place_one_threat(container_img, placement_coords, threat_array)

            # Update XML with new threat placed
            xml_annotation = self.update_bbox_in_XML(xml_annotation, os.path.splitext(selected_threat)[0],
                                                     placement_coords,
                                                     threat_array.shape[1], threat_array.shape[0])

        # Save TIP image output
        container_img.save(save_dir)

        # Draw TIP image with ground truth bbox
        self.draw_groundtruth(container_img, os.path.join(output_dir, "images", curr_filename_bbox), xml_annotation)

        # Make XML File pretty and Save it
        dom = minidom.parseString(ET.tostring(xml_annotation))
        xml_out = dom.toprettyxml(indent='\t')
        with open(os.path.join(output_dir, "annotations", f"myTIP_{count}.xml"), "w") as f:
            f.write(xml_out)

    #######################

    def draw_groundtruth(self, container_img, save_dir_box, xml_annotation):
        """
        Draw ground truth box in red and save
        """
        # xml_tree = ET.parse(xml_annotation)
        objectlist = xml_annotation.findall("object")
        coords = ["xmin", "ymin", "xmax", "ymax"]
        container_img = container_img.convert(mode='RGB')

        draw = ImageDraw.Draw(container_img)

        for obj in objectlist:
            bndbox = obj.find("bndbox")
            threat_coords = [int(bndbox.find(elem).text) for elem in coords]
            draw.rectangle([(threat_coords[0], threat_coords[1]), (threat_coords[2], threat_coords[3])], outline="red",
                           width=3)
            draw.text((threat_coords[0], threat_coords[1] - 10), text="TIP", fill="red")

        container_img.save(save_dir_box)

    def update_bbox_in_XML(self, xml_annotation, selected_threat, placement_coords,
                           threat_width, threat_height):
        """
        Adds bounding box info "Object Node" into XML labels file

        Inputs:
            1. xml_annotation (XML ElementTree Object)
            2. selected_threat (Name without file extension)
            3. placement_coords (Tuple in x,y format)
            4. threat_width (x)
            5. threat_height (y)

        Returns:
            1.  xml_annotation (XML ElementTree Object)
        """
        myObject = ET.SubElement(xml_annotation, "object")

        # Get threat class
        threat_class = str(self.OBJ_CLASS)

        # Object child nodes
        ET.SubElement(myObject, "name").text = str(threat_class)
        ET.SubElement(myObject, "pose").text = "Unspecified"
        ET.SubElement(myObject, "truncated").text = "0"
        ET.SubElement(myObject, "difficult").text = "0"
        bndbox = ET.SubElement(myObject, "bndbox")

        # bndbox child nodes
        ET.SubElement(bndbox, "xmin").text = str(placement_coords[0])
        ET.SubElement(bndbox, "ymin").text = str(placement_coords[1])
        ET.SubElement(bndbox, "xmax").text = str(placement_coords[0] + threat_width)
        ET.SubElement(bndbox, "ymax").text = str(placement_coords[1] + threat_height)

        return xml_annotation

    def create_xml_backbone(self, curr_filename, save_dir, img_width, img_height):
        """
        PascalVOC Format
        Creates backbone of XML label file, populating tree with everything except object bounding box labels

        Returns:
            1. xml_annotation (ElementTree Object)
        """
        # Main node
        xml_annotation = ET.Element("annotation")

        # Primary nodes
        ET.SubElement(xml_annotation, "folder").text = "images"
        ET.SubElement(xml_annotation, "filename").text = str(curr_filename)
        ET.SubElement(xml_annotation, "path").text = str(save_dir)
        source = ET.SubElement(xml_annotation, "source")
        size = ET.SubElement(xml_annotation, "size")
        ET.SubElement(xml_annotation, "segmented").text = "0"

        # Source child node
        ET.SubElement(source, "database").text = "Unknown"

        # Size child nodes
        ET.SubElement(size, "width").text = str(img_width)
        ET.SubElement(size, "height").text = str(img_height)
        ET.SubElement(size, "depth").text = "1"

        return xml_annotation

    def create_output_folder(self):
        """
        Helper function to create new directory to store TIP images & annotations

        Returns:
        1. new_dir
            - Directory to store outputs, named after time and date
        """
        new_dir_name = datetime.now().strftime("%Y_%m_%d-%H.%M.%S")

        # Directory is named after time and date
        new_dir = os.path.join(self.output_dir, f"TIP_{new_dir_name}")
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

            # Make sub-folders in each
            os.mkdir(os.path.join(new_dir, "annotations"))
            os.mkdir(os.path.join(new_dir, "images"))

        return new_dir

    def randomly_pick_files(self):
        """
        Randomly selects threats and containers and returns them as a list

        Returns:
            1. threat_list: list of threat filenames picked. No repeats.
            2. container_list: list of container filenames picked. No repeats.
        """
        # Check if user is requesting a reaosnable number of threats and containers
        threat_dir_full = os.path.join(self.threats_dir)
        container_dir_full = os.path.join(self.container_dir)
        num_threats_database = len(
            [name for name in os.listdir(threat_dir_full) if os.path.isfile(os.path.join(threat_dir_full, name))])
        num_containers_databse = len(
            [name for name in os.listdir(container_dir_full) if os.path.isfile(os.path.join(container_dir_full, name))])
        if self.NUM_THREATS > num_threats_database:
            self.printLog(str(
                f"ERROR! Number of threat images requested exceed that stored in database. Please lower NUM_THREATS (max = {num_threats_database})"))
            return None, None
        elif self.NUM_CONTAINERS > num_containers_databse:
            self.printLog(str(
                f"ERROR! Number of container images requested exceed that stored in database. Please lower NUM_CONTAINERS (max = {num_containers_databse})"))
            return None, None
        elif self.NUM_TIP_OUTPUTS < self.NUM_CONTAINERS:
            self.printLog(str(
                f"ERROR! Number of TIP outputs must exceed number of containers. Please increase NUM_TIP_OUTPUTS (min = {self.NUM_CONTAINERS})"))
            return None, None
        else:
            self.printLog(str("Selecting images for TIP..."))

        # Randomly select images
        threat_imgs = []
        container_imgs = []

        # Pick threats
        threat_count = 0
        while len(threat_imgs) < self.NUM_THREATS:
            sel = random.choice(os.listdir(threat_dir_full))
            if sel not in threat_imgs and os.path.isfile(os.path.join(threat_dir_full, sel)):
                threat_imgs.append(sel)
            threat_count += 1
            if threat_count > 1e5:
                self.printLog(
                    str("Error! Unable to pick required number of suitable threat images. Try reducing num threat required"))
                return None, None

        # Pick containers
        cont_count = 0
        while len(container_imgs) < self.NUM_CONTAINERS:
            sel = random.choice(os.listdir(container_dir_full))
            if sel not in container_imgs and os.path.isfile(
                    os.path.join(container_dir_full, sel)) and self.check_bbox_size(
                    os.path.splitext(sel)[0]):
                container_imgs.append(sel)
            cont_count += 1
            if cont_count > 1e6:
                self.printLog(str(
                    "Error! Unable to pick required number of suitable container images. Try reducing num container required"))
                return None, None

        self.printLog(str(f"\nThreat Images selected: {threat_imgs}"))
        self.printLog(str(f"\nContainer Images selected: {container_imgs}"))
        self.printLog(str(f"--------------------------------------------------------"))
        return (threat_imgs, container_imgs)

    #######################

    def rotate_and_magnify(self, img, rotation_deg=0, d=0.5):
        # Magnify
        (width, height) = (img.width, img.height)
        mag_factor = 1 + d * (self.FAR_NEAR_RATIO - 1)
        img = img.resize((int(round(width * mag_factor)), int(round(height * mag_factor))))

        # Rotate
        img = img.rotate(angle=rotation_deg, expand=1, fillcolor=255)

        return img

    def remove_bg_then_blending(self, input_img, bg_threshold=240):
        """
        Inputs:
           1. input_img (PIL Object)
               - Gun image
           2. bg_threshold (Default = 241)
               - Background removal threshold (Default = 241)

        Output:
           1. output_img (PIL Object)
        """

        output_img = input_img.convert("L")
        datas = output_img.getdata()

        newData = []

        # Remove background layers
        for item in datas:
            newData.append(255 if (item >= bg_threshold) else item)

        # Append modified image data into output
        output_img.putdata(newData)
        output_img = output_img.filter(ImageFilter.SMOOTH)

        return output_img

    def trim_and_normalise(self, im):
        """
        Automatically trims away the excess whitespace in a gun image to get a tighter bounding box.

        Input:
            1. im (PIL Object)
                - Background layer of im MUST be set to L=255 (This is handled by function Fx2.)

        Output:
            1. threat_matrix/255 (NumPy Array)
               - Matrix containing normalied [0:1] pixel values of cropped threat
        """

        # Create bg mask of only white colour
        bg = Image.new(im.mode, im.size, 255)

        # Pixel by pixel comparison of image and background. All pixels with 255 on image should have value 0 in "diff"
        diff = ImageChops.difference(im, bg)

        # adds two images, dividing the result by scale and adding the offset
        diff = ImageChops.add(diff, diff, scale=1.0, offset=0)

        # Gets non-zero bounding box of image (ie crops image)
        bbox = diff.getbbox()

        # Crop image according to bounding box
        im_cropped = im.crop(bbox)

        # Convert image to NumPy array & normalise it in preparation for TIP
        threat_matrix = np.asarray(im_cropped)
        return threat_matrix / 255

    def determine_random_coords(self, threat_dims, container_name):
        """
        Inputs:
           1. threat_dims (2x1 tuple)
               - Width and Height of threat image
           2. container_name (str)
               - Name of container (used to check bounding boxes)

        Output:
           1. Placement_coords (2x1 tuple)
               - Random coordinates to place gun at (x,y)
        """
        # Get container coords & Randomly choose container to place threat in
        container_coords_list = self.get_container_coords(container_name)
        chosen_box_idx = np.random.randint(low=len(container_coords_list), size=1)[0]
        (xmin, ymin, xmax, ymax) = container_coords_list[chosen_box_idx]

        # Generate placement coords & compute max coords and check if threat image lies outside container (not allowed)
        fail_flag = True
        while fail_flag:
            # (x,y) coords
            placement_coords = [np.random.randint(low=xmin, high=xmax, size=1)[0],
                                np.random.randint(low=ymin, high=ymax, size=1)[0]]
            max_coords = [placement_coords[0] + threat_dims[1], placement_coords[1] + threat_dims[0]]
            fail_flag = not (self.check_within_box(xmin, ymin, xmax, ymax, placement_coords[0], placement_coords[1])
                             and self.check_within_box(xmin, ymin, xmax, ymax, max_coords[0], max_coords[1]))

        return placement_coords  # (x,y)

    def check_within_box(self, xmin, ymin, xmax, ymax, x, y):
        """
        Helper function: Check if coords (x,y) within bounding box
        """
        return (x > xmin and x < xmax and y > ymin and y < ymax)

    def get_container_coords(self, container_name):
        """
        Helper function: Get coordinates of bounding box of container

        Input: (str) container_name with ".xml"

        Output: list of container bounding coords. List of list if multiple bounding boxes.
        """
        xml_tree = ET.parse(os.path.join(self.container_xml_dir, f"{container_name}.xml"))
        objectlist = xml_tree.findall("object")
        container_coords_list = []
        coords = ["xmin", "ymin", "xmax", "ymax"]

        for obj in objectlist:
            bndbox = obj.find("bndbox")
            container_coords = [int(bndbox.find(elem).text) for elem in coords]
            container_coords_list.append(container_coords)

        return container_coords_list

    def check_bbox_size(self, container_name):
        """
        Check if bbox is of sufficient size to put threat images on. If too small, returns False. Else True

        Input: container_name (str)

        Output: True or False
        """
        container_coords_list = self.get_container_coords(container_name)

        for coords in container_coords_list:
            if ((coords[2] - coords[0]) < self.MIN_BBOX_SIZE) or ((coords[3] - coords[1]) < self.MIN_BBOX_SIZE):
                return False
        return True

    def place_one_threat(self, container_img, placement_coords, threat_array):
        """
        Superimposes one threat onto the container

        Inputs:
            1. container_img (PIL Object)
            2. placement_coords (2x Tuple)

        Outputs:
            1. output_container (PIL Object)
        """
        # Invert placement_coords from (x,y) to (y,x)
        start_coordinates = (placement_coords[1], placement_coords[0])

        # Convert container image to array
        container_datas = np.asarray(container_img.convert("L"))

        # Determine size of threat image
        (height, width) = threat_array.shape
        end_coordinates = [start_coordinates[0] + height, start_coordinates[1] + width]

        # Superimpose threat onto container, replacing affected slice on container image
        container_slice = container_datas[start_coordinates[0]:end_coordinates[0], :][:,
                          start_coordinates[1]:end_coordinates[1]]

        superimposed = np.multiply(container_slice, threat_array).astype(int)

        new_container_datas = np.copy(container_datas)
        new_container_datas[start_coordinates[0]:end_coordinates[0], :][:,
        start_coordinates[1]:end_coordinates[1]] = superimposed

        # Recover finished image from array
        return Image.fromarray(new_container_datas)


    ###### MY OWN CODE END ######



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
