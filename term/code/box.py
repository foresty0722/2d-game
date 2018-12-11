from pico2d import *
import game_framework as gf
import random
import config
import box


class Box:
    image = None
    ID = 0
    def __init__(self,px,py):
        self.x,self.y = px,py



        Box.ID +=1
        self.id = Box.ID
        print("create", self.id,self.x,self.y)


        self.font = load_font('ENCR10B.TTF',16)
        if Box.image == None:
            Box.image = load_image('../res/box.png')

    def draw(self):
        self.image.draw(self.x,self.y)
      #  self.font.draw(self.x - 60, self.y + 50, '(id: %3.2f)'%self.id, (255, 255, 0))
       # if config.draws_bounding_box:
        #    draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def handle_events(self):
        pass
    def get_bb(self):
        return (self.x - 50, self.y - 50, self.x + 50, self.y + 50)
