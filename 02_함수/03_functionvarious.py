# 1. 결과값이 없는 함수
def print_sum(a, b):
    print(a + b)

print_sum(1, 2)


# 2. 매개변수가 없는 함수
import random
def get_random_number():
    number = random.randint(1, 10)
    return number

print(get_random_number())

# 3. 결과값과 매개변수가 없는 함수
def print_hello():
    print('hello')

print_hello()