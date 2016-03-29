# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 16:10:15 2016

@author: Kem
"""

#INTERFACE
#---------

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ImageLabel(QLabel):
    def __init__(self, image, parent=None):
        super(ImageLabel, self).__init__(parent)
        self.setPixmap(image)

    def mousePressEvent(self, event):
        print 'I was pressed'

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__() #call init fro the base class
        self.home()

    def home(self):
        #self.resize(250, 150) optional resize method
        self.setGeometry(0,0,600,600)
        self.setWindowTitle("P I X E L S")
        self.setWindowIcon(QtGui.QIcon('icon'))

        #name_label = QLabel("Here's a clickable image:")
        img_label = ImageLabel(QPixmap('logo.png'))

        vbox = QHBoxLayout()
        #vbox.addWidget(name_label)
        vbox.addWidget(img_label)
        #vbox.addStretch(1)

        vbox2 = QVBoxLayout()
        vbox.addLayout(vbox2)

        main_frame = QWidget()
        main_frame.setLayout(vbox)
        self.setCentralWidget(main_frame)

        #self.setStyleSheet("QMainWindow{ background-image: url(logo2) }")
        #self.setStyleSheet("QMainWindow{ background-color: 'gray10' }")

    #Call this function to center the window on user's screen
        self.center()

    #Status Bar
        self.statusBar().showMessage('Ready')

    #TOOLTIP
        #This is a tooltip
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('Thanks for using <b>PIXELS</b>!')

    #ADD IMAGES BUTTON
        addimgButton = QtGui.QPushButton("Add Images", self)
        addimgButton.resize(addimgButton.sizeHint())
        addimgButton.move(150, 200)
        #grid.addWidget(addimgButton, 1,0)
        addimgButton.setToolTip('Click to add your images')
        addimgButton.clicked.connect(self.selectFile)
        vbox2.addWidget(addimgButton)
        addimgButton.resize(300,300)

    #EXIT BUTTON
        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setToolTip('Click to <b>EXIT</b> PIXELS')
        exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        exitButton.resize(exitButton.sizeHint())
        #grid.addWidget(exitButton, 0,1)
        exitButton.move(150,250)
        vbox2.addWidget(exitButton)

    #FRAME RATE
        self.frameRate = QtGui.QPushButton('Frame rate', self)
        self.frameRate.move(150,300)
        self.frameRate.clicked.connect(self.showDialog)     #dialogue box popup
        self.frameRate.setToolTip('Frame rate')
        vbox2.addWidget(self.frameRate)               #tooltip

        self.frateEdit = QtGui.QLineEdit(self)
        self.frateEdit.move(150, 330)
        self.frateEdit.setToolTip('Enter frame rate')
        vbox2.addWidget(self.frateEdit)


        self.show()
# ------------   END OF Window CLASS    ---------------------------------

#MESSAGE BOX
    #This function displays a message box when the user
    #wants to quit the application
    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#CENTER WINDOW
    #Centers the window on the screen
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#FRAMERATE DIALOG BOX POPUP
    #Has the user enter the framerate of the pictures to be processed
    def showDialog(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Input Framerate',
            'Enter framerate:')

        if ok:
            self.frateEdit.setText(str(text))

#OPEN File
    #Opensfile explorer
    def selectFile(self):
        #lineEdit.setText(QFileDialog.getOpenFileName())
        openfile = QtGui.QFileDialog.getOpenFileName(self) # Filename line
        f = open(openfile, 'r') # New line
        data = f.read() # New line

    def slotFile(self):
        filename=QFileDialog.getOpenFileName("", "*.py", self, "FileDialog")

    def changebackground(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select background image', 'C:/Users/Kem/Documents/GitHub/SoftwareEngineering')
        print fname
        self.results.setStyleSheet("background-image: url(" + fname + "); background-repeat: no-repeat; background-position: center;")

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
