from pico2d import *
import game_framework
import boy
import game_world
from tilebg import TiledBackground as Background
import box
from monster import Monster
# from enum import Enum

# BOYS_COUNT = 1000

sword = False

left_key_lock = False
right_key_lock = False
up_key_lock = False
down_key_lock = False
bg =None

cand = None


class candy():
    image = None
    def __int__(self, sX, sY):
        self.x = sX
        self.y = sY
        print("succe")
        if candy.image == None:
            self.image = load_image('ball.png')
    def draw(self):
        print("now")
        self.image.draw(300,200)
    def update(self):
        pass


def handle_events():
    global player,sword
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        if (e.type) == (SDL_KEYDOWN):
            if e.key == SDLK_a:
                player.attacking = True
                player.dig()
        if (e.type) == (SDL_KEYDOWN):
            if e.key == SDLK_RIGHT or e.key == SDLK_LEFT or e.key == SDLK_UP or e.key == SDLK_DOWN :
                if e.key == SDLK_RIGHT and right_key_lock == False:     #False라는건 잠금이 해제되었다는뜻이므로 진입가능
                    player.set_dir(2)
                    box.dir = 1
                    player.moving = True
                elif e.key == SDLK_LEFT and left_key_lock == False:
                    player.set_dir(1)
                    box.dir = 2
                    player.moving = True
                elif e.key == SDLK_UP and up_key_lock == False:
                    player.set_dir(3)
                    box.dir = 3
                    player.moving = True
                elif e.key == SDLK_DOWN and down_key_lock == False:
                    player.set_dir(4)
                    box.dir = 4
                    player.moving = True
                if player.moving:
                    player.set_state(boy.RunState)

        else :
            player.set_state(boy.IdleState)
            player.moving =  False
            player.wall_touch = False




def init():
    global player,boxs, cand
    player = boy.Boy()
    cand = candy(1,2)

    color = 0
    for i in range(8):
        for j in range(16):
            if i == 0: color = 1
            if i == 1: color = 2
            temp = box.Box( ((j*1.099999)*95-570)  ,  (i*1.099999) * 95-570,color)
            boxs.append(temp)
def enter():
    init()



def draw():
    global boy,cand
    clear_canvas()

    cand.draw()
    for i in boxs:
        i.draw()
    player.draw()
    #game_world.draw()
    #for i in boxs:
    #     i.draw()
    update_canvas()

stop = False
def wall_player():
    global stop
    for i in boxs:
        if i.x-50 < player.x and i.x + 50 > player.x and i.y +50 > player.y and i.y - 50 < player.y:
            stop = True
            break


def isCollider():
    global player
    if player.attack == False:
        return
    for b in boxs:
        if b.active== False : continue
        la, ba, ra, ta = b.get_bb()

        if la > player.x: continue
        if ra < player.x: continue
        if ta < player.y: continue
        if ba > player.y: continue
        b.active = False
player = None
boxs = []





def update():
    global boy, bg, boxs,sword,player,cand


    player.update()
    isCollider()
    for i in boxs:
        if stop:break
        i.update()
    #wall_player()
    update_frame()

current_time = get_time()

def update_frame():
    global current_time

    game_world.frame_time = (get_time() - current_time)
    current_time += game_world.frame_time

    # if sword:
    #     for b in boxs:
    #         if isCollider(boy,b):
    #             boxs.remove(b)
    #             del (b)
    #             break

# fill here

def exit():
    game_world.clear()



if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()