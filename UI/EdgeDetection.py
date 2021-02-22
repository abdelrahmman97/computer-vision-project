# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\C Projects\My-Github\computer-vision-project\UI\EdgeDetection.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import threading

from m_edgeDetection import detectEdges

from UI.About import Ui_Dialog


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.ImageFile = ''
        self.NewImageFile = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 540)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 540))
        MainWindow.setMaximumSize(QtCore.QSize(700, 540))
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_DetectEdges = QtWidgets.QPushButton(self.centralwidget)
        self.btn_DetectEdges.setGeometry(QtCore.QRect(10, 450, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_DetectEdges.setFont(font)
        self.btn_DetectEdges.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_DetectEdges.setStyleSheet("#btn_DetectEdges{\n"
                                           "background-color: rgb(78, 78, 117);\n"
                                           "font: 12pt \"Segoe UI\";\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border:none;\n"
                                           "border-radius:15px;\n"
                                           "}\n"
                                           "QPushButton:pressed#btn_DetectEdges{\n"
                                           "background-color: #434a53;\n"
                                           "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "e:\\C Projects\\My-Github\\computer-vision-project\\UI\\../Icons/005-conversion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_DetectEdges.setIcon(icon1)
        self.btn_DetectEdges.setObjectName("btn_DetectEdges")
        self.btn_DetectEdges.setEnabled(False)
        self.btn_SaveImg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SaveImg.setEnabled(False)
        self.btn_SaveImg.setGeometry(QtCore.QRect(170, 450, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_SaveImg.setFont(font)
        self.btn_SaveImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_SaveImg.setStyleSheet("#btn_SaveImg{\n"
                                       "background-color: rgb(78, 78, 117);\n"
                                       "font: 12pt \"Segoe UI\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border:none;\n"
                                       "border-radius:15px;\n"
                                       "}\n"
                                       "QPushButton:pressed#btn_SaveImg{\n"
                                       "background-color: #434a53;\n"
                                       "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "e:\\C Projects\\My-Github\\computer-vision-project\\UI\\../Icons/003-double-check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_SaveImg.setIcon(icon2)
        self.btn_SaveImg.setObjectName("btn_SaveImg")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 40, 681, 400))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.img_OriginaImage = QtWidgets.QLabel(self.splitter)
        self.img_OriginaImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_OriginaImage.setText("")
        self.img_OriginaImage.setObjectName("img_OriginaImage")
        self.img_OriginaImage.setMinimumSize(QtCore.QSize(338, 400))
        self.img_OriginaImage.setMaximumSize(QtCore.QSize(338, 400))
        self.img_OriginaImage.setScaledContents(True)

        self.img_NewImage = QtWidgets.QLabel(self.splitter)
        self.img_NewImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_NewImage.setText("")
        self.img_NewImage.setObjectName("img_NewImage")
        self.img_NewImage.setMinimumSize(QtCore.QSize(338, 400))
        self.img_NewImage.setMaximumSize(QtCore.QSize(338, 400))
        self.img_NewImage.setScaledContents(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 5, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(170, 204, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 55, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(170, 204, 255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("border-bottom-color: rgb(85, 85, 127);\n"
                                   "background-color: rgb(85, 85, 127);\n"
                                   "border-bottom:1px solid;\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.menubar.setObjectName("menubar")
        self.menuSelect_Image = QtWidgets.QMenu(self.menubar)
        self.menuSelect_Image.setStyleSheet("#menuSelect_Image{\n"
                                            "background-color: rgb(78, 78, 117);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 8pt \"Segoe UI\";\n"
                                            "}\n"
                                            "QMenu:pressed#menuSelect_Image{\n"
                                            "background-color: rgb(100, 100, 149);\n"
                                            "}")
        self.menuSelect_Image.setTitle("File")
        self.menuSelect_Image.setObjectName("menuSelect_Image")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet("color : white")
        self.btn_OpenImage = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "e:\\C Projects\\My-Github\\computer-vision-project\\UI\\../Icons/006-copywriting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_OpenImage.setIcon(icon3)
        self.btn_OpenImage.setObjectName("btn_OpenImage")
        self.btn_About = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            "e:\\C Projects\\My-Github\\computer-vision-project\\UI\\../Icons/004-about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_About.setIcon(icon4)
        self.btn_About.setObjectName("btn_About")
        self.menuSelect_Image.addAction(self.btn_OpenImage)
        self.menuSelect_Image.addSeparator()
        self.menuSelect_Image.addAction(self.btn_About)
        self.menubar.addAction(self.menuSelect_Image.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.statusbar.showMessage('Ready')

        self.btn_About.triggered.connect(self.open_about_form)
        self.btn_OpenImage.triggered.connect(self.openFileNameDialog)
        self.btn_SaveImg.clicked.connect(self.save_Image_thread)
        self.btn_DetectEdges.clicked.connect(self.detect_Image_thread)

    def detect_Image_thread(self):
        thread = threading.Thread(target=self.detect_Image)
        thread.start()

    def save_Image_thread(self):
        thread = threading.Thread(target=self.saveFileDialog)
        thread.start()

    def open_about_form(self):
        self.statusbar.showMessage('Open About Form')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def openFileNameDialog(self):
        self.statusbar.showMessage('Open file dialog opened')
        fname = QFileDialog.getOpenFileName(self.menuSelect_Image, "Open Image", "", "(*.jpg *.png);;" "All files (*.*)")
        # fname = QFileDialog.getOpenFileName()
        if fname[0]:
            imagePath = fname[0]
            print(fname[0])
            print(imagePath)
            self.ImageFile = imagePath
            self.img_OriginaImage.setPixmap(QtGui.QPixmap(imagePath))
            self.statusbar.showMessage('Image selected')
            self.btn_DetectEdges.setEnabled(True)

    def saveFileDialog(self):
        self.statusbar.showMessage('Save file dialog opened')
        fileName = QFileDialog.getSaveFileName(self.menuSelect_Image, 'some text',"whatever.png", '*.png')
        if "." not in fileName[0]:
            fileName[0] += ".png"
            self.fileName = fileName[0]
            detectEdges.saveImg('tmp_new.png', self.fileName)
            self.statusbar.showMessage('Image saved')
        else:
            self.fileName = fileName[0]
            detectEdges.saveImg('tmp_new.png', self.fileName)
            self.statusbar.showMessage('Image saved')

    def detect_Image(self):
        print('Processing')
        self.statusbar.showMessage('Processing ...')
        # ? Edge detection Prodess
        detectEdges(self.ImageFile)
        self.img_NewImage.setPixmap(QtGui.QPixmap('tmp_new.png'))
        self.img_NewImage.setScaledContents(True)
        self.btn_SaveImg.setEnabled(True)
        self.btn_DetectEdges.setEnabled(False)
        self.statusbar.showMessage('Edges detected and new image generated')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edge Detection"))
        self.btn_DetectEdges.setText(_translate("MainWindow", "Detect edges"))
        self.btn_SaveImg.setText(_translate("MainWindow", "Save new iamge"))
        self.label_2.setText(_translate("MainWindow", "New Image"))
        self.label.setText(_translate("MainWindow", "Image"))
        self.btn_OpenImage.setText(_translate("MainWindow", "Open Image"))
        self.btn_About.setText(_translate("MainWindow", "About"))
