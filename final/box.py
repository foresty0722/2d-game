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

floor1_image = load_image("../res/1_floor.png")
floor2_image = load_image("../res/2_floor.png")
class Box:
    image = None
    ID = 0
    def __init__(self,_x,_y,_category):
        self.x,self.y = _x,_y
        self.b_dir = 0
        self.active = True
        self.velocity = game_world.GRASS_SPEED_PPS
        #Box.ID +=1
        #self.id = Box.ID
        #print("create", self.id,self.x,self.y)
        self.image = None
        if _category == 1:
            self.image = floor1_image
        elif _category == 2:
            self.image = floor2_image
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

        if dir == 1 and scroll_state.right_key_lock == False:       #좌
            self.x -= self.velocity * game_world.frame_time

        if dir == 2and scroll_state.left_key_lock == False:     #우
            self.x += self.velocity * game_world.frame_time
        if dir == 3and scroll_state.up_key_lock == False:     #상
            self.y -= self.velocity * game_world.frame_time
        if dir == 4and scroll_state.down_key_lock == False:#하
            self.y += self.velocity * game_world.frame_time
    def handle_events(self):
        pass
        (self.x - 25, self.y - 30, self.x + 25, self.y + 30)
    def get_bb(self,_obj):
        if self.x-50 < _obj.x+25 and self.x + 50 > _obj.x-25 and self.y - 50 < _obj.y+30 and self.y + 50 > _obj.y-30:

            if self.x+50 <= _obj.x and  box.dir == 2 and self.y+50 > _obj.y:
                scroll_state.left_key_lock = True
            elif self.x-50 >= _obj.x and box.dir == 1 :
                scroll_state.right_key_lock = True
            elif self.y-50 >= _obj.y and box.dir == 3 :
                scroll_state.up_key_lock = True
            elif self.y+50 <= _obj.y and box.dir == 4  :
                scroll_state.down_key_lock = True
            return True
        return False