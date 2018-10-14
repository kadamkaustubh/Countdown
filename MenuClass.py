import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QRadioButton, QSpinBox, QPushButton, QButtonGroup, QVBoxLayout, QLabel, \
    QHBoxLayout, QApplication


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()

        # define inputs
        # modes
        self.user_def = QRadioButton('User Defined')
        self.random_set = QRadioButton('Random')
        self.sure_set = QRadioButton('Random with Sure Answer')


        # time modes
        self.std_time = QRadioButton('30 Secs')
        self.var_time = QRadioButton('Variable')
        self.relaxed_time = QRadioButton('Relaxed')
        self.var_time_edit = QSpinBox()
        self.var_time_edit.setRange(30,3000)


        # Next Connection
        self.next_page = QPushButton('Next')

        layout = self.def_layout()
        groups = self.group_buttons()
        self.user_def.setChecked(True)
        self.std_time.setChecked(True)

        self.setLayout(layout)

    def def_layout(self):
        left_col = QVBoxLayout()
        left_col.addWidget(self.user_def)
        left_col.addWidget(self.random_set)
        left_col.addWidget(self.sure_set)

        var_time_row = QHBoxLayout()
        var_time_row.addWidget(self.var_time)
        var_time_row.addWidget(self.var_time_edit)
        var_time_row.addWidget(QLabel('Secs'))

        right_col = QVBoxLayout()
        right_col.addWidget(self.std_time)
        right_col.addLayout(var_time_row)
        right_col.addWidget(self.relaxed_time)

        top_row = QLabel('Let\'s Play CountDown!!!')
        top_row.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        font.setStyleHint(QFont.Helvetica)
        top_row.setFont(font)

        mid_row = QHBoxLayout()
        mid_row.addLayout(left_col)
        mid_row.addLayout(right_col)

        main_layout = QVBoxLayout()
        main_layout.addWidget(top_row)
        main_layout.addLayout(mid_row)
        main_layout.addWidget(self.next_page)
        return main_layout

    def group_buttons(self):
        mode_picker = QButtonGroup(self)
        mode_picker.addButton(self.user_def)
        mode_picker.addButton(self.random_set)
        mode_picker.addButton(self.sure_set)

        time_picker = QButtonGroup(self)
        time_picker.addButton(self.std_time)
        time_picker.addButton(self.var_time)
        time_picker.addButton(self.relaxed_time)
        return mode_picker, time_picker


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainMenu()
    mw.show()
    sys.exit(app.exec_())
