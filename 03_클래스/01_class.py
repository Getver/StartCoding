# 클래스 : 제품의 설계도
# 객체 : 설계도로 만든 제품
# 속성 : 클래스 안의 변수
# 메서드 : 클래스 안의 함수
# 생성자 : 객체를 만들 때 실행되는 함수
# 인스턴스 : 메모리에 살아있는 객체

# class 클래스이름:
#   def 메서드이름(self):
#       명령블록
# self : 객체에 자기 자신이 들어감
# 객체 = 클래스이름()
# 객체.메서드()    . : ~의

class Monster:
    def say(self):
        print('나는 몬스터다')

shark = Monster()
shark.say()

# 속성 추가하기
class Monster:
    def __init__(self, name):   # self 의 name : 속성
        self.name = name
    def say(self):
        print(f'나는 {self.name}다')

shark = Monster('상어')
shark.say()  # 나는 상어다
wolf = Monster('늑대')
wolf.say()

# shark가 self로 들어가고 상어가 name으로
# self.name : 객체의 이름은 상어다, shark는 상어다


