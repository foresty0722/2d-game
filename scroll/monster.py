import random
from pico2d import *

class Monster:
    image = None
    def __init__(self,_x,_y):
        self.x, self.y = _x, _y
        #_x = random.randint(100,600)
        #_y = random.randint(100,600)
        self.x = 300
        self.y = 300

        if Monster.image == None:
            Monster.image = load_image('../res/ball.png')

    def get_bb(self):
        return (self.x - 25, self.y - 30, self.x + 25, self.y + 30)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def handle_events(selfs):
        pass


