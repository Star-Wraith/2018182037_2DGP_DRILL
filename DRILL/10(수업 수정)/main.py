import pico2d
import play_state
import logo_state


# state = logo_state # 모듈을 변수로 취급


pico2d.open_canvas()
states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:

        state.handle_events()
        # 게임 월드 객체를 업데이트 - 게임 로직
        state.update()
        state.draw()
    state.exit()


# # game main loop code
# while state.running:
#     state.handle_events()
#     # 게임 월드 객체를 업데이트 - 게임 로직
#     state.update()
#     state.draw()
#     pico2d.delay(0.05)
# state.exit()
# state = play_state
#
# state.enter()
#
# # game main loop code
# while state.running:
#     state.handle_events()
#     # 게임 월드 객체를 업데이트 - 게임 로직
#     state.update()
#     state.draw()
#     pico2d.delay(0.05)
# state.exit()


# finalization code
pico2d.close_canvas()
