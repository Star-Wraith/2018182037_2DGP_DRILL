import pico2d
from pico2d import *
import game_framework
import logo_state
import title_state
import item_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 200), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')



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
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)







# 게임 초기화 : 객체들을 생성
grass = None
running = True
count = 1 # ??
team = None

def enter():
    global grass, running, team, count
    team = [Boy() for i in range(count)] # ??
    grass = Grass()
    running = True


# 게임 종료 - 객체를 소멸
def exit():
    global team, count, grass
    del team
    del grass



def update():
    global team, count

    for boy in team:
        boy.update()


def draw_world():
    global team, count, grass
    grass = Grass()

    grass.draw()
    for boy in team:
        boy.draw()

def draw():
    # 게임 월드 렌더링
    global team, count, grass

    clear_canvas()
    draw_world()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

def pause():
    global grass
    pass


def resume():
    global grass
    pass


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()



if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()




