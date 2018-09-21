from pico2d import* 
import os 
  
os.getcwd() 
 
 
os.chdir('..') 
os.chdir('resource') 
os.listdir() 


def handle_events():
    global running
    global x, y
    global k
    global xx,yy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            xx = e.x
            yy = 600- e.y

global a

speed = 3 
            
open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

x, y = 800 // 2, 90
xx,yy = 800//2, 90


frame = 0

running = True

while running:
    
    grass.draw(400, 30)
    
    if(x <= xx and y <= yy):
        if(x != xx):
            x = x + speed
        if(y != yy):
            y = y + speed
    elif(x <= xx and y >= yy):
        if(x != xx):
            x = x + speed
        if(y != yy):
            y = y - speed
    elif(x >= xx and y <= yy):
        if(x != xx):
            x = x - speed
        if(y != yy):
            y = y + speed
    elif(x >= xx and y >= yy):
        if(x != xx):
            x = x - speed
        if(y != yy):
            y = y - speed
    
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    clear_canvas()

    frame = (frame + 1) % 8
    delay(0.001)
    
close_canvas()
