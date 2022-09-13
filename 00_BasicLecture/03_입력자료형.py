# 입력 : 프로그램 사용자로부터 받는 데이터
# input() : 입력 함수 : 사용자로부터 데이터를 입력받는 함수
x = int(input('숫자1을 입력하세요 >> '))
y = int(input('숫자2를 입력하세요 >> '))
print(x*y)

a, b = input('두개 띄어쓰기로 입력 >> ').split()
print(a + b)

# 퀴즈 2
year = int(input('태어난 연도를 입력해주세요 >> '))
age = 2022 - year + 1
print(str(age) + '살')

