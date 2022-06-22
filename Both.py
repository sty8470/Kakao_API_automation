# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Sending import Sending

class Both(QDialog):
    def __init__(self, data_type):
        super().__init__()
        self.data_type = data_type
        self.sending = Sending()
        self.initUI()
        
    # method for widgets
    def initUI(self):
        self.setWindowTitle('개인과 그룹에게 보내기.')
        self.notice = QLabel('지금 개인과 그룹에게 메세지를 보내고 있어요.')
        self.question = QLabel('몇 명에게 {}을 보내시겠습니까?'.format(self.data_type))
        self.num_input = QLineEdit()
        
        self.text_v_layout = QVBoxLayout()
        self.button = QPushButton('전송')
        self.text_v_layout.addWidget(self.notice)
        self.text_v_layout.addSpacing(10)
        self.text_v_layout.addWidget(self.question)
        self.text_v_layout.addWidget(self.num_input)
        self.text_v_layout.addWidget(self.button)
        self.setLayout(self.text_v_layout)
        
        self.button.clicked.connect(self.groupButtonClicked)
    
    def groupButtonClicked(self):
        num_friends = self.num_input.text()
        
        if self.data_type == "문자":
            self.sending.text_to_individuals(num_friends)
            self.sending.text_to_groups()
        elif self.data_type == "사진":
            self.sending.image_to_individuals(num_friends)
            self.sending.image_to_groups()

    def showDialog(self):
        return super().exec_()
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Both('문자')
    window.showDialog()
    sys.exit(App.exec())

