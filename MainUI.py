# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from kakao import KakaoAutomation
import sys
# kakao = KakaoAutomation()
from Text import Text 
from Image import Image
class MainUI(QDialog):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("카카오 자동전송 프로그램")
        self.text_obj = Text()
        self.image_obj = Image()
        self.initUI()

    # method for widgets
    def initUI(self):
        self.setWindowTitle('카카오톡 자동전송하기 프로그램')
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        msgBox = QLabel("카카오톡 자동전송을 시작합니다. 어떤 파일을 보낼까요?")
        self.text_button = QPushButton('문자')
        self.image_button = QPushButton('사진')
        # self.voice_button = QPushButton('목소리')
        self.text_v_layout.addWidget(msgBox)
        self.text_h_layout.addWidget(self.text_button)
        self.text_h_layout.addWidget(self.image_button)
        # self.text_h_layout.addWidget(self.text_button)
        # msgBox.addButton(self.text_button, msgBox.ActionRole)
        # msgBox.addButton(self.image_button, msgBox.ActionRole)
        # msgBox.addButton(self.voice_button, msgBox.ActionRole)
        # msgBox.setIcon(QMessageBox.Question)
        # msgBox.setText("카카오톡 자동전송을 시작합니다 \n\n어떤 파일을 보낼까요?")
        # msgBox.setText("어떤 파일을 보낼까요?")
        msgBox.setWindowTitle("QMessageBox Example")
        self.text_v_layout.addLayout(self.text_h_layout)
        # self.text_h_layout.addWidget(self.text_button)
        # self.text_h_layout.addWidget(self.photo_button)
        # self.text_v_layout.addLayout(self.text_h_layout)
        self.setLayout(self.text_v_layout)
        self.text_button.clicked.connect(self.textClicked)
        self.image_button.clicked.connect(self.imageClicked)
      
        # self.text_v_layout = QVBoxLayout()
        # self.questionMark = QMessageBox()
        # self.questionMark.setIcon(QMessageBox.Question)
        # self.notice = QLabel("카카오톡 자동전송을 시작합니다 ")
        # self.survey = QLabel("어떤 파일을 보낼까요? ")
        # self.text_v_layout.addWidget(self.notice)
        # self.text_v_layout.addWidget(self.survey)
        # self.text_h_layout.addWidget(self.qustionMark)
        # self.text_h_layout.addLayout(self.text_v_layout)
        # self.setLayout(self.text_h_layout)
    
    def textClicked(self):
        self.text_obj.showDialog()
    
    def imageClicked(self):
        self.image_obj.showDialog()
        
    # def voiceClicked(self):
    #     print('voice is clicekd!')
        
    def showDialog(self):
        return super().exec_()
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MainUI()
    window.showDialog()
    sys.exit(App.exec())

