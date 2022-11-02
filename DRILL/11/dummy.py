# table = {
#     "SLEEP": {"HIT": "WAKE"},
#     "WAKE": {"TIMER10", "SLEEP"}
# }
#
#
#
# cur_state = "SLEEP"
# next_state = table[cur_state]["HIT"] # 상태 변환 테이블 딕셔너리 + 딕셔너리






# class Player:
#     name = 'Player'
# 
#     def __init__(self):
#         self.x = 100
# 
# 
#     def where(self):
#         print(self.x)
# 
# player = Player()
# player.where()
# 
# 
# print(Player.name) # 클래스 변수 출력
# print(player.name) # name이라는 객체 변수가 없으면, 같은 이름의 클라스 변수가 선택됨.
#              # self
# Player.where(player) # 이게 원칙적인 파이썬의 맴버 함수 호출
# player.where() # ==> Player.where(player) 와 동일








# class Star:
#     type = "star" # 클래스 변수
#     x = 100  # 클래스 변수
#
#
#     def change():
#         x = 200
#         print('x is', x)
#
#
# print('x is', Star.x)  # Star라는 이름으로 변수랑 함수를 그룹핑한다.
# Star.change()
#
# star = Star() # 굳이 객체를 생성하는 것도 가능?
# print('x is', star.x) # 객체 뱐수를 액세스하지만, 뭘로 귀착? 클래스 변수 x를 가리킨다.
# star.change()