from pico2d import *
import os
import random


open_canvas()

def handle_events():
    global running
    global waypoints
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == 1:
                xx = e.x 
                yy = 600 - e.y
                waypoints += [(xx,yy)]
            else:
                waypoints =[]

class Boy():
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed = random.randint(1,4)
        self.frame = random.randint(0,7)
        self.ani = load_image('../resource/run_animation.png')

    def draw(self):
        self.ani.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        
    def update(self,xx,yy):
        self.frame = (self.frame + 1)%8
        if(self.x<=xx and self.y <=yy):
            if(self.x != xx):
                self.x = self.x+self.speed
            if(self.x != yy):
                self.y = self.y +self.speed
        if(self.x<=xx and self.y >=yy):
            if(self.x != xx):
                self.x = self.x+self.speed
            if(self.x != yy):
                self.y = self.y -self.speed
        if(self.x>=xx and self.y <=yy):
            if(self.x != xx):
                self.x = self.x-self.speed
            if(self.x != yy):
                self.y = self.y +self.speed
        if(self.x >= xx and self.y >=yy):
            if(self.x != xx):
                self.x = self.x-self.speed
            if(self.x != yy):
                self.y = self.y -self.speed
    def nwaypoints(self):
        self.frame = (self.frame + 1)%8
class grass():
    def __init__(self):
        self.image = load_image('../resource/grass.png')
    def draw(self,xa,ya):
        self.image.draw(xa,ya)



grs = grass()
wayp = load_image('../resource/wp.png')
boys = [Boy() for i in range(20)]
count = 0
waypoints = []
running = True


while running:
    update_canvas()
   
    handle_events()
    if len(waypoints)>0:
        (xx,yy) = waypoints[0]
        for b in boys:
            b.update(xx,yy)
            if(b.x ==xx and b.y == yy):
                count +=1
                if(count == 20):
                    del waypoints[0]
                    count = 0
    else :
        for b in boys:
            b.nwaypoints()
    clear_canvas()
    for way in waypoints:
        wayp.draw(way[0],way[1])
    grs.draw(400,40)
    for b in boys:
        b.draw()
    update_canvas()
    delay(0.001)

close_canvas()
    
    
    
