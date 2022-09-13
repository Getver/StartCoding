from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pyautogui
import requests

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹 사이트 열기
browser.get('https://maple.gg/')
browser.implicitly_wait(10)   # 로딩이 끝날 때까지 10초는 기다려줌

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, '.form-control-lg')
search.click()
time.sleep(2)

# # 검색어 입력
# keyword = pyautogui.prompt('검색어를 입력하세요!')
# response = requests.get(f"{keyword}")
search.send_keys('흰달')
search.send_keys(Keys.ENTER)


# # 검색창 클릭
# search = browser.find_element(By.CSS_SELECTOR, '._searchInput_search_input_QXUFf')
# search.click()
# time.sleep(2)

# # 검색어 입력
# search.send_keys('아이폰 13')
# search.send_keys(Keys.ENTER)

# # 스크롤 전 높이
# before_h = browser.execute_script('return window.scrollY')

# # 무한 스크롤 : 반복문
# while True:
#     # 맨 아래로 스크롤을 내린다
#     browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

#     # 스크롤 사이 페이지 로딩 시간
#     time.sleep(1)

#     # 스크롤 후 높이
#     after_h = browser.execute_script("return window.scrollY")

#     if after_h == before_h:
#         break
#     before_h = after_h

# # 파일 생성
# f = open(r'C:\startcode_python\06_쇼핑\data.csv', 'w', encoding='CP949', newline='')
# # 1인자: 경로, 2: 쓰기모드, 3: 인코딩(안하면 글자깨짐) 4: 이상한 줄바꿈 안하게

# csvWriter = csv.writer(f)

# # 상품 정보 div
# items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__TWvzp')

# for item in items:

#     name = item.find_element(By.CSS_SELECTOR, '.basicList_title__VfX3c').text
#     try:
#         price = item.find_element(By.CSS_SELECTOR,'.basicList_price_area__K7DDT').text
#     except:
#         price = '판매중단'

#     link = item.find_element(By.CSS_SELECTOR, '.basicList_title__VfX3c > a').get_attribute('href')
    
#     print(name, price, link)

    
#     # 데이터 쓰기
#     csvWriter.writerow([name, price, link])

# # 파일 닫기
# f.close()
