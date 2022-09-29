from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir, dir2
    global move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move = 0
                dir += 1
            elif event.key == SDLK_LEFT:

                move = 2
                dir -= 1
            elif event.key == SDLK_UP:
                if move == 1:
                    move = 0
                elif move == 3:
                    move = 2
                dir2 += 1
            elif event.key == SDLK_DOWN:
                if move == 1:
                    move = 0
                elif move == 3:
                    move = 2
                dir2 -= 1

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                move = 1
            elif event.key == SDLK_LEFT:
                dir += 1
                move = 3
            elif event.key == SDLK_UP:
                if move == 0:
                    move = 1
                elif move == 2:
                    move = 3

                dir2 -= 1
            elif event.key == SDLK_DOWN:
                if move == 0:
                    move = 1
                elif move == 2:
                    move = 3

                dir2 += 1



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


running = True
x = 800 // 2
y = 90
frame = 0
dir = 0
dir2 = 0

# RIGHT 0 RIGHT STOP 1 LEFT 2 LEFT_STOP 3
move = 1

while  running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if move == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif move == 1:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    elif move == 2:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif move == 3:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x <= 1260 and x >= 20:
        x += dir * 5
    elif x < 20:
        x += 20
    elif x > 1260:
        x -= 20

    if y <= 1004 and y >= 20:
        y += dir2 * 5
    elif y < 20:
        y += 20
    elif y > 1004:
        y -= 20

    delay(0.01)

close_canvas()

