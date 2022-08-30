# 반복문 : 반복해서 명령을 수행하는 것

names = ['티모', '리신', '이즈리얼']

for name in names:
    if name == '티모':
        print(name + '는 탑 챔피언입니다.')
    elif name == '리신':
        print(name + '은 정글 챔피언입니다.')
    else:
        print(name + '은 원딜 챔피언입니다.')

for i in range(1, 11):
    print(i, '번째 페이지입니다.')

a = 20
while a > 10:
    print(a)
    a -= 1