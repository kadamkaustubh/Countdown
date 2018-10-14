import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QLabel, QApplication

from MenuClass import MainMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CountDown')
        self.Stack = QStackedWidget()
        self.setCentralWidget(self.Stack)
        self.setWindowIcon(QIcon('CD_logo.png'))
        self.Stack.addWidget(QLabel('My Central Window'))
        self.main_menu = MainMenu()
        self.Stack.addWidget(self.main_menu)
        self.Stack.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
