from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pyautogui
import requests
from bs4 import BeautifulSoup

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹 사이트 열기
browser.get('https://maple.gg/')
browser.implicitly_wait(10)   # 로딩이 끝날 때까지 10초는 기다려줌

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, '.form-control-lg')
search.click()
time.sleep(2)

# keyword = pyautogui.prompt('검색어를 입력하세요!')
# response = requests.get(f"https://maple.gg/search?q={keyword}")
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')

# 흰달 길드 검색
search.send_keys('흰달')
search.send_keys(Keys.ENTER)
time.sleep(2)

# 나오는 흰달 목록 items에 저장
items = browser.find_elements(By.CSS_SELECTOR, '.font-size-14')

# 흰달 길드 클릭
for item in items:
    if item.text == '루나':
        item.click()
        break


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



# 파일 생성
f = open(r'C:\startcode_python\07_메이플\data_흰달.csv', 'w', encoding='CP949', newline='')
# 1인자: 경로, 2: 쓰기모드, 3: 인코딩(안하면 글자깨짐) 4: 이상한 줄바꿈 안하게

csvWriter = csv.writer(f)

# 운영진과 길드원 구분
biggrade = browser.find_elements(By.CSS_SELECTOR, '.text-center')
del biggrade[0]

for i in biggrade:
    # 길드원 정보 div
    items = i.find_elements(By.CSS_SELECTOR, '.col-lg-3')

    # 길드원 닉넴 직위 직업 저장
    for item in items:

        name = item.find_element(By.CSS_SELECTOR, '.font-size-14').text

        # 만약 운영진이면 운영진을 직위에 넣고
        if i == biggrade[0]:
            grade = item.find_element(By.CSS_SELECTOR, '.member-grade-header').text
        # 길드원이면 길드원이라고 씀
        elif i == biggrade[1]: 
            grade = '길드원'
            
        vocation = item.find_element(By.CSS_SELECTOR,'.font-size-12').text
        # images = browser.find_elements(By.CSS_SELECTOR, "#img > a").get_attribute('href')
        
        print(name, grade, vocation)

        
        # 데이터 쓰기
        csvWriter.writerow([name, grade, vocation])

        
# 파일 닫기
f.close()
