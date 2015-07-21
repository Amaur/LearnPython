#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a statusbar.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,QAction, qApp)
from PyQt5.QtGui import QIcon

"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('StatusBar')
        self.show()
"""



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        exitAction = QAction('&exit',self)
        exitAction.setShortcut('ctrl +Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)


        self.statusBar()#.showMessage("Ready")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&file")
        myMenu = menubar.addMenu("&Teste")
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        self.setGeometry(300,300,250,250)
        self.setWindowTitle('Toolbar & menubar')
        self.show()



if __name__ == '__main__':

    app= QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

