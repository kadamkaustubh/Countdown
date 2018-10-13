import sys

from PyQt5 import QtWidgets


class IntroductionPage(QtWidgets.QWizardPage):
    def __init__(self):
        super(IntroductionPage, self).__init__()

        self.setTitle("Introduction")
        self.label = QtWidgets.QLabel("set this up")
        self.label.setWordWrap(True)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def nextId(self):
        return Wizard.class1

    def backId(self):
        return Wizard.class2


class ClassesPage1(QtWidgets.QWizardPage):
    def __init__(self):
        super(ClassesPage1, self).__init__()
        self.setTitle("Choices")
        self.setSubTitle("Choose 1")

        self.radButton1 = QtWidgets.QRadioButton('1A')
        self.radButton2 = QtWidgets.QRadioButton('1B')
        self.radButton3 = QtWidgets.QRadioButton('1C')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.radButton1)
        self.layout.addWidget(self.radButton2)
        self.layout.addWidget(self.radButton3)
        self.class_selected1 = QtWidgets.QLineEdit()
        self.setLayout(self.layout)

    def nextId(self):
        if self.radButton2.isChecked():

            return Wizard.class2
        elif self.radButton3.isChecked():

            return Wizard.class2
        else:
            return Wizard.conclusion


class ClassesPage2(QtWidgets.QWizardPage):
    def __init__(self):
        super(ClassesPage2, self).__init__()
        # self.page = QWizardPage()
        self.setTitle("Classes for grade 2")
        self.setSubTitle("Please select a Class")

        self.radButton1 = QtWidgets.QRadioButton('2A')
        self.radButton2 = QtWidgets.QRadioButton('2B')
        self.radButton3 = QtWidgets.QRadioButton('2C')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.radButton1)
        self.layout.addWidget(self.radButton2)
        self.layout.addWidget(self.radButton3)
        self.class_selected2 = QtWidgets.QLineEdit()

        self.setLayout(self.layout)

    def nextId(self):
        return Wizard.conclusion


class ClassesPage3(QtWidgets.QWizardPage):
    def __init__(self):
        super(ClassesPage3, self).__init__()
        self.setTitle("Classes for grade 3")
        self.setSubTitle("Please select a Class")

        self.radButton1 = QtWidgets.QRadioButton('3A')
        self.radButton2 = QtWidgets.QRadioButton('3B')
        self.radButton3 = QtWidgets.QRadioButton('3C')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.radButton1)
        self.layout.addWidget(self.radButton2)
        self.layout.addWidget(self.radButton3)
        self.class_selected3 = QtWidgets.QLineEdit()

        self.setLayout(self.layout)

    def nextId(self):
        return Wizard.conclusion


class ConclusionPage(QtWidgets.QWizardPage):
    def __init__(self):
        super(ConclusionPage, self).__init__()

        self.layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label2)
        self.setLayout(self.layout)


class Wizard(QtWidgets.QWizard):
    num_of_pages = 5
    (intro, class1, class2, class3, conclusion) = range(num_of_pages)

    def __init__(self):
        super(Wizard, self).__init__()
        self.setPage(self.intro, IntroductionPage())

        self.setPage(self.class1, ClassesPage1())
        self.setPage(self.class2, ClassesPage2())
        self.setPage(self.class3, ClassesPage3())
        self.setPage(self.conclusion, ConclusionPage())
        self.setStartId(self.intro)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    wizard = Wizard()

    wizard.setWindowTitle("Set Up")
    wizard.setWizardStyle(QtWidgets.QWizard.MacStyle)
    wizard.show()

    sys.exit(app.exec_())
