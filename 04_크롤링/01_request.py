# requests: HTTP 통신을 위한 파이썬 라이브러리
# 라이브러리 : 프로그램 개발을 쉽게 하기 위한 도구
# HTTP 통신 : 인터넷에 접속했을 때 발생하는 대화(=서버와 내가 소통)
# GET : 해당 페이지 보여줌 POST: 아이디, 비번으로 로그인

# pip install requests

import requests

response = requests.get("https://www.naver.com")
html = response.text
print(html)