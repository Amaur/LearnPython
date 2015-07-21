#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.
"""
import sys
from PyQt5.QtWidgets import  (QApplication, QWidget, QVBoxLayout, QLCDNumber,QSlider,QMainWindow,QPushButton)
from  PyQt5.QtCore import Qt,QObject,pyqtSignal


"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox= QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Signal & Slot")

        self.show()

"""
"""
class Example(QWidget):
#reimplementing event handler
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Event handler")

        self.show()

    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Escape:
            self.close()
"""
"""
class Example(QMainWindow):
#determining an event sender
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton("Button 1",self)
        btn1.move(30,50)

        btn2 = QPushButton("Button 2",self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()



        self.setGeometry(300,300,290,150)
        self.setWindowTitle("Event Sender")

        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+ " was pressed")

"""

class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
#emiting events
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)



        self.statusBar()



        self.setGeometry(300,300,290,150)
        self.setWindowTitle("Emit sinal")

        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
