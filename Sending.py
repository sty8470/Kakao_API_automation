# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys, pyautogui, time, pyperclip, os, random


class Sending():
  
    def __init__(self):
        self.search_icon_path = self.get_icon_path('search_icon.png')
        self.person_icon_path = self.get_icon_path('person_icon.png')
        self.img_path = None
        self.icon = None
        self.current_path = os.path.dirname(os.path.realpath(__file__))
    
    def get_icon_path(self, icon_name):
        
        self.img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
        self.icon = self.img_path + icon_name

        return self.icon
    
    def get_icon_coord(self, icon_name):  
        icon_coord = pyautogui.locateCenterOnScreen(self.get_icon_path(icon_name), confidence=0.8)
        x, y = icon_coord
        return x, y

    def get_file_path(self, file_dir_name):
        file_path = os.path.normpath(os.path.join(self.current_path, file_dir_name))
        return file_path
    
    def digitize_pic_filename(self):
        # 모든 사진파일 이름을 숫자로 변경한다.
        # 'pic' 폴더의 디렉토리를 조사합니다
        pic_path = os.path.normpath(os.path.join(self.current_path, 'inspirational_img'))
        # 'pic' 폴더로, 디렉토리를 변경합니다
        os.chdir(pic_path)
        self.num_pic_files = len(os.listdir(pic_path))
        self.file_ext = 'jpg'
        # filenames = os.listdir(pic_path)
        # sorted_filenames = sorted(filenames, key=lambda x: int(x.split('.')[0]) if x.isnumeric())
        # files_to_remove= [file for file in sorted_filenames if '.' not in file]
        # for file in files_to_remove:
        #     file_path = os.path.normpath(os.path.join(pic_path, file))
        #     os.remove(file_path)
        # 잘 지워졌는데 점검코드    
        # print(sorted(os.listdir(pic_path), key=lambda x: int(x.split('.')[0])))
        # 'pic'폴더 안에 있는 모든 파일을 선회하며 조사합니다
        for idx, file in enumerate(os.listdir(pic_path), 1):
            #sorted_filenames = sorted(filenames, key=lambda x: int(x.split('_')[0]))
            #new_name = '{}.{}'.format(str(idx), 'jpg')
            temp_name = '{}'.format(str(idx))
            os.rename(file, temp_name)
        time.sleep(random.uniform(0.5,2))
        for idx, file in enumerate(os.listdir(pic_path), 1):
            new_name = '{}.{}'.format(str(idx), 'jpg')
            os.rename(file, new_name)
    
    def get_num_pic_files(self):
        return self.num_pic_files
    
        
    def text_to_individuals(self, num_friends):

        # search_icon 밑에 있는 내 프로필 사진을 클릭 후 관련 성경 문자 정보를 들고온다.
        search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon_path, grayscale=True, confidence=0.7)
        search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
        pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
        pyautogui.keyDown('enter')
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        bible_texts = pyperclip.paste()
        pyautogui.keyDown('esc')
        print(bible_texts)

        # search_icon을 클릭한 뒤, 키워드('+')를 클릭하고, 순차적으로 친구들에게 성경문자를 전송한다.

        pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate)
        time_wait = random.uniform(0.3, 1)
        time.sleep(time_wait)
        pyautogui.write('+')

        for i in range(1,int(num_friends)+1):
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)
            pyautogui.keyDown('enter')
            print('지금은 {} 번째 친구에게 메세지를 보내고 있습니다.'.format(i))
            pyautogui.hotkey('ctrl', 'v')  
            pyautogui.keyDown('enter')
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)
            pyautogui.keyDown('esc')
            pyautogui.keyDown('down')
        
        # search_icon 한번 클릭하고,
        pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate)

        # 다시 프로필로 돌아가기
        person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon_path, grayscale=True, confidence=0.7)
        person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location

        pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate)


    def text_to_groups(self):

        #search_icon 밑에 있는 내 프로필 사진을 클릭 후 관련 성경 문자 정보를 들고온다.
        search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon_path, grayscale=True, confidence=0.7)
        search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
        pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
        pyautogui.keyDown('enter')
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        bible_texts = pyperclip.paste()
        pyautogui.keyDown('esc')

        print('단톡방에 보내질 현재 성경메세지는 ', bible_texts)

        group_chat_name = ["Harmony", "Howl_village", "Ain_village", "Jeju_trip", "Metro_girls", "Yongmun_girls", "Greenville_sisters", "USA Yongmun", "Chinese Worshipper", "94"]

        # 그룹챗 아이콘을 클릭한다.
        person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon_path, grayscale=True, confidence=0.7)
        person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
        pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate + 65)

        time_wait = random.uniform(0.3,2)
        time.sleep(time_wait)

        # 돋보기 아이콘을 클릭한다.
        inner_search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon_path, grayscale=True, confidence=0.7)
        inner_search_icon_x_coordinate, inner_search_icon_y_coordinate = inner_search_icon_location
        pyautogui.click(inner_search_icon_x_coordinate, inner_search_icon_y_coordinate)

        time_wait = random.uniform(0.3,2)
        time.sleep(time_wait)
        
        # 그룹챗 이름을 돌면서, 그룹챗 이름을 입력한다.
        for chat_name in group_chat_name:

            # 그룹쳇 이름의 한 인스턴스를 저장하여서, 검색창에 붙입니다.
            pyautogui.write(chat_name)
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)
            # pyperclip.paste()
            # pyautogui.hotkey('ctrl', 'v')

            # 조금 시간을 두고, 그 그룹챗방에 들어갑니다.
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)
            pyautogui.keyDown('enter')

            # 여기에서 bible_text을 한번 복사붙여 넣기를 해야 합니다
            pyperclip.copy(bible_texts)
            print('복사된 성경문자는', bible_texts)

            # 어느 정도 시간 간격을 두고, 성경 문자를 붙입니다.
            time_wait = random.uniform(0,3.5)
            time.sleep(time_wait)
            pyautogui.hotkey('ctrl', 'v')

            # 성경문자를 붙이고, enter 키를 내리고 내용을 드디어!!! 전달합니다 !!!
            time.sleep(time_wait)
            pyautogui.keyDown('enter')

            # 지금 보내고 있는 단톡방의 이름 출력하기
            print('지금 성경메세지를 보내고 있는 단톡방은 ', chat_name ,' 방입니다.')

            # 일정한 시간을 두고, esc을 누르고 창을 빠져나옵니다.
            time.sleep(time_wait)
            pyautogui.keyDown('esc')
            time_wait = random.uniform(0,2)
            time.sleep(time_wait)

            pyautogui.keyDown('esc')
            for w in range(len(chat_name)):
                pyautogui.hotkey('backspace')
            time_wait = random.uniform(0,2)
            time.sleep(time_wait)
        
        # search_icon 한번 클릭하고, 성경 문자 발송을 마무리합니다.
        pyautogui.click(inner_search_icon_x_coordinate, inner_search_icon_y_coordinate)
            
    
    def image_to_individuals(self, num_friends):
        # 카카오 메인 화면에서 시작한다
        # 내 프로필 사진을 클릭한다.
        search_icon_x_coord, search_icon_y_coord = self.get_icon_coord('search_icon.png')
        pyautogui.click(search_icon_x_coord,search_icon_y_coord+30)
        pyautogui.keyDown('enter')
        self.digitize_pic_filename()
        random_img_idx = random.randrange(1,self.get_num_pic_files())
        random_img_ext = self.file_ext
        time.sleep(random.uniform(0.5,2))
        send_file_link_search = pyautogui.locateCenterOnScreen(self.get_icon_path('send_file_icon.png'), confidence=0.8)
        x,y = send_file_link_search
        pyautogui.click(x,y)
        img_to_send = os.path.normpath(os.path.join(self.get_file_path('inspirational_img'), '{}.{}'.format(random_img_idx, random_img_ext)))
        pyperclip.copy(img_to_send)
        pyautogui.hotkey('ctrl','v')
        time_wait = random.uniform(0.3,2)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')
        time.sleep(random.uniform(0.5,2.1))
        send_yellow_icon_x_coord, send_yellow_icon_y_coord = self.get_icon_coord('send_yellow_icon.png')
        pyautogui.click(send_yellow_icon_x_coord-40,send_yellow_icon_y_coord-80)
        time.sleep(random.uniform(0.5,2.1))
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(random.uniform(0.5,2.1))
        pyautogui.keyDown('esc')
        time.sleep(random.uniform(0.5,1))
        pyautogui.keyDown('esc')
        search_icon_x_coord, search_icon_y_coord = self.get_icon_coord('search_icon.png')
        pyautogui.click(search_icon_x_coord, search_icon_y_coord)
        time.sleep(random.uniform(0.3,1))
        pyautogui.write('+')
        time.sleep(random.uniform(0.3, 1))
        for i in range(1,int(num_friends)+1):
            time.sleep(random.uniform(0.3,2))
            pyautogui.keyDown('enter')
            print('지금은 {} 번째 친구에게 이미지를 보내고 있습니다.'.format(i))
            pyautogui.hotkey('ctrl', 'v')  
            pyautogui.keyDown('enter')
            time.sleep(random.uniform(0.3,2))
            pyautogui.keyDown('esc')
            pyautogui.keyDown('down')
        # search_icon 한번 클릭하고,
        pyautogui.click(search_icon_x_coord, search_icon_y_coord)
        # 다시 프로필로 돌아가기
        kakao_emoticon_x_coord, kakao_emoticon_y_coord = self.get_icon_coord('kakao_emoticon.png')
        pyautogui.click(kakao_emoticon_x_coord, kakao_emoticon_y_coord-366)
    
    def image_to_groups(self):
        # 카카오 메인 화면에서 시작한다
        # 내 프로필 사진을 클릭한다.
        search_icon_x_coord, search_icon_y_coord = self.get_icon_coord('search_icon.png')
        pyautogui.click(search_icon_x_coord,search_icon_y_coord+30)
        pyautogui.keyDown('enter')
        self.digitize_pic_filename()
        random_img_idx = random.randrange(1,self.get_num_pic_files())
        random_img_ext = self.file_ext
        time.sleep(random.uniform(0.5,2))
        send_file_link_search = pyautogui.locateCenterOnScreen(self.get_icon_path('send_file_icon.png'), confidence=0.8)
        x,y = send_file_link_search
        pyautogui.click(x,y)
        img_to_send = os.path.normpath(os.path.join(self.get_file_path('inspirational_img'), '{}.{}'.format(random_img_idx, random_img_ext)))
        pyperclip.copy(img_to_send)
        pyautogui.hotkey('ctrl','v')
        time_wait = random.uniform(0.3,2)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')
        time.sleep(random.uniform(0.5,2.1))
        send_yellow_icon_x_coord, send_yellow_icon_y_coord = self.get_icon_coord('send_yellow_icon.png')
        pyautogui.click(send_yellow_icon_x_coord-40,send_yellow_icon_y_coord-80)
        time.sleep(random.uniform(0.5,2.1))
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(random.uniform(0.5,2.1))
        pyautogui.keyDown('esc')
        time.sleep(random.uniform(0.5,1))
        pyautogui.keyDown('esc')
        
        group_chat_name = ["Harmony", "House", "0093", "Howl_village", "Ain_village", "Jeju_trip", "Metro_girls", "Yongmun_girls", "Greenville_sisters", "USA Yongmun", "Chinese Worshipper", "94"]

        # 그룹챗 아이콘을 클릭한다.
        person_icon_location = pyautogui.locateCenterOnScreen(self.person_icon_path, grayscale=True, confidence=0.7)
        person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
        pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate + 65)

        time_wait = random.uniform(0.3,2)
        time.sleep(time_wait)

        # 돋보기 아이콘을 클릭한다.
        inner_search_icon_location = pyautogui.locateCenterOnScreen(self.search_icon_path, grayscale=True, confidence=0.7)
        inner_search_icon_x_coordinate, inner_search_icon_y_coordinate = inner_search_icon_location
        pyautogui.click(inner_search_icon_x_coordinate, inner_search_icon_y_coordinate)

        time_wait = random.uniform(0.3,2)
        time.sleep(time_wait)
        
        # 그룹챗 이름을 돌면서, 그룹챗 이름을 입력한다.
        for chat_name in group_chat_name:

            # 그룹쳇 이름의 한 인스턴스를 저장하여서, 검색창에 붙입니다.
            pyautogui.write(chat_name)
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)

            # 조금 시간을 두고, 그 그룹챗방에 들어갑니다.
            time_wait = random.uniform(0.3,2)
            time.sleep(time_wait)
            pyautogui.keyDown('enter')

            print('지금은 {} 채팅방에 이미지를 보내고 있습니다.'.format(chat_name))
            pyautogui.hotkey('ctrl', 'v')  
            pyautogui.keyDown('enter')
            time.sleep(random.uniform(0.3,2))
            pyautogui.keyDown('esc')
            
            for w in range(len(chat_name)):
                pyautogui.hotkey('backspace')
            time_wait = random.uniform(0,2)
            time.sleep(time_wait)
            
        # 다시 프로필로 돌아가기
        kakao_emoticon_x_coord, kakao_emoticon_y_coord = self.get_icon_coord('kakao_emoticon.png')
        pyautogui.click(kakao_emoticon_x_coord, kakao_emoticon_y_coord-366)