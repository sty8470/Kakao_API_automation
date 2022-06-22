
import sys
import pyautogui
import time


import pyperclip
import os
import random


def fetch_icon_path(icon_name):
    
    img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
    icon = img_path + icon_name

    return icon

search_icon_path = fetch_icon_path('search_icon.png')
person_icon_path = fetch_icon_path('person_icon.png')


def send_bible_texts_to_individuals(search_icon_path, person_icon_path, num_friends):

    # search_icon 밑에 있는 내 프로필 사진을 클릭 후 관련 성경 문자 정보를 들고온다.
    search_icon_location = pyautogui.locateCenterOnScreen(search_icon_path, grayscale=True, confidence=0.7)
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

    for i in range(1,num_friends+1):
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
    person_icon_location = pyautogui.locateCenterOnScreen(person_icon_path, grayscale=True, confidence=0.7)
    person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location

    pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate)




def send_bible_texts_to_groups(search_icon_path, person_icon_path):

    #search_icon 밑에 있는 내 프로필 사진을 클릭 후 관련 성경 문자 정보를 들고온다.
    search_icon_location = pyautogui.locateCenterOnScreen(search_icon_path, grayscale=True, confidence=0.7)
    search_icon_x_coordinate, search_icon_y_coordinate = search_icon_location
    pyautogui.click(search_icon_x_coordinate, search_icon_y_coordinate + 30)
    pyautogui.keyDown('enter')
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    bible_texts = pyperclip.paste()
    pyautogui.keyDown('esc')

    print('단톡방에 보내질 현재 성경메세지는 ', bible_texts)

    group_chat_name = ["Harmony", "Howl_village", "Ain_village", "Jeju_trip", "Metro_girls", "Yongmun_girls", "Greenville_sisters", "USA Yongmun", "Chinese Worshipper", "2022", "94"]

    # 그룹챗 아이콘을 클릭한다.
    person_icon_location = pyautogui.locateCenterOnScreen(person_icon_path, grayscale=True, confidence=0.7)
    person_icon_x_coordinate, person_icon_y_coordinate = person_icon_location
    pyautogui.click(person_icon_x_coordinate, person_icon_y_coordinate + 65)

    time_wait = random.uniform(0.3,2)
    time.sleep(time_wait)

    # 돋보기 아이콘을 클릭한다.
    inner_search_icon_location = pyautogui.locateCenterOnScreen(search_icon_path, grayscale=True, confidence=0.7)
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
    

def main():
    print("######################################################")

    print("아래의 주의 사항을 실행전에 꼭 읽어주시고 실행해주세요!! ~")
    print("1. 성경 문자를 보낼 친구의 이름뒤에는 반드시 + 표식을 붙여주세요!")
    print("2. 실행 전에 반드시 키보드 언어 세팅은 영어로 맞추어 주세요! ")
    print("3. 실행전에 필요없는 대화창은 모두 다 종료해주세요.")
    print("4. 실행전에 반드시 카카오톡 기본화면이 화면의 절반에는 위치하도록 설정해주세요! ")
    print("5. 보내실 성경메세지를 복사하여서 \'나에게 쓰는 카카오톡 창에 붙여넣기하고 esc을 눌러주세요 (붙여넣기만 하고 enter을 누르고 보내지는 마세요!)\'")
    print("6. 성경문자를 몇 명에게 보낼 껀지 \'+\'로 검색하여서 미리 계산하고 있으시고, 프로그램 실행뒤에 그 숫자만 입력한 뒤에 enter을 눌러주세요! ")
    print("7. \'+\'로 친구 숫자를 검색하고는 밑에 print문의 친구 숫자를 업데이트 해주세요, 그리고 다시 4번 화면으로 돌아가도록 맞춰주세요")
    print("8. 만약, 실행하다가 에러가 날 경우에는, ctrl+c을 같이 눌러주세요!")
    print("9. 이외에, 궁금한 사항이 있으시면 010-7791-8470으로 연락주세요! ")
    print("10. 본 소프트웨어의 저작권은 @신태영에게 있음을 공지합니다. @Copyright Taeyoung 2021")

    print("######################################################")
    print("######################################################")
    print("현재 friend는 102명 입니다!!!")
    num_friends = int(input("성경문자를 보낼 친구의 숫자를 입력하세요: "))
    send_bible_texts_to_individuals(search_icon_path, person_icon_path, num_friends)
    time_wait = random.uniform(0.3,2)
    time.sleep(time_wait)

    # 이 함수를 실행시키기전에, 반드시, 내게 쓰는 카카오창을 열고, 성경문자를 한번 복사 해야 합니다!!
    send_bible_texts_to_groups(search_icon_path, person_icon_path)

main()


















'''


# def read_bible_text():
#     file = open('bible_text.txt','r', encoding='utf-8')
#     tailored = []
#     for content in file:
#         tailored.append(content.strip())
#     file.close()
#     return tailored


# bible_texts = read_bible_text()
#print('bible_texts are ', bible_texts)


# def print_bible_text(bible_texts):
#     for text in bible_texts:
#         print(text)

# print_bible_text(bible_texts)


def send_msg(my_msg, repeat_number):
    for i in range(int(repeat_number)):
        time_wait = random.uniform(1, 3)
        print('Repeat Number : ', i + 1, end='')
        print(' // Time wait : ', time_wait)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')
        pyperclip.copy(my_msg)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')


def filter_friend(filter_keyword, init_number):
    # 사람 아이콘 클릭
    try:
        click_img(img_path + 'person_icon.png')
        print('person_icon.png is clicked now!')
        try:
            click_img(img_path + 'person_icon2.png')
            print('person_icon2.png is clicked now!')
        except Exception as e :
            print('e ', e)
            print('person_icon2.png is not clicked unfortunately!')
    except Exception as e :
        print('e ', e)
        print('person_icon.png is not clicked unfortunately!')
    # X 버튼이 존재한다면 클릭하여 내용 삭제
    try:
        click_img(img_path + 'x.png')
        print('x.png is clicked now!')
    except:
        pass
    time.sleep(1)
    # 돋보기 아이콘 오른쪽 클릭
    click_img_plus_x(img_path+'search_icon.png', 60, 30)
    # 필터값을 설정하지 않으면 모든 친구들에게 보내게 된다.
    if filter_keyword == '':
        # esc을 눌러서, filter값을 검색창에서 삭제한다.
        pyautogui.keyDown('esc')
        print('esc button is just pressed!')
    else:
        pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')
    for i in range(int(init_number)-1):
        pyautogui.keyDown('down')
        print('down key is just pressed!')
    time.sleep(2)


def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y)


def click_img_plus_x(imagePath, x_pixel, y_pixel):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x - x_pixel, y + y_pixel)


# def doubleClickImg (imagePath):
#     location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
#     x, y = location
#     pyautogui.click(x, y, clicks=2)


def set_delay():
    delay_time = input("몇 초 후에 프로그램을 실행하시겠습니까? : ")
    print(delay_time + "초 후에 프로그램을 실행합니다.")
    for remaining in range(int(delay_time), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r프로그램 실행!\n")


# def logout():
#     try:
#         click_img(img_path + 'menu.png')
#     except Exception as e:
#         print('e ', e)
#     try:
#         click_img(img_path + 'logout.png')
#     except Exception as e:
#         print('e ', e)


# def bye_msg():
#     input('프로그램이 종료되었습니다.')


def set_import_msg():
    with open("send_for_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        print('======== 아래는 전송할 텍스트입니다. ========\n', text)
        return text

 
def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    print(pyautogui.position())
    filter_keyword = input("필터링할 친구 이름. 없으면 enter.   ex) 학생 직장 99 : ")
    init_number = input("필터링한 친구 기준 시작지점(ex. 필터링된 친구 시작지점) : ")
    repeat_number = input("반복할 횟수(ex. 필터링 검색된 친구 수) : ")
    my_msg = input("전송할 메세지. enter를 누를 경우 send_for_text.txt를 전송 : ")
    print('=================')
    print('메세지 전송 시작!')
    print('=================') 
    return (filter_keyword, init_number, repeat_number, my_msg)

  
# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.9
pyautogui.PAUSE = 0.5

if __name__ == "__main__":
    (filter_keyword, init_number, repeat_number, my_msg) = initialize()
    if len(my_msg) > 2:
        filter_friend(filter_keyword, init_number)
        send_msg(my_msg, repeat_number)
        #bye_msg()

    else:
        long_msg = set_import_msg()
        set_delay()
        filter_friend(filter_keyword, init_number)
        send_msg(long_msg, repeat_number)
        #logout()
        #bye_msg()

'''
