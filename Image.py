# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Individual import *
from Group import *
from Both import *

class Image(QDialog):
    def __init__(self):
        super().__init__()
        # setting title
        self.num_individual = Individual('사진')
        self.group = Group('사진')
        self.both = Both('사진')
        self.initUI()

    # method for widgets
    def initUI(self):
        self.setWindowTitle('사진 보내기')
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        msgBox = QMessageBox()
        self.individual_button = QPushButton('개인')
        self.group_button = QPushButton('단체')
        self.individual_and_group_button = QPushButton('개인과 단체')
        msgBox.addButton(self.individual_button, msgBox.ActionRole)
        msgBox.addButton(self.group_button, msgBox.ActionRole)
        msgBox.addButton(self.individual_and_group_button, msgBox.ActionRole)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("누구에게 사진를 보낼까요?")
        msgBox.setWindowTitle("QMessageBox Example")
        self.text_v_layout.addWidget(msgBox)

        self.setLayout(self.text_v_layout)
        self.individual_button.clicked.connect(self.individualButtonClicked)
        self.group_button.clicked.connect(self.groupButtonClicked)
        self.individual_and_group_button.clicked.connect(self.individualAndGroupButton)

    
    def individualButtonClicked(self):
        self.num_individual.showDialog()
        print('개인(사진) is clicked!')
    
    def groupButtonClicked(self):
        self.group.showDialog()
        print('단체(사진) is clicked!')
    
    def individualAndGroupButton(self):
        self.both.showDialog()
        print('둘 다(사진) is clicked!')

    def showDialog(self):
        return super().exec_()
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Image()
    window.showDialog()
    sys.exit(App.exec())

