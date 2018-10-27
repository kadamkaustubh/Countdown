import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication

from MenuClass import MainMenu
from problemClass import ProblemPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CountDown')
        self.Stack = QStackedWidget()
        self.setCentralWidget(self.Stack)
        self.setWindowIcon(QIcon('CD_logo.png'))
        self.main_menu = MainMenu()
        self.Stack.addWidget(self.main_menu)
        self.problem_page = ProblemPage(0,30)
        self.Stack.addWidget(self.problem_page)
        self.Stack.setCurrentIndex(0)
        self.main_menu.next_page.clicked.connect(lambda: self.Stack.setCurrentIndex(1))
        self.problem_page.back_button.clicked.connect(lambda: self.Stack.setCurrentIndex(0))
        self.main_menu.next_page.clicked.connect(lambda: print(self.main_menu.selected_modes))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
