'''

This python script gets access to certain directory in which multiple image files reside
Afterwards, the following function changes all file names by a numerical order

Default condition 1: 현재 파이썬 파일이 위치해 있는 디렉토리에, 'pic'이라는 빈 폴더를 만듭니다
Default condition 2: 그 'pic'이라는 빈 폴더에 내가 저장하고 싶은 모든 이미지 파일들을 옮겨서 저장해둡니다
Default condition 3: 새로운 이미지를 추가할 때, 그 이미지는 숫자와 영문자의 조합으로 이루어졌다고 가정합니다 (순수 숫자는 없다고 가정합니다)

'''

# sys와 os : 필요한 라이브러리들을 import합니다
import sys, os
from os import remove
from shutil import move

# 현재, 내 파이썬 파일이 위치하고 있는 경로를 조사합니다
current_path = os.path.dirname(os.path.realpath(__file__))

def change_img_file_name(current_path):

    # 'pic' 폴더의 디렉토리를 조사합니다
    pic_path = os.path.normpath(os.path.join(current_path, 'inspirations_img'))

    # 'pic' 폴더로, 디렉토리를 변경합니다
    os.chdir(pic_path)

    # 'pic'폴더 안에 있는 모든 파일을 선회하며 조사합니다
    for idx, file in enumerate(os.listdir(pic_path)):
        # 만일 파일안에 '.'이 있다면 (즉, 확장자가 정확히 명시된 파일이면)
        if '.' in file:
            # 파일 이름과 파일 확장자명을 따로 분리합니다
            file_name, file_ext = file.split('.')
            # if not os.path.exists()
            # 새로 그 이미지 파일에 번호를 매기고, 확장자 명을 string으로 추가합니다
            new_name = '{}.{}'.format(str(idx), file_ext)
            if new_name in os.listdir(pic_path):
                continue
            # 기존의 파일의 이름을 새 파일의 이름으로 바꾸어줍니다
            os.rename(file, new_name)

change_img_file_name(current_path)


