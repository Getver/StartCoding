# URL : 인터넷 주소 형식
# Protocol//Domain/Path?Parameter
# parameter : ?key=value&key=value

# pyautogui
# 마우스, 키보드 매크로 라이브러리, 간단한 입력 창 띄우기

import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt('검색어를 입력하세요!')
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text

# f string : f 를 쓰고 변수 자리에 {변수명} 이렇게 씀

soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit')

for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)

