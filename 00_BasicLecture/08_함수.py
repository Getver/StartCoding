# 반복적으로 사용되는 코드를 함수로 만든다
def sum(a, b):
    result = a + b
    return result

x = sum(1, 2)
y = sum(4, 5)
print(x, y)

import random

def getRandomNumber():
    number = random.randint(1, 10)
    return number

print(getRandomNumber())


def printName(name):
    print(name)

printName('스타트코딩')


def sayHi():
    print('Hi')

sayHi()