from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as QtGui


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_widget = LoginWidget(self)
        self.central_widget.addWidget(self.login_widget)

        self.logged_in_widget = LoggedWidget(self)
        self.central_widget.addWidget(self.logged_in_widget)

        self.central_widget.setCurrentIndex(0)
        self.login_widget.button.clicked.connect(lambda: self.central_widget.setCurrentIndex(1))
        self.logged_in_widget.re_button.clicked.connect(lambda: self.central_widget.setCurrentIndex(0))


class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)


class LoggedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel('logged in!')
        self.re_button = QtGui.QPushButton('Re-Login')
        layout.addWidget(self.label)
        layout.addWidget(self.re_button)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
