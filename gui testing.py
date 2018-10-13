import sys

from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QApplication, QVBoxLayout, QComboBox, QStackedWidget


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Python and Ruby texts
        python_text = ('Python is a programming language '
                       'that lets you work more quickly '
                       'and integrate your systems more effectively.\n\n'
                       'visit https://www.python.org/')
        ruby_text = ('A dynamic, open source programming language with a focus on simplicity and productivity. '
                     'It has an elegant syntax that is natural to read and easy to write.\n\n'
                     'visit https://www.ruby-lang.org/')

        # Python text edit
        python_text_edit = QPlainTextEdit(python_text)
        python_text_edit.setReadOnly(True)

        # Ruby text edit
        ruby_text_edit = QPlainTextEdit(ruby_text)
        ruby_text_edit.setReadOnly(True)

        # stacked widget
        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(python_text_edit)
        stacked_widget.addWidget(ruby_text_edit)

        # combobox
        combobox = QComboBox()
        combobox.addItems(['Python', 'Ruby'])
        # activated signal - setCurrentIndex slot
        combobox.activated.connect(stacked_widget.setCurrentIndex)

        # vertical box layout
        vlayout = QVBoxLayout()
        vlayout.addWidget(combobox)
        vlayout.addWidget(stacked_widget)
        self.setLayout(vlayout)


application = QApplication(sys.argv)

# window
window = Window()
window.setWindowTitle('Stacked Widget')
window.resize(280, 260)
window.show()

sys.exit(application.exec_())