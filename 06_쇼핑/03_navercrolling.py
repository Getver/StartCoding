# 무한 스크롤 처리 방법
# 현재 스크롤된 높이를 알 수 있는 자바 스크립트 명령어를 이용

# console : 자바 스크립트를 실행할 수 잇는 명령 프롬프트 : 명령어를 입력하면 대답
# window.scrollY : 스크롤 된 높이

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹 사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10)   # 로딩이 끝날 때까지 10초는 기다려줌

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
serch = browser.find_element(By.CSS_SELECTOR, '._searchInput_search_input_QXUFf')
serch.click()
time.sleep(2)

# 검색어 입력
serch.send_keys('아이폰 13')
serch.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script('return window.scrollY')

# 무한 스크롤 : 반복문
while True:
    # 맨 아래로 스크롤을 내린다
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 상품 정보 div

items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7').text
    try:
        price = item.find_element(By.CSS_SELECTOR,'.price_num__2WUXn').text
    except:
        price = '판매중단'
    link = item.find_element(By.CSS_SELECTOR, '.basicList_title__3P9Q7 > a').get_attribute('href')
    
    print(name, price, link)

