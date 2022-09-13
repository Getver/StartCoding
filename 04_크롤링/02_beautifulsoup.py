# beautifulsoup
# HTML 분석을 위한 파이썬 라이브러리
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 네이버 서버에 대화 시도
response = requests.get("https://www.naver.com")

# 네이버에서 html 가져옴
html = response.text

# soup : 원하는 태그 선택 가능(html 번역 선생님으로 스프를 만듦)
soup = BeautifulSoup(html, 'html.parser')

# select_one : 하나의 태그 선택(id값이 ''인거 가져옴)
# id 는 #, class 는 .
word = soup.select_one('#NM_set_home_btn')

# word는 앞에 태그도 다 뜨고 .text를 붙이면 글씨만 뜬다
print(word.text)

