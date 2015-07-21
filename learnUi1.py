import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

"""

if __name__ == "__main__":
    app= QApplication(sys.argv)

    w= QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle("Simple window")
    w.show()

    sys.exit(app.exec_())


class Example(QWidget):
    #An application icon
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))
        self.show()



class Example(QWidget):
    #Showing a tooltip
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("This is a <b>Qwidget</b> widget")

        btn = QPushButton('Button',self)
        btn.setToolTip("This is a <b>QPushButton</> widget")
        btn.resize(btn.sizeHint())
        btn.move(200,150)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))


        self.show()


class Example(QWidget):
    #Closing a window basic usage of signal and slot
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):



        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200,150)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))


        self.show()
"""

class Example(QWidget):
    #Closing a window basic usage of signal and slot
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Message Box")
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,"Message","Are you sure to quit", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())