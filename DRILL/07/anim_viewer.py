from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('eagle.png')

x = 0
frame = 0

# def move_move(left, bottom, width, height, x, y, frame):
#     clear_canvas()
#     character.clip_draw(frame * left, bottom, width, height, x, y)
#     update_canvas()
#     frame = (frame + 1) % 3
#     x = x + 10
#     delay(0.04)
#     get_events()


# left->right move
while (x < 800):

    clear_canvas()
    character.clip_draw(frame * 133, 143, 133, 143, x, 500)
    update_canvas()
    frame = (frame+1) % 3
    x = x+10
    delay(0.04)
    get_events()
# right -> left move
while (x > 0):
    clear_canvas()
    character.clip_draw(frame * 133, 286, 133, 143, x, 200)
    update_canvas()
    frame = (frame+1) % 3
    x = x-10
    delay(0.04)
    get_events()
# up -> down move
y = 550
while (y > 0):
    clear_canvas()
    character.clip_draw(frame * 142, 429, 133, 143, 400, y)
    update_canvas()
    frame = (frame + 1) % 3
    y = y-10
    delay(0.04)
    get_events()
# down -> up move
while(y < 550):
    clear_canvas()
    character.clip_draw(frame * 142, 0, 133, 143, 400, y)
    update_canvas()
    frame = (frame + 1) % 3
    y = y+10
    delay(0.04)
    get_events()

close_canvas()

