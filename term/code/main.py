from pico2d import *
import game_framework as gf
import random
import config
class Boy:
    KEY = [SDLK_RIGHT,SDLK_LEFT,SDLK_UP,SDLK_DOWN]

    def __init__(self):
        self.frame = random.randint(0,7)
        self.x = 500
        self.y = 440
        self.key = {}
        for k in Boy.KEY:
            self.key[k]= False
        self.image = load_image('../res/run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    #    if config.draws_bounding_box:
     #       draw_rectangle(*self.get_bb())
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x +=10 if self.key[SDLK_RIGHT] else 0
        self.x -= 10 if self.key[SDLK_LEFT] else 0
        self.y += 10 if self.key[SDLK_UP] else 0
        self.y -= 10 if self.key[SDLK_DOWN] else 0
    def handle_events(self,keys):
        if keys.type == SDL_KEYDOWN or keys.type == SDL_KEYUP:
            if keys.key in Boy.KEY:
                self.key[keys.key] = keys.type == SDL_KEYDOWN
    def get_bb(self):
        return self.x - 30 , self.y -30, self.x+30, self.y+ 30


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
    boy = Boy()
    ground  = Ground()

def exit():
	pass

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
    global boy,boxs,ground
    boy.update()
    for b in boxs:
        if isCollider(boy,b):
            #print(b.x,b.y)
            boxs.remove(b)

    delay(0.03)


def handle_events():
    global boy,boxs
    events = get_events()
    for key in events:
        if key.type == SDL_QUIT: gf.quit()
        elif (key.type,key.key) == (SDL_KEYDOWN, SDLK_ESCAPE): gf.pop_state()
        else:
            boy.handle_events(key)



def pause():
	pass

def resume():
	pass



if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas()
    gf.run(glCurrentModule)
    close_canvas()
