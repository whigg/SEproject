# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 16:10:15 2016

@author: Kem
"""

#INTERFACE
#---------

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        #Template for home menu
        super(Window,self).__init__()
        #self.resize(250, 150) optional resize method
        self.setGeometry(600,600,600,600)
        self.setWindowTitle("P I X E L S")
        self.setWindowIcon(QtGui.QIcon('icon'))

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowOpacity(.9)
        #text_widget = text(self)
        #self.setCentralWidget(text_widget)
        #self.setStyleSheet("QMainWindow { background: 'grey13'}");
        #self.setStyleSheet("QMainWindow { padding: 20px}");

        self.setStyleSheet("QMainWindow{ background-image: url(logo) }")

        # extractAction = QtGui.QAction("Get to the choppah", self)
        # extractAction.setShortcut("Ctrl+Q")
        # extractAction.setStatusTip('Leave the app')
        # extractAction.triggered.connect(QtCore.QCoreApplication.instance().quit)
        #
        # self.stausBar()
        #
        # mainMenu = self.menuBar()
        # fileMenu = mainMenu.addMenu('&File')
        # fileMenu.addAction(extractAction)

        self.home()
        #self.changebackground()

    def home(self):
    #Call this function to center the window on user's screen
        self.center()

    #Status Bar
        self.statusBar().showMessage('Ready')

    #TOOLTIP
        #This is a tooltip
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('Thanks for using <b>PIXELS</b>!')

        logoButton = QtGui.QPushButton(self)
        logoButton.setStyleSheet("background-color: red")
        logoButton.move(150, 150)

    #ADD IMAGES BUTTON
        addimgButton = QtGui.QPushButton("Add Images", self)
        #addimgButton.resize(addimgButton.sizeHint)
        addimgButton.move(150, 200)
        addimgButton.setToolTip('Click to add your images')
        addimgButton.clicked.connect(self.selectFile)

        #oD=openDirectoryDialog.getExistingDirectory(self,"open","C:/")

    #EXIT BUTTON
        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setToolTip('Click to <b>EXIT</b> PIXELS')
        exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        exitButton.resize(exitButton.sizeHint())
        exitButton.move(150,250)

    #FRAME RATE
        self.frameRate = QtGui.QPushButton('Frame rate', self)
        self.frameRate.move(150,300)
        self.frameRate.clicked.connect(self.showDialog)     #dialogue box popup
        self.frameRate.setToolTip('Frame rate')                  #tooltip

        self.frateEdit = QtGui.QLineEdit(self)
        self.frateEdit.move(150, 330)
        self.frateEdit.setToolTip('Enter frame rate')

    #LAYOUT
        # grid = QtGui.QGridLayout()
        # self.setLayout(grid)
        # grid.addWidget(logoButton, 0,0)
        # grid.addWidget(addimgButton, 0,1)
        # grid.addWidget(exitButton, 0,2)
        # # grid.addWidget(frameRate, 1,1)

        self.show()
# ------------   END OF Window CLASS    ---------------------------------

#MESSAGE BOX
    #This function displays a message box when the user
    #wants to quit the application
    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
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
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select background image', 'C:/Users/Kem/Documents/GitHub/SoftwareEngineering/conversion')
        print fname
        self.results.setStyleSheet("background-image: url(" + fname + "); background-repeat: no-repeat; background-position: center;")

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
