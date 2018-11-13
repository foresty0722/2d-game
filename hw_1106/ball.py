class ball:
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x , self.y = random.randint(0,1600-1),500,
        self.fall_speed = random.randint(BigBall.Min-FALL_SPEED,
                                         BigBall.MAX_FALL-SPEED)

    def get_bb(self):
        return self.x - 20 , self.y - 20 ,self.x + 20 ,self.y+ 20 
