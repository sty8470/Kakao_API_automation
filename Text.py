# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Individual import *
from Group import *
from Both import Both

import sys
class Text(QDialog):
    def __init__(self):
        super().__init__()
        # setting title
        self.initUI()
        self.num_individual = Individual('문자')
        self.group = Group('문자')
        self.both = Both('문자')
     
    # method for widgets
    def initUI(self):
        self.setWindowTitle('문자 보내기')
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        self.msg_h_layout = QHBoxLayout()
        msgBox = QLabel()
        msgBox.setText("누구에게 문자를 보낼까요? 아래 버튼을 클릭해주세요")
        self.individual_button = QPushButton('개인')
        self.group_button = QPushButton('단체')
        self.individual_and_group_button = QPushButton('개인과 단체')
        # msgBox.addButton(self.individual_button, msgBox.ActionRole)
        # msgBox.addButton(self.group_button, msgBox.ActionRole)
        # msgBox.addButton(self.individual_and_group_button, msgBox.ActionRole)
        # msgBox.setIcon(QMessageBox.Question)
        # msgBox.setText("누구에게 문자를 보낼까요?")
        # msgBox.setWindowTitle("QMessageBox Example")
        # self.text_v_layout.addWidget(msgBox)
        self.text_h_layout.addWidget(self.individual_button)
        self.text_h_layout.addWidget(self.group_button)
        self.text_h_layout.addWidget(self.individual_and_group_button)
        self.msg_h_layout.addWidget(msgBox)
        self.text_v_layout.addLayout(self.msg_h_layout)
        self.text_v_layout.addLayout(self.text_h_layout)

        self.setLayout(self.text_v_layout)
        self.individual_button.clicked.connect(self.individualButtonClicked)
        self.group_button.clicked.connect(self.groupButtonClicked)
        self.individual_and_group_button.clicked.connect(self.individualAndGroupButtonClicked)

    
    def individualButtonClicked(self):
        self.num_individual.showDialog()
        print('개인(문자) is clicked!')
        
    def groupButtonClicked(self):
        self.group.showDialog()
        print('개인(문자) is clicked!')
        
    def individualAndGroupButtonClicked(self):
        self.both.showDialog()
        print('개인(문자) is clicked!')

    def showDialog(self):
        return super().exec_()
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Text()
    window.showDialog()
    sys.exit(App.exec())

