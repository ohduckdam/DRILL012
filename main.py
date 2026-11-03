from pico2d import *
from boy import Boy
from grass import Grass, Grass1
from ball import Ball

import game_world   # 게임 월드 모듈 임포트

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            # 자는 중에는 IDLE로만 돌아가고 볼은 발사하지 않음
            if (event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and
                    boy.state != 'SLEEP'):
                ball = Ball(boy.x, boy.y, boy.face_dir * 10)
                game_world.add_object(ball) # 볼을 생성해서 게임 월드에 추가
            boy.handle_event(event)



def reset_world():
    global boy

    boy = Boy()
    game_world.add_object(boy,1) #게임 월드에 객체를 담는 함수 호출

    grass = Grass()
    grass1 = Grass()
    game_world.add_object(grass) #게임 월드에 객체를 담는 함수 호출
    game_world.add_object(grass,2)
  



def update_world():
    game_world.update_world() # 게임 월드에 존재하는 모든 객체를 업데이트
    pass


def render_world():
    clear_canvas()
    game_world.render_world() # 게임 월드에 존재하는 모든 객체를 렌더링
    pass

    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
