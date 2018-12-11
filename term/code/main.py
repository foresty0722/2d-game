from pico2d import *
import game_framework as gf
import game_world
import random
import config

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
    def handle_events(self,event):
        pass
    def get_bb(self):
        return (self.x - 50, self.y - 50, self.x + 50, self.y + 50)

class Ground:
    def __init__(self):
        self.image = load_image('../res/ground.png')


    def draw(self):
        self.image.draw(400,300)


def isCollider(player,other):
    la,ba,ra,ta =other.get_bb()
    lb,bb,rb,tb = player.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True



def enter():
    global boy,boxs,ground
    boxs = []

    for i in range(8):
        for j in range(4):
            boxs.append(Box(i*100+50,j*100+50))

    ground  = Ground()

#def exit():
#	pass

def draw():
    global boy,boxs,ground
    clear_canvas()
    clear_canvas()
    ground.draw()
    boy.draw()
    for j in boxs:
        j.draw()

    update_canvas()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    global boy,boxs,ground
    boy.update()
    for b in boxs:
        if isCollider(boy,b):
            #print(b.x,b.y)
            boxs.remove(b)

    delay(0.03)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gf.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                gf.quit()
        else:
            boy.handle_event(event)

def pause():
	pass

def resume():
	pass
