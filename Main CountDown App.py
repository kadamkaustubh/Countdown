import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget, \
    QHBoxLayout, QRadioButton, QButtonGroup, QFrame, QSpinBox, QComboBox


def title_font():
    font = QFont()
    font.setPointSize(12)
    font.setStyleHint(QFont.Helvetica)
    return font


class HomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.fix_combo = QPushButton('Set Target')
        self.gen_reset = QPushButton('Reset')
        self.number_tray_layout = QHBoxLayout()
        self.number_show = QLabel('')
        self.big_number = QSpinBox()
        self.gen_big_numbers = QPushButton('Generate')
        self.set_numbers()
        # menu page buttons
        self.time_input_box = QSpinBox()
        self.radio_variable = QRadioButton('Variable')
        self.radio_relax = QRadioButton('Relaxed')
        self.radio_std = QRadioButton('30 Secs')
        self.radio_sure = QRadioButton('Sure Answer')
        self.radio_random = QRadioButton('Random')
        self.radio_cats = QRadioButton('Cats')

        # Constructors

        self.stack_menu = QWidget()
        self.input_menu = QWidget()
        self.menu_page()
        self.input_page()

        # Stack Appending
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack_menu)
        self.Stack.addWidget(self.input_menu)
        self.setCentralWidget(self.Stack)
        self.Stack.setCurrentIndex(1)

        # Formatting
        self.resize(300*1.6,300)

    def menu_page(self):
        left_col = QVBoxLayout()
        tv_label = QLabel("VS TV")
        tv_label.setFont(title_font())
        cpu_label = QLabel('VS CPU')
        cpu_label.setFont(title_font())
        left_col.addWidget(tv_label)
        left_col.addWidget(self.radio_cats)
        left_col.addWidget(cpu_label)
        left_col.addWidget(self.radio_random)
        left_col.addWidget(self.radio_sure)

        mode_picker = QButtonGroup(self)
        mode_picker.addButton(self.radio_cats)
        mode_picker.addButton(self.radio_random)
        mode_picker.addButton(self.radio_sure)

        right_col = QVBoxLayout()
        time_label = QLabel("Time")
        time_label.setFont(title_font())
        self.time_input_box.setRange(30, 1000)
        var_lay = QHBoxLayout()
        var_lay.addWidget(self.radio_variable)
        var_lay.addWidget(self.time_input_box)
        var_lay.addWidget(QLabel('Secs'))

        right_col.addWidget(time_label)
        right_col.addWidget(self.radio_std)
        right_col.addWidget(self.radio_relax)
        right_col.addLayout(var_lay)

        time_picker = QButtonGroup(self)
        time_picker.addButton(self.radio_std)
        time_picker.addButton(self.radio_relax)
        time_picker.addButton(self.radio_variable)

        top_box = QHBoxLayout()
        top_box.addLayout(left_col)
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Raised)
        top_box.addWidget(line)
        top_box.addLayout(right_col)

        central_layout = QVBoxLayout()
        run_menu = QPushButton('Start')
        central_layout.addLayout(top_box)
        central_layout.addWidget(run_menu)

        self.radio_std.setChecked(True)
        self.radio_sure.setChecked(True)
        self.stack_menu.setLayout(central_layout)

    def input_page(self):
        big_number_label = QLabel("How Many Big Ones?")
        self.big_number.setRange(1, 4)
        first_line = QHBoxLayout()
        first_line.addWidget(big_number_label)
        first_line.addWidget(self.big_number)
        first_line.addWidget(self.gen_big_numbers)
        self.gen_reset.setDisabled(True)
        first_line.addWidget(self.gen_reset)

        second_line = QHBoxLayout()
        self.number_show.hide()
        self.gen_big_numbers.clicked.connect(lambda: self.set_numbers())
        self.gen_big_numbers.clicked.connect(lambda: self.number_tray())
        self.gen_big_numbers.clicked.connect(lambda: self.gen_big_numbers.setDisabled(True))
        self.gen_big_numbers.clicked.connect(lambda: self.gen_reset.setDisabled(False))
        self.gen_reset.clicked.connect(lambda: self.resetter())
        self.gen_reset.clicked.connect(lambda: self.gen_reset.setDisabled(True))
        self.fix_combo.clicked.connect(lambda: self.extract_numbers())

        second_line.addWidget(self.number_show)
        second_line.addWidget(QLabel(''))
        sec_layout = QVBoxLayout()
        sec_layout.addLayout(first_line)
        sec_layout.addLayout(second_line)
        sec_layout.addLayout(self.number_tray_layout)
        self.input_menu.setLayout(sec_layout)

    def set_numbers(self):
        print_string = 'Coming up, %d big and %d little ones, and the numbers are:' \
                       % (self.big_number.value(), 6 - self.big_number.value())
        self.number_show.show()
        return self.number_show.setText(print_string)

    def number_tray(self):
        big = self.big_number.value()
        small = 6 - big
        big_numbers = [str(25*(i+1)) for i in range(4)]
        small_numbers = [str(i+1) for i in range(10)]
        for i in range(big):
            big_combo = QComboBox()
            big_combo.addItems(big_numbers)
            self.number_tray_layout.addWidget(big_combo)
        for i in range(small):
            small_combo = QComboBox()
            small_combo.addItems(small_numbers)
            self.number_tray_layout.addWidget(small_combo)
        self.number_tray_layout.addWidget(self.fix_combo)
        lst = []

    def extract_numbers(self):
        for i in range(self.number_tray_layout.count()):
            item = self.number_tray_layout.itemAt(i).widget()
            if isinstance(item, QComboBox):
                print(item.currentText())

    def resetter(self):
        self.gen_big_numbers.setDisabled(False)
        for i in range(self.number_tray_layout.count()):
            item = self.number_tray_layout.itemAt(i).widget()
            item.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomeWindow()
    ex.show()
    sys.exit(app.exec_())