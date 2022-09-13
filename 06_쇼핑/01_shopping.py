# requests 한계 :  레니움 라이브러리를 사용하는 이유
#   - 로그인이 필요한 사이트 크롤링이 어렵다
#   - 동적으로 HTML을 만드는 경우 사용 불가능 : 서버에서 정보를 찍어올 때 웹사이트의 
#       정보가 바뀔 때 전체 페이지를 전부다 바꾸는 게 아니고 필요한 부분만 바꾸는 것
#   * 동적으로 HTML 만드는 경우
#       - 스크롤 하거나 클릭하면 데이터 생성 : URL 변경되지 않음 -> 표나 테이블
# 셀리니움 기초 사용법
#   크롬 드라이버 다운, pip install selenium
# 셀리니움 무한 스크롤 처리 방법
# CSV 파일로 저장하는 법

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