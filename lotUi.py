import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QTabBar,QTabWidget,QHBoxLayout
from PyQt5.QtGui import QTabletEvent


class LotUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        mega = menubar.addMenu("&Megasena")
        quina = menubar.addMenu("&Quina")

        tabs = QTabWidget(self)
        tab_bar =QTabBar(tabs)

        tab_1 = tab_bar.addTab("Main")
        tab_2 = tab_bar.addTab("Description")

        vbox = QHBoxLayout()
        #vbox.addWidget(menu_bar)
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.statusBar().showMessage("Working fine")
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Lotericas')
        self.show()



if __name__=="__main__":
    app = QApplication(sys.argv)
    ex= LotUi()
    sys.exit(app.exec_())
