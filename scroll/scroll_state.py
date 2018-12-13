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

def handle_events():
    global player,sword
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        if (e.type) == (SDL_KEYDOWN):
            player.moving = True
            if stop:
                player.set_dir(0)
                box.dir = 0
                return
            if e.key == SDLK_RIGHT:
                player.set_dir(2)
                box.dir = 1
            if e.key == SDLK_LEFT:
                player.set_dir(1)
                box.dir = 2
            if e.key == SDLK_UP:
                player.set_dir(3)
                box.dir = 3
            if e.key == SDLK_DOWN:
                player.set_dir(4)
                box.dir = 4
            player.set_state(boy.RunState)
        else :
            player.set_state(boy.IdleState)
            player.moving =  False


bg =None

monsters = []
def isMove():
    global boy,boxs
    pass
def enter():
    global boy,bg,boxs,monsters

    init()
    return
    boy = Boy()
    bg = Background()
    boy.bg = bg
    bg.target = boy


    for i in range(2):
        for j in range(8):
            box = Box(450 + i * 90 , 10 + -j * 90)
            #game_world.add_object(box, game_world.layer_box)
            boxs.append(box)

    for i in range(20):
        monster = Monster(600 , 600)
        game_world.add_object(monster,game_world.layer_monster)
        monsters.append(monster)

    game_world.add_object(bg, game_world.layer_bg)
    game_world.add_object(boy, game_world.layer_player)


def draw():
    global boy
    clear_canvas()

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
def init():
    global player,boxs
    player = boy.Boy()
    for i in range(2):
        for j in range(8):
            temp = box.Box( i*100,  j * 100)
            boxs.append(temp)
def update():
    global boy, bg, boxs,sword,player

    player.update()
    isCollider()
    for i in boxs:
        if stop:break
        i.update()
    #wall_player()
    return
    game_world.update()

    isCollider(boy)
    for i in boxs:
        i.update()

    boy.isRun = False


    # if sword:
    #     for b in boxs:
    #         if isCollider(boy,b):
    #             boxs.remove(b)
    #             del (b)
    #             break

    delay(0.03)

# fill here

def exit():
    game_world.clear()



if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()