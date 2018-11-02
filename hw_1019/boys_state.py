from pico2d import *
import game_framework
import random
from enum import Enum


class Grass:
    def __init__(self):
        self.image = load_image('../resource/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)



def handle_events():
    global boys
    global span
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT: 
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        else:
            boy.handle_event(e) 

      

def enter():
    global boys, grass

    boys = [ Boy() for i in range(10) ]
    grass = Grass()




def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
