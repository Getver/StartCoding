# quiz 1
# 프로그램 사용자로부터 자연수를 입력 받고, 0부터 자연수까지의 합계를 출력하세요

num = int(input('자연수를 입력해주세요 >> '))

sum = 0
for i in range(1, num+1):
    sum += i

print('총 합계는', sum, '입니다.')


# quiz 2
# 사용자로부터 -1을 받으면 프로그램이 종료되는 프로그램을 작성해보세요

print('프로그램 시작합니다.')

while True:
    num = int(input('-1을 입력하시면 프로그램이 종료됩니다. >> '))
    if num == -1:
        break
print('드디어 입력하셨군요!')

# quiz 3

while True:
    print('[메뉴를 입력하세요]')
    menu = int(input('1. 게임시작 2. 랭킹보기 3. 게임종료 >> '))
    if menu == 1:
        print('-> 게임을 시작합니다')
    elif menu == 2:
        print('-> 랭킹보기')
    elif menu == 3:
        print('게임을 종료합니다')
        break
    else: 
        print('다시 입력해주세요')

