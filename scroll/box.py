import game_world
import game_framework
import tilebg as tb
from pico2d import *
import game_framework as gf
import random
import config
import box
import scroll_state
import boy

dir = 0
class Box:
    image = None
    ID = 0
    def __init__(self,_x,_y):
        self.x,self.y = _x,_y
        self.b_dir = 0
        self.active = True
        #Box.ID +=1
        #self.id = Box.ID
        #print("create", self.id,self.x,self.y)


        #self.font = load_font('ENCR10B.TTF',16)
        if Box.image == None:
            Box.image = load_image('../res/box.png')

    def draw(self):
        if self.active:
            self.image.draw(self.x,self.y)
        #  self.font.draw(self.x - 60, self.y + 50, '(id: %3.2f)'%self.id, (255, 255, 0))
       # if config.draws_bounding_box:
        #    draw_rectangle(*self.get_bb())

    def update(self):
        global dir
        if self.active == False:return
        if scroll_state.player.moving == False :return
        if dir == 1:       #좌
            self.x -= 2

        if dir == 2:     #우
            self.x += 2
        if dir == 3:     #상
            self.y -= 2
        if dir == 4:#하
            self.y += 2
    def handle_events(self):
        pass
    def get_bb(self):
        return (self.x - 50, self.y - 50, self.x + 50, self.y + 50)
