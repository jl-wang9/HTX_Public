# -*- coding: utf-8 -*-

# Designed with QT Designer

# Includes GUI and logic


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import os, sys, subprocess
import cv2
import xml.etree.ElementTree as ET
from datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 727)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RunProgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RunProgBtn.setGeometry(QtCore.QRect(350, 440, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.RunProgBtn.setFont(font)
        self.RunProgBtn.setObjectName("RunProgBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 121))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.statusReportBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.statusReportBox.setGeometry(QtCore.QRect(170, 510, 701, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusReportBox.setFont(font)
        self.statusReportBox.setReadOnly(True)
        self.statusReportBox.setPlainText("")
        self.statusReportBox.setOverwriteMode(True)
        self.statusReportBox.setObjectName("statusReportBox")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(30, 280, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.openFolderCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.openFolderCheckbox.setGeometry(QtCore.QRect(370, 390, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openFolderCheckbox.setFont(font)
        self.openFolderCheckbox.setIconSize(QtCore.QSize(16, 16))
        self.openFolderCheckbox.setChecked(True)
        self.openFolderCheckbox.setObjectName("openFolderCheckbox")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 180, 661, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.selectThreatFilesBtn = QtWidgets.QToolButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectThreatFilesBtn.setFont(font)
        self.selectThreatFilesBtn.setObjectName("selectThreatFilesBtn")
        self.gridLayout.addWidget(self.selectThreatFilesBtn, 0, 1, 1, 1)
        self.selectContainerFilesInput = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectContainerFilesInput.setFont(font)
        self.selectContainerFilesInput.setReadOnly(True)
        self.selectContainerFilesInput.setObjectName("selectContainerFilesInput")
        self.gridLayout.addWidget(self.selectContainerFilesInput, 1, 0, 1, 1)
        self.selectContainerFilesBtn = QtWidgets.QToolButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectContainerFilesBtn.setFont(font)
        self.selectContainerFilesBtn.setObjectName("selectContainerFilesBtn")
        self.gridLayout.addWidget(self.selectContainerFilesBtn, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 180, 291, 91))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(330, 320, 661, 32))
        self.widget2.setObjectName("widget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.selectOutputDirInput = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectOutputDirInput.setFont(font)
        self.selectOutputDirInput.setReadOnly(True)
        self.selectOutputDirInput.setObjectName("selectOutputDirInput")
        self.gridLayout_3.addWidget(self.selectOutputDirInput, 0, 0, 1, 1)
        self.selectOutputDirBtn = QtWidgets.QToolButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectOutputDirBtn.setFont(font)
        self.selectOutputDirBtn.setObjectName("selectOutputDirBtn")
        self.gridLayout_3.addWidget(self.selectOutputDirBtn, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(470, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(150, 20, 841, 121))
        self.widget3.setObjectName("widget3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ###### MY OWN CODE - EVENT LISTENERS FOR BUTTONS ######

        # File selection buttons
        self.selectThreatFilesBtn.clicked.connect(self.selectInputFileFx)
        self.selectContainerFilesBtn.clicked.connect(self.selectXMLFileFx)
        self.selectOutputDirBtn.clicked.connect(self.selectOutputDirFx)

        # Generate button
        self.RunProgBtn.clicked.connect(self.crop_from_manual_XML)

        ###### MY OWN CODE END ######


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HTX - Auto Labelled Image Cropper"))
        self.RunProgBtn.setText(_translate("MainWindow", "Generate Cropped Images!"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"HTX logo.png\" width=\"100\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Output Directory:"))
        self.label_25.setText(_translate("MainWindow", "Note: XML files must be the same name as the images."))
        self.openFolderCheckbox.setText(_translate("MainWindow", "Open Output Folder afterwards"))
        self.lineEdit.setText(_translate("MainWindow", "C:/ ..."))
        self.selectThreatFilesBtn.setText(_translate("MainWindow", "..."))
        self.selectContainerFilesInput.setText(_translate("MainWindow", "C:/ ..."))
        self.selectContainerFilesBtn.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Images to Crop (Folder):"))
        self.label_5.setText(_translate("MainWindow", "XML Annotations:"))
        self.selectOutputDirInput.setText(_translate("MainWindow", "C:/ ..."))
        self.selectOutputDirBtn.setText(_translate("MainWindow", "..."))
        self.label_21.setText(_translate("MainWindow", "(For Annotated Images)"))
        self.label_2.setText(_translate("MainWindow", "Auto Image Cropper"))
        self.label_22.setText(_translate("MainWindow", "Given any image and its associated PascalVOC format XML label, this programme crops"))
        self.label_24.setText(_translate("MainWindow", "out the objects for you, according to their Bounding Boxes.  Supports .jpg, .png, .tiff, .tif"))
        self.label_20.setText(_translate("MainWindow", "by Wang Jiale, Jul 2021"))


    ###### MY OWN CODE ######

    def selectInputFileFx(self):
        self.image_dir = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(self.image_dir)

    def selectXMLFileFx(self):
        self.xml_folder = QFileDialog.getExistingDirectory()
        self.selectContainerFilesInput.setText(self.xml_folder)

    def selectOutputDirFx(self):
        self.output_dir = QFileDialog.getExistingDirectory()
        self.selectOutputDirInput.setText(self.output_dir)

    # Status Report printing
    def printLog(self, textToPrint):
        """
        Status Report printing
        """
        self.statusReportBox.appendPlainText(textToPrint)

    # Main Function that runs everything
    def crop_from_manual_XML(self):
        """
        Given a PascalVOC XML annotation file and the asociated image, this script
        automatically crops out the objects enclosed within the bounding boxes and saves
        them as standalone images.
        """
        # Clear output box
        self.statusReportBox.setPlainText('')

        xml_folder_dir = self.xml_folder
        crop_images_output_dir = os.path.join(self.output_dir, 'cropped_images',
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
            curr_img = cv2.imread(os.path.join(self.image_dir, f'{xml_filename_noext}.png'))
            if curr_img is None:
                curr_img = cv2.imread(os.path.join(self.image_dir, f'{xml_filename_noext}.jpg'))
                if curr_img is None:
                    curr_img = cv2.imread(os.path.join(self.image_dir, f'{xml_filename_noext}.tiff'))
                    if curr_img is None:
                        curr_img = cv2.imread(os.path.join(self.image_dir, f'{xml_filename_noext}.tif'))
                        if curr_img is None:
                            self.printLog(
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
                self.printLog(f"{i + 1}/{len(xml_list)} processed!")

        self.printLog("Success! Images cropped. See 'cropped_images' folder")

        # Opens output folder if checkbox is checked
        if self.openFolderCheckbox.isChecked():
            self.open_file(crop_images_output_dir)


    def open_file(self, filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])

    ###### MY OWN CODE ######


# import graphics_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
