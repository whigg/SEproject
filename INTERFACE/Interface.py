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
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PIXELS")
        self.setWindowIcon(QtGui.QIcon('Image'))
        self.home()

    def home(self):
        button = QtGui.QPushButton("Browse", self)
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()


def run():
    app= QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
