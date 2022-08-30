# quiz 1
# 프로그램 사용자로부터 삼성전자의 현재가격을 입력 받는다
# 조건에 따라 출력되는 문장을 작성한다

samsung = int(input('삼성전자의 현재 가격을 입력해주세요 >> '))

if samsung >= 90000:
    print('매도합니다')
elif samsung >= 80000:
    print('대기중입니다')
else:
    print('매수합니다')

# quiz 2
# 프로그램 사용자로부터 가방과 시계의 금액을 입력 받는다
# 조건에 따라 합계 금액을 계산하고, 합계금액을 출력한다

bag = int(input('가방의 금액을 입력해주세요 >> '))
watch = int(input('시계의 금액을 입력해주세요 >> '))

sum = float(bag + watch)
sale = 0

if sum >= 100000:
    sale = 0.7 * sum
    print('할인율 30% 적용해서 총', sale, '원 입니다.')
elif sum >= 50000:
    sale = 0.8 * sum
    print('할인율 20% 적용해서 총', sale, '원 입니다.')
else:
    sale = 0.9 * sum
    print('할인율 10% 적용해서 총', sale, '원 입니다.')