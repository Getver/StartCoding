import random

# def rotto():
#     num = [0, 0, 0, 0, 0, 0]
#     for i in range(0, 6):
#         num[i] = random.randint(1, 46)
#         for j in num:
#             if j == num[i]:
#                 i -= 1
#     return num


# print(rotto())

lotto_number = []

def getRandomNumber():
    number = random.randint(1, 45)
    return number

while True:
    if len(lotto_number) == 6:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_number:
        lotto_number.append(random_number)

while True:
    bonus_number = getRandomNumber()
    if bonus_number not in lotto_number:
        break
print(lotto_number, '+', bonus_number)

