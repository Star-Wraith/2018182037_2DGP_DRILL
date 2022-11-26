import random
from pico2d import *
import game_world
import background
import play_state
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 2400), random.randint(0, 1800), 0


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = self.x + background.FixedBackground.windowcost_x(server.background)
        self.y = self.y + background.FixedBackground.windowcost_y(server.background)
        pass
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def handle_collision(self, other, group):
        print('ball disapeears')
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass