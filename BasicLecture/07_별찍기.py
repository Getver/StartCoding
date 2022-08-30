# 별찍기
# for i in range(1, 6):
#     print('*'*i)

# for i in range(1, 6):
#     print('*'*(6-i))

# for i in range(1, 6):
#     print(' '*(6-i)+'*'*i)

# for i in range(1, 6):
#     print(' '*(i)+'*'*(6-i))


def star(a, b, c):
    if a == 'P':
        if b == 'F':
            for i in range(1, c):
                print('*'*i)
        else:
            for i in range(1, c):
                print('*'*(c-i))
    else:
        if b == 'F':
            for i in range(1, c):
                print(' '*(c-i)+'*'*i)
        else:
            for i in range(1, c):
                print(' '*i+'*'*(c-i))

def star2(a, b, c):
    i = 1
    if a == 'P':
        x = '*'
        if b == 'F': 
            y = 1
        else:
            y = c - i
    else:
        x = ' '
        if b == 'F':
            y = 1
        else: 
            y = c - i
    return x, y

a = input('앞땡김(P) 뒤땡김(B) >> ')
b = input('정방향(F) 역방향(R) >> ')
c = int(input('별의 크기는 >> ')) + 1

# result = star(a, b, c)
result = star(a, b, c)
for i in range(1, c):
    print(a*i)