import requests
import csv
from bs4 import BeautifulSoup



def get_text():
    all_quotes = []
    # 1 페이지에서 500쪽까지 조사하기
    for i in range(1,500):
        webpage = requests.get("https://www.hackers.co.kr/?c=s_lec/lec_study/lec_B_others_wisesay&uid={}&p=1".format(i))
        soup = BeautifulSoup(webpage.content, "html.parser")

        # 영어로 된 명언 부분 추출하기
        eng_texts = soup.find_all("div", attrs={'class': 'text_en'})

        for text in eng_texts:
            quote = [text.find('p').text]
            if len(quote) != 0:
                all_quotes.append(quote)
    return all_quotes

all_quotes = get_text()
print(all_quotes)

def save_csv(all_quotes):
    # all_sayings을 엑셀 파일에 덮어쓰기
    tags = ["Quote(en)", "Person(en)", "Quote(ko)", "Person(ko)", "Date"]
    with open('inspirational_quotes.csv','w') as f:
        write = csv.writer(f)
        write.writerow(tags)
        write.writerows(all_quotes)

save_csv(all_quotes)
