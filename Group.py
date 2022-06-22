# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Sending import Sending

class Group(QDialog):
    def __init__(self, data_type):
        super().__init__()
        # setting title
        self.data_type = data_type
        self.sending = Sending()
        self.initUI()
        
    # method for widgets
    def initUI(self):
        self.setWindowTitle('그룹에게  보내기.')
        self.notice = QLabel('지금 {}을 전송할 그룹들은 다음과 같습니다'.format(self.data_type))
        
        # self.question = QLabel('몇 명에게 {}을 보내시겠습니까?'.format(self.data_type))
        self.text_v_layout = QVBoxLayout()
        # self.text_h_layout = QHBoxLayout()
        # self.num_input = QLineEdit()
        self.button = QPushButton('전송')
        # self.unit = QLabel('명')
        # self.text_h_layout.addWidget(self.num_input)
        # self.text_h_layout.addWidget(self.unit)
        self.text_v_layout.addWidget(self.notice)
        self.text_v_layout.addSpacing(10)
        
        # self.text_v_layout.addLayout(self.text_h_layout)
        # self.text_v_layout.addSpacing(10)
        self.text_v_layout.addWidget(self.button)
        self.setLayout(self.text_v_layout)
        
        self.button.clicked.connect(self.groupButtonClicked)
    
    def groupButtonClicked(self):
        
        if self.data_type == "문자":
            self.sending.text_to_groups()
        elif self.data_type == "사진":
            self.sending.image_to_groups()

    def showDialog(self):
        return super().exec_()
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Group('문자')
    window.showDialog()
    sys.exit(App.exec())

