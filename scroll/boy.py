from pico2d import *
import random
import time
import game_world
import box
import scroll_state


class IdleState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8
        elapsed = time.time() - boy.time
        if elapsed > 10.0:
            boy.set_state(SleepState)
    @staticmethod
    def draw(boy):
        if boy.src_y == 100:
            boy.src_y = 300
        elif boy.src_y == 0:
            boy.src_y = 200
        if boy.dir == 1:
            boy.src_y = 200
        elif boy.dir == 2:
            boy.src_y = 300

        Boy.image.clip_draw(boy.frame * 100, boy.src_y, 100, 100, boy.x,boy.y)
#        Boy.image.clip_draw(boy.fram e * 100, y, 100, 100, *boy.pos())
    def get_bb(self):
        return (self.x - 40, self.y - 40, self.x + 40, self.y + 40)


class RunState:
    MARGIN = 25
    @staticmethod
    def enter(boy):
        boy.time = time.time()
    @staticmethod
    def exit(boy):
        boy.src_y = 200
    @staticmethod
    def update(boy):
        #elapsed = time.time() - boy.time
       # mag = 2 if elapsed > 2.0 else 1
        # print(mag, elapsed)
        boy.frame = (boy.frame + 1) % 8
    #    boy.x = boy.x + mag * boy.mag * boy.dx
    #    boy.y = boy.y + mag * boy.mag * boy.dy

        #if hasattr(boy.bg, 'clamp'):
         #   boy.bg.clamp(boy)

    @staticmethod
    def draw(boy):
        boy.src_y = 0
        if boy.dir == 1:
            boy.src_y = 0
        elif boy.dir == 2:
            boy.src_y = 100
        Boy.image.clip_draw(boy.frame * 100, boy.src_y, 100, 100, boy.x,boy.y)

class SleepState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        pass
    #    if boy.dir == 1:
    #        y, mx, angle = 300, -25, 3.141592/2
   #     else:
    #        y, mx, angle = 200, +25, -3.141592/2
#        x, y = boy.pos()
    #    Boy.image.clip_composite_draw(boy.frame * 100, y, 100, 100,
      #      angle, '', x + mx, y - 25, 100, 100)


okay_right = False
okay_left = False
okay_up = False
okay_down = False


class Boy:
    image = None

    def __init__(self):
        global okay_right, okay_left, okay_up, okay_down
        print("Creating..")
        self.x = 400
        self.src_y = 0
        self.attack = False
        self.moving = False
        self.Okay_right = okay_right
        self.Okay_up = okay_up
        self.Okay_left = okay_left
        self.Okay_down = okay_down
        # self.y = random.randint(90, 550)
        self.y = 300#손대지말기
        self.speed = random.uniform(5.0, 8.0)
        self.frame = random.randint(0, 7)
        self.state = None
        self.set_state(IdleState)
        self.dir = 1
        self.dx = 0
        self.dy = 0
        self.mag = 1
        self.isRun = False
        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')

    def get_bb(self):
        return (self.x - 25, self.y - 30, self.x + 25, self.y + 30)

    def pos(self):
       # return self.x - self.bg.x, self.y - self.bg.y
        pass
    def draw(self):
        self.state.draw(self)

    def update(self):
        self.state.update(self)

    def handle_event(self,e):
        if e.type == SDL_KEYDOWN:
            #print("test")
            self.isRun = True
            if e.key == SDLK_RIGHT:
                self.dx = 1
                box.dir = 2
            elif e.key == SDLK_LEFT:
                self.dx = -1
                box.dir = 1
            elif e.key == SDLK_UP:
                self.dy = 1
                box.dir = 3
            elif e.key == SDLK_DOWN:
                self.dy = -1
                box.dir = 4
            else : box.dir = 0

        elif e.type == SDL_KEYUP:

            self.isRun = False
            self.dx, self.dy = 0, 0

    def set_dir(self,_dir):
        self.dir = _dir


        # if (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHT):
        #     self.dx += self.speed
        #
        #     for i in scroll_state.boxs:
        #         i.b_dir = 1
        #     if self.dx > 0: self.dir = 1
        # elif (e.type, e.key) == (SDL_KEYUP, SDLK_RIGHT):
        #
        #     self.dx -= self.speed
        #     for i in scroll_state.boxs:
        #         i.b_dir = 2
        #     if self.dx < 0: self.dir = 0
        #
        # elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
        #     self.dx -= self.speed
        #     if self.dx < 0: self.dir = 0
        # elif (e.type, e.key) == (SDL_KEYUP, SDLK_LEFT):
        #     self.dx += self.speed
        #     if self.dx > 0: self.dir = 1
        #
        # elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_UP):
        #     self.isRun = True
        #     self.dy += self.speed
        # elif (e.type, e.key) == (SDL_KEYUP, SDLK_UP):
        #     self.isRun = False
        #     self.dy -= self.speed
        # elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_DOWN):
        #     self.isRun = True
        #     self.dy -= self.speed
        # elif (e.type, e.key) == (SDL_KEYUP, SDLK_DOWN):
        #     self.isRun = False
        #     self.dy += self.speed
        #
        # elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LSHIFT):
        #     self.mag = 2.0
        # elif (e.type, e.key) == (SDL_KEYUP, SDLK_LSHIFT):
        #     self.mag = 1.0




        self.set_state(IdleState if self.dx == 0 and self.dy == 0 else RunState)
       # for i in scroll_state.boxs:
       #     print("box : ",i.x, i.y,i.dir)


    def set_state(self, state):
        if self.state == state: return

        if self.state and self.state.exit:
            self.state.exit(self)

        self.state = state

        if self.state.enter:
            self.state.enter(self)



    # def fire_ball(self, big):
    #     mag = 1.5 if self.dir == 1 else -1.5
    #     ballSpeed = mag * self.speed + self.dx

    #     ySpeed = 2 * self.speed * (1 + random.random())
    #     if big: ySpeed *= 0.75
    #     ball = Ball(big, self.x, self.y, ballSpeed, ySpeed)
    #     game_world.add_object(ball, game_world.layer_obstacle)
