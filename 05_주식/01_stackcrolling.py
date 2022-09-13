# 네이버 증권 사이트 현재가 데이터를 파이썬으로 가져온다
# 엑셀을 불러와서 데이터를 저장한다

import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트

codes = [
    '005930',
    '000660',
    '035720'
]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)

