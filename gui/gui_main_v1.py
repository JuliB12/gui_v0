#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from gui_v1 import Ui_MainWindow

def setupUi (self, Mainwindow):
       
        #self.btn_config = QtWidgets.QPushButton(self.frameizq)
        self.btn_config.clicked.connect(self.printHello)

def printHello(self): # 1) Creamos el método printHello
        print("Hello world desde el boton push")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
