import pico2d
from pico2d import *
import game_framework
import logo_state
import title_state
import item_state
import random
import boy_adjust_state
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None



    def update(self):

        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 400:
            self.dir = -1
            self.x = 400
        elif self.x < 100:
            self.dir = 1
            self.x = 100


    def draw(self):
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10, self.y+50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)

        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    # game_framework_change_state(title_state)
                    game_framework.quit()
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_b:
                    game_framework.push_state(boy_adjust_state)







# 게임 초기화 : 객체들을 생성
boys = [] # 여러 명의 소년들

grass = None
running = True

def enter():
    global grass, running
    boys.append(Boy())
    boys.append(Boy())
    grass = Grass()
    running = True


# 게임 종료 - 객체를 소멸
def exit():
    global grass
    for boy in boys:
        del boy
    del grass



def update():
    for boy in boys:
        boy.update()


def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()

def draw():
    # 게임 월드 렌더링
    global grass

    clear_canvas()
    draw_world()
    grass.draw()
    for boy in boys:
        boy.draw()
    update_canvas()

def pause():
    global grass
    pass


def resume():
    global grass
    pass


def add_one_boy():
    boys.append(Boy())


def delete_one_boy():
    if len(boys) > 1:
        boys.pop() # 리스트의 맨 마지막을 꺼내는 것

def set_all_boys_item(item):
    for boy in boys:
        boy.item = item


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()



if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()




