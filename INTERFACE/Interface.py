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
import os


# This class handles the logo object and functionality
class ImageLabel(QLabel):
    def __init__(self, image, parent=None):
        super(ImageLabel, self).__init__(parent)
        self.setPixmap(image)

    #This function handles what happens when the image logo clicked
    def mousePressEvent(self, event):
        #print 'I was pressed'
        print ('I was pressed')

        #Opens the HELP/DOCUMENTATION file
        os.startfile("C:\Users\Kem\Documents\GitHub\SEproject\documentation.docx")


# ------------   END OF ImageLabel CLASS    ---------------------------------

# This class handles the main Window of the program.
# Window contains buttons, tooltips, logo, and each
# button's functionality
class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__() #call init from the base class
# MAIN WINDOW TEMPLATE:
        # Creates a window with the following specifications:
        # Geometry/size:  600x600 PIXELS
        # Title:          PIXELS
        # Icon:           sets image icon contained in image folder
        self.setGeometry(0,0,150,300)
        self.setWindowTitle("P I X E L S")
        self.setWindowIcon(QtGui.QIcon('icon'))
        self.home()

    def home(self):

        # Create a Qt label object with image file
        img_label = ImageLabel(QPixmap('logo.png'))
        img_label.setToolTip("<b> Click Here For HELP!</b>")
        DescripLabel = QtGui.QLabel("Welcome to PIXELS If you need any help click on the image logo")

        # Create Qt box objects
        # box objects allows you to set different layouts by
        # saving objects in boxes and setting boxes in different
        # positions within the window
        vbox = QHBoxLayout()
        vbox.addWidget(img_label)
        #vbox.addWidget(DescripLabel)

        vbox2 = QVBoxLayout()
        vbox.addLayout(vbox2)

        main_frame = QWidget()
        main_frame.setLayout(vbox)
        self.setCentralWidget(main_frame)

    #Call this function to center the window on user's screen
        self.center()

    #Status Bar
        self.statusBar().showMessage('Ready')
        self.statusBar().setToolTip("Program status")

    #TOOLTIP
        #This is a tooltip
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('Thanks for using <b>PIXELS</b>!')

    #ADD IMAGES BUTTON
        # Creates a button with the following specifications:
        # Name:             AddImages
        # Position:         150, 200 (px)
        # Functinality:     when clicked opens Windows Explorer window
        addimgButton = QtGui.QPushButton("Add Images", self)
        addimgButton.resize(addimgButton.sizeHint())
        addimgButton.move(150, 200)
        addimgButton.setToolTip('Click to add your images')
        addimgButton.clicked.connect(self.selectFile)
        vbox2.addWidget(addimgButton)
        #addimgButton.resize(300,300)

    #EXIT BUTTON
        # Creates a button with the following specifications:
        # Name:             Exit
        # Position:         150, 250 (px)
        # Functinality:     when clicked calls Qt exit function
        #                   to close the window
        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setToolTip('Click to <b>EXIT</b> PIXELS')
        exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        exitButton.resize(exitButton.sizeHint())
        exitButton.move(150,250)
        vbox2.addWidget(exitButton) #add button to vbox2 layout

    #FRAME RATE
        # Creates a button with the following specifications:
        # Name:             Frame rate
        # Position:         150, 300 (px)
        # Functinality:     when clicked calls Qt dialog box function
        #                   which ask the user to entera value. Stores
        #                   that value in frateEdit box object
        self.frameRate = QtGui.QPushButton('Frame rate', self)
        self.frameRate.move(150,300)
        self.frameRate.clicked.connect(self.showDialog)     #dialogue box popup
        self.frameRate.setToolTip('Click to enter Frame rate')
        vbox2.addWidget(self.frameRate)               #tooltip

        #Creates a Qt box object to save user entered value
        self.frateEdit = QtGui.QLineEdit(self)
        self.frateEdit.move(150, 330)
        self.frateEdit.setToolTip('Enter frame rate')
        vbox2.addWidget(self.frateEdit)

        #paint the Window created
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
    #Have the user enter the framerate of the pictures to be processed
    def showDialog(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Input Framerate',
            'Enter framerate:')

        if ok:
            self.frateEdit.setText(str(text))

#OPEN File
    #Opensfile explorer
    def selectFile(self):
        #lineEdit.setText(QFileDialog.getOpenFileName())
        openfile = QtGui.QFileDialog.getOpenFileName(self, 'Open File') # Filename line
        f = open(openfile, 'r') # New line
        data = f.read() # New line

        ########INSERT Code to read images and process data OR call to a function#######
        ### 1. create new window pop-up with progress bar
        ### 2. save data to folder
        ### 3. message to user

    def slotFile(self):
        filename=QFileDialog.getOpenFileName("", "*.py", self, "FileDialog")

    def changebackground(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select background image', 'C:/Users/Kem/Documents/GitHub/SoftwareEngineering/logo')
        print (fname)
        self.setStyleSheet("background-image: url(" + fname + "); background-repeat: no-repeat; background-position: center;")

#RUN THE PROGRAM
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
