# 제어문의 종류
# 조건문, 반복문
# 조건문 : 조건에 따라서 실행할 명령이 달라진다
# if 조건식:   - 조건식은 비교연산, 조건식이 참일때 실행되는 명령

distance = int(input('적과의 거리를 입력해주세요 >> '))

if distance >= 200:
    print('저격 소총 쏘기!')
else:
    print('돌격 소총 쏘기!')


# 저녁 메뉴 선택 프로그램

money = int(input('현재 있는 돈은? >> '))

if money >= 20000:
    print('치킨에 맥주를 먹는다')
elif money >= 10000: 
    print('떡볶이를 먹는다')
else: 
    print('편의점 김밥을 먹는다')