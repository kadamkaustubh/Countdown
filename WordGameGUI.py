from PyQt5.QtWidgets import QWidget, QPushButton


class WordGameGui(QWidget):
    def __init__(self):
        super().__init__()
        self.consonant_button = QPushButton('CONSONANT')
        self.vowel_button = QPushButton('VOWEL')
        self.wordline