import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QPushButton, QLineEdit, QLabel, QProgressBar, \
    QHBoxLayout, QComboBox, QVBoxLayout


class ProblemPage(QWidget):
    def __init__(self,mode,timer):
        super().__init__()
        self.timer = timer
        self.mode = mode
        self.back_button = QPushButton("Back")
        self.big_number_count = QSpinBox()
        self.big_number_count.setRange(1,4)
        self.generate_number_box = QPushButton("Generate")
        self.reset_button = QPushButton("Reset")
        self.spin_box_group = QHBoxLayout()
        self.set_numbers = QPushButton("Set Numbers")
        self.number_line()
        self.target_window = QLineEdit("Target")
        self.set_target = QPushButton("Set Target")
        self.target_check = QLabel("Checking Target")
        self.timer_bar = QProgressBar()
        self.target_window.text
        self.setLayout(self.set_layout())

    def set_layout(self):
        back_line = QHBoxLayout()
        back_line.addWidget(self.back_button)

        big_number_line = QHBoxLayout()
        big_number_line.addWidget(QLabel("Big Number Count : "))
        big_number_line.addWidget(self.big_number_count)
        big_number_line.addWidget(self.generate_number_box)
        big_number_line.addWidget(self.reset_button)

        target_line = QHBoxLayout()
        target_line.addWidget(self.target_window)
        target_line.addWidget(self.set_target)
        target_line.addWidget(self.target_check)

        main_layout = QVBoxLayout()
        main_layout.addLayout(back_line)
        main_layout.addLayout(big_number_line)
        main_layout.addLayout(self.spin_box_group)
        main_layout.addLayout(target_line)
        main_layout.addWidget(self.timer_bar)
        return main_layout


    def number_line(self):
        for i in range(6):
            if self.mode == 0:
                self.spin_box_group.addWidget(QLabel(""))
            elif self.mode == 1:
                self.spin_box_group.addWidget(QComboBox())
        self.spin_box_group.addWidget(self.set_numbers)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = ProblemPage(2,30)
    mw.show()
    sys.exit(app.exec_())