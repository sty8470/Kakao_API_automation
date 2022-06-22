import requests
import csv
from bs4 import BeautifulSoup

def get_images():

    webpage = requests.get("https://www.pinterest.co.kr/search/pins/?q=daily%20inspirational%20quotes&rs=typed&term_meta[]=daily%7Ctyped&term_meta[]=inspirational%7Ctyped&term_meta[]=quotes%7Ctyped")
    soup = BeautifulSoup(webpage.content, "html.parser")

    divs = soup.find_all('div', attrs={'class': 'img.hCL.kVc.L4E.Mlw'})
    #eng_texts = soup.find_all("div", attrs={'class': 'text_en'})
    print(divs)

get_images()