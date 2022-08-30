# 자료형
# 리스트 만들기 : animal = []

animals = ['사자', '호랑이', '고양이', '강아지']
name = animals[0]
print(animals)
print(name)

# 데이터 추가하기
animals.append('거북이')
print(animals[-1])

# 데이터 삭제하기
del animals[-1]
print(animals[-1])

# 리스트 슬라이싱
print(animals[1:3])

# 리스트 길이
length = len(animals)
print(length)

# 리스트 정렬
animals.sort()  # defalut는 오름차순, 내림차순은 .sort(reverse=True)
print(animals)