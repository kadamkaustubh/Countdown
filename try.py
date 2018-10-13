import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QDesktopWidget, \
    QWidget, QLabel, QPushButton, QDialog, QVBoxLayout, QStackedWidget, QHBoxLayout, QRadioButton, QCheckBox, QLineEdit, \
    QFormLayout
from PyQt5.QtGui import QIcon, QPixmap


class HomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.stack1 = QWidget()
        #self.stack2 = QWidget()
        #self.stack3 = QWidget()

        self.menu_page()
        #self.stack2UI()
        #self.stack3UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        #self.Stack.addWidget(self.stack2)
        #self.Stack.addWidget(self.stack3)
        #self.Stack.setCurrentIndex(0)
        #self.init_ui()
        #self.setGeometry(350, 50, 100, 10)
        #self.resize(100,100)

    def menu_page(self):
        top_layout = QVBoxLayout()
        tv_label = QLabel("VS TV")
        cpu_label = QLabel('VS CPU')
        top_layout.addWidget(tv_label)
        top_layout.addWidget(cpu_label)
        self.stack1.setLayout(top_layout)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex :"), sex)
        layout.addRow("Date of Birth", QLineEdit())

        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack3.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomeWindow()
    ex.show()
    sys.exit(app.exec_())
