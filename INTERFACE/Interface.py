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
        self.setGeometry(400,100,500,500)
        self.setWindowTitle("PIXELS")
        self.setWindowIcon(QtGui.QIcon('icon'))


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

    def home(self):
        #Call the function to center the window
        self.center()

        #This is a tooltip
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('Thanks for using <b>P I X E L S</b>!')


        button = QtGui.QPushButton("Exit", self)
        button.setToolTip('click to <b>EXIT</b> pixels')
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.resize(button.sizeHint())
        button.move(150,250)
        self.show()

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

    #Centers the window on the screen
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def run():
    app= QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
