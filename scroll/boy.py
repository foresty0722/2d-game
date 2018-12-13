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
        boy.frame = 0
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 8 * game_world.ACTION_PER_TIME * game_world.frame_time) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.src_y = 200
        elif boy.dir == 2:
            boy.src_y = 300

        Boy.image.clip_draw(int(boy.frame) * 100, boy.src_y, 100, 100, boy.x,boy.y)
#        Boy.image.clip_draw(boy.fram e * 100, y, 100, 100, *boy.pos())
    def get_bb(self):
        return (self.x - 40, self.y - 40, self.x + 40, self.y + 40)


class RunState:
    MARGIN = 25
    @staticmethod
    def enter(boy):
        boy.time = time.time()
        boy.frame = 0
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def update(boy):
        #elapsed = time.time() - boy.time
       # mag = 2 if elapsed > 2.0 else 1
        # print(mag, elapsed)
        boy.frame = (boy.frame + 8 * game_world.ACTION_PER_TIME * game_world.frame_time) % 8


    @staticmethod
    def draw(boy):
        boy.src_y = 0
        if boy.dir == 1:
            boy.src_y = 0
        elif boy.dir == 2:
            boy.src_y = 100

        Boy.image.clip_draw(int(boy.frame) * 100, boy.src_y, 100, 100, boy.x,boy.y)


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
        self.y = 300  # 손대지말기
        self.hand_image = load_image("../res/hand.png")
        self.attacking = False
        self.src_y = 0
        self.attack = False
        self.moving = False
        self.hand_frame = 0
        self.wall_touch = False
        self.speed = random.uniform(5.0, 8.0)
        self.frame = random.randint(0, 7)
        self.state = None
        self.set_state(IdleState)
        self.dir = 1        #좌우
        self.dir_up_down = 0    #상하

        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')

    def get_bb(self):
        return (self.x - 25, self.y - 30, self.x + 25, self.y + 30)

    def pos(self):
       # return self.x - self.bg.x, self.y - self.bg.y
        pass
    def draw(self):
        self.state.draw(self)
        if self.attacking:
            if self.dir == 1:
                self.hand_image.clip_draw(int(self.hand_frame) * 64, 0, 64, 64, self.x - 30, self.y)
            else : self.hand_image.clip_draw(int(self.hand_frame) * 64, 0, 64, 64, self.x + 30, self.y)
    def update(self):
        self.state.update(self)
        if self.attacking:
            self.hand_frame = (self.hand_frame + 4 * game_world.ACTION_PER_TIME * game_world.frame_time) % 5
            if self.hand_frame > 4:
                self.hand_frame = 0
                self.attacking = False
        self.collider()
    def handle_event(self):
        pass

    def set_dir(self,_dir):
        self.dir = _dir
    def collider(self):
        for i in scroll_state.boxs:
            if i.get_bb(self):
                self.wall_touch = True
                if i.x > self.x :
                    scroll_state.right_key_lock = True
                elif i.x < self.x:
                    scroll_state.left_key_lock = True
                elif i.y > self.y:
                    scroll_state.up_key_lock = True
                elif i.y < self.y:
                    scroll_state.down_key_lock = True
                return

        scroll_state.right_key_lock = False
        scroll_state.left_key_lock = False
        scroll_state.up_key_lock = False
        scroll_state.down_key_lock = False
    def dig(self):
        if self.dir == 1:
            for i in scroll_state.boxs:
                if i.x + 50 > self.x - 50 and i.y -50 < self.y and i.y + 50 > self.y:
                    i.active = False
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