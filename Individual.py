# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from kakao import KakaoAutomation
import sys
from Sending import Sending

class Individual(QDialog):
    def __init__(self, data_type):
        super().__init__()
        # setting title
        self.data_type = data_type
        self.sending = Sending()
        self.initUI()
        
    # method for widgets
    def initUI(self):
        self.setWindowTitle('개인에게 보내기')
        self.question = QLabel('몇 명에게 {}을 보내시겠습니까?'.format(self.data_type))
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        self.num_input = QLineEdit()
        self.button = QPushButton('전송')
        self.unit = QLabel('명')
        self.text_h_layout.addWidget(self.num_input)
        self.text_h_layout.addWidget(self.unit)
        self.text_v_layout.addWidget(self.question)
        self.text_v_layout.addSpacing(10)
        self.text_v_layout.addLayout(self.text_h_layout)
        self.text_v_layout.addSpacing(10)
        self.text_v_layout.addWidget(self.button)
        self.setLayout(self.text_v_layout)
        
        self.button.clicked.connect(self.individualButtonClicked)
    
    def individualButtonClicked(self):
        num_friends = self.num_input.text()
        
        if self.data_type == "문자":
            self.sending.text_to_individuals(num_friends)
        elif self.data_type == "사진":
            self.sending.images_to_individuals(num_friends)

    def showDialog(self):
        return super().exec_()
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Individual('문자')
    window.showDialog()
    sys.exit(App.exec())

