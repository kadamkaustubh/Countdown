import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QPushButton, QLineEdit, QLabel, QProgressBar, \
    QHBoxLayout, QComboBox, QVBoxLayout

from countdown_backend import CountDownSolver


class ProblemPage(QWidget):
    def __init__(self, mode, timer):
        super().__init__()
        self.solution_stack = []
        self.start_time = 0
        self.timer = timer
        self.mode = mode
        self.numbers = []
        self.target = 0
        self.back_button = QPushButton("Back")
        self.big_number_count = QSpinBox()
        self.big_number_count.setRange(1, 4)
        self.generate_number_box = QPushButton("Generate")
        self.reset_button = QPushButton("Reset")
        self.reset_button.setDisabled(True)
        self.number_group = QHBoxLayout()
        self.set_numbers = QPushButton("Set Numbers")
        self.set_numbers.setDisabled(True)
        self.number_line()
        self.target_window = QLineEdit("Target")
        self.set_target = QPushButton("Set Target")
        self.set_target.setDisabled(True)
        self.target_check = QLabel("Target should be between 100 and 999")
        self.timer_bar = QProgressBar()
        self.timer_bar.setRange(0, 100)
        self.time_keeper = QTimer()
        self.counter = 0
        self.time_keeper.timeout.connect(lambda: self.timer_props())

        self.setLayout(self.set_layout())

        if self.mode == 0:
            self.generate_number_box.clicked.connect(lambda: self.generate_button_mode0_action())
            self.set_numbers.clicked.connect(lambda: self.set_numbers_action())
            self.reset_button.clicked.connect(lambda: self.reset_actions())
            self.set_target.clicked.connect(lambda: self.target_button_action())
            self.back_button.clicked.connect(lambda: self.reset_actions())

    def solve(self):
        solver = CountDownSolver(self.big_number_count.value(), self.numbers, self.target)
        print('Solver started')
        start_time = time.time()
        solver.solve()
        self.solution_stack = solver.solution_stack
        print('solver done')
        end_time = time.time()
        print('solver took :', round(end_time - start_time, 3), 'secs')

    def timer_props(self):
        self.counter += 1
        value = (self.counter / 100) / self.timer * 100
        self.timer_bar.setValue(value)
        if value > 100:
            self.time_keeper.stop()
            self.solve()
            print(self.solution_stack)

    def target_button_action(self):
        try:
            if 100 <= int(self.target_window.text()) <= 999:
                self.set_target.setDisabled(True)
                self.target = int(self.target_window.text())
                print('valid target: ', self.target)

                self.time_keeper.start(1)


            else:
                self.target = 0
                print('target not in range')
        except ValueError:
            print('invalid target')

    def reset_actions(self):
        self.generate_number_box.setDisabled(False)
        self.set_numbers.setDisabled(True)
        self.set_target.setDisabled(True)
        for i in range(self.number_group.count()):
            item = self.number_group.itemAt(i).widget()
            if isinstance(item, QComboBox):
                for j in range(item.count()):
                    item.removeItem(0)

    def set_numbers_action(self):
        self.numbers = []
        for i in range(self.number_group.count()):
            item = self.number_group.itemAt(i).widget()
            if isinstance(item, QComboBox):
                self.numbers.append(int(item.currentText()))
        print(self.numbers)
        self.set_target.setDisabled(False)

    def generate_button_mode0_action(self):
        big = self.big_number_count.value()
        box = 0
        for i in range(self.number_group.count()):
            item = self.number_group.itemAt(i).widget()
            if isinstance(item, QComboBox):
                if box < big:
                    item.addItems(str(25 * j) for j in [1, 2, 3, 4])
                elif big <= box < 6:
                    item.addItems(str(j) for j in range(1, 11))
                box += 1
        self.generate_number_box.setDisabled(True)
        self.set_numbers.setDisabled(False)
        self.reset_button.setDisabled(False)

    def set_layout(self):
        back_line = QHBoxLayout()
        back_line.addStretch(1)
        back_line.addWidget(self.back_button)
        back_line.addStretch(1)

        big_number_line = QHBoxLayout()
        big_number_line.addWidget(QLabel("Big Number Count : "))
        big_number_line.addStretch(1)
        big_number_line.addWidget(self.big_number_count)
        big_number_line.addStretch(1)
        big_number_line.addWidget(self.generate_number_box)
        big_number_line.addStretch(1)
        big_number_line.addWidget(self.reset_button)

        target_line = QHBoxLayout()
        target_line.addWidget(self.target_window)
        target_line.addStretch(1)
        target_line.addWidget(self.set_target)
        target_line.addStretch(1)
        target_line.addWidget(self.target_check)

        main_layout = QVBoxLayout()
        main_layout.addLayout(back_line)
        main_layout.addStretch(1)
        main_layout.addLayout(big_number_line)
        main_layout.addStretch(1)
        main_layout.addLayout(self.number_group)
        main_layout.addStretch(1)
        main_layout.addLayout(target_line)
        main_layout.addStretch(1)
        main_layout.addWidget(self.timer_bar)
        main_layout.addStretch(1)
        return main_layout

    def number_line(self):
        for i in range(6):
            if self.mode == 1:
                self.number_group.addWidget(QLabel(" "))
                self.number_group.addStretch(1)
            elif self.mode == 0:
                self.number_group.addWidget(QComboBox())
                self.number_group.addStretch(1)
        self.number_group.addWidget(self.set_numbers)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = ProblemPage(0, 5)
    mw.show()
    sys.exit(app.exec_())
