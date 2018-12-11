from pico2d import *
import game_framework as gf
import random
import game_world
import config
import box


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class WalkingState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHTKEY_DOWN:
            boy.x_velocity += RUN_SPEED_PPS
        elif event == RIGHTKEY_UP:
            boy.x_velocity -= RUN_SPEED_PPS
        if event == LEFTKEY_DOWN:
            boy.x_velocity -= RUN_SPEED_PPS
        elif event == LEFTKEY_UP:
            boy.x_velocity += RUN_SPEED_PPS

        if event == UPKEY_DOWN:
            boy.y_velocity += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            boy.y_velocity -= RUN_SPEED_PPS
        if event == DOWNKEY_DOWN:
            boy.y_velocity += RUN_SPEED_PPS
            boy.y_velocity -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            boy.y_velocity += RUN_SPEED_PPS



    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * gf.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.x_velocity * gf.frame_time
        boy.y += boy.y_velocity * gf.frame_time

        boy.x = clamp(boy.canvas_width//2, boy.x , boy.bg.w - boy.canvas_width//2)
        boy.y = clamp(boy.canvas_height // 2, boy.y , boy.by.h - boy.canvas_height // 2)


    @staticmethod
    def draw(boy):
        cx,cy = boy.canvas_width//2 , boy.canvas_height//2

        if boy.x_velocity > 0:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, cx, cy)
            boy.dir = 1
        elif boy.x_velocity < 0:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, cx, cy)
            boy.dir = -1
        else:
            # if boy x_velocity == 0
            if boy.y_velocity > 0 or boy.y_velocity < 0:
                if boy.dir == 1:
                    boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, cx, cy)
                else:
                    boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, cx, cy)
            else:
                # boy is idle
                if boy.dir == 1:
                    boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, cx, cy)
                else:
                    boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, cx, cy)


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}






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
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    def get_bb(self):
        return self.x - 30 , self.y -30, self.x+30, self.y+ 30

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.canvas_width//2 - 60, self.canvas_height//2 + 50, '(%5d, %5d)' % (self.x, self.y), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


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

#    for i in range(8):
#        for j in range(4):
#            boxs.append(Box(i*100+50,j*100+50))
#    boy = Boy()
#    ground  = Ground()

#def exit():
#	pass

def draw():
    global boy,boxs,ground
    clear_canvas()
    clear_canvas()
#    ground.draw()
#    boy.draw()
#    for j in boxs:
#        j.draw()



    update_canvas()

def update():
    pass
#    global boy,boxs,ground
#    boy.update()
#    for b in boxs:
#        if isCollider(boy,b):
#            #print(b.x,b.y)
#            boxs.remove(b)

    delay(0.03)


def handle_events(self,event):
    if (event.type, event.key) in key_event_table:
        key_event = key_event_table[(event.type, event.key)]
        self.add_event(key_event)


def pause():
	pass

def resume():
	pass


def exit():
    pass






if __name__ == '__main__':
    import sys
    glCurrentModule = sys.modules[__name__]
    open_canvas()
    gf.run(glCurrentModule)
    close_canvas()
