# 딕셔너리 : 키와 값의 쌍으로 이루어진 자료형 

# 변수 사용시
result = '승리'
champ_name = '비에고'
kill = 13
death = 9
assist = 17

# 리스트 사용시
play_data = ['승리', '비에고', 13, 9, 17]

# 딕셔너리
play_data = {
    'result':'승리', 
    'champ_name':'비에고', 
    'kill':13, 
    'death':9, 
    'assist':17
    }

# 기존 값 변경
play_data['result'] = '패배'
print(play_data)

# 새로운 키, 값 추가
play_data['level'] = 18
print(play_data)

# 데이터 삭제
del play_data['champ_name']
print(play_data)

# keys()
for key in play_data.keys():
    print(key)
print(play_data.keys())

# values()
for value in play_data.values():
    print(value)
print(play_data.values())

# items()
for key, value in play_data.items():
    print(key, value)
print(play_data.items())


# 튜플 : 값을 변경할 수 없는 리스트
tuple_a = (1, 2, 3, 4)

print(tuple_a)