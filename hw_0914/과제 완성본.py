from pico2d import*
import os
import math

os.getcwd()

os.chdir('..')
os.chdir('resource')
os.listdir()

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')



def haha():
    

    
    x = 20 
    y = 90
    frame = 0 
    a = 770
    b = 570
    while(True):
        if( x <= 770 ):
            grass.draw(400,30)
            character.clip_draw(frame * 100,0,100,100,x,90)
            frame = (frame+1) % 8
            x = x + 2
            update_canvas()
            clear_canvas()
            delay(0.002)
       
        elif( y <= 570):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100,0,100,100,770,y)
            frame = (frame+1) % 8
            y = y + 2
            update_canvas()
            clear_canvas()
            delay(0.002)
  

        elif( a >= 20 ):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100,0,100,100,a,570)
            frame = (frame+1) % 8
            a = a - 2
            update_canvas()
            clear_canvas()
            delay(0.002)
  
        elif( b >= 90 ):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100,0,100,100,20,b)
            frame = (frame+1) % 8
            b = b - 2
            update_canvas()
            clear_canvas()
            delay(0.002)
            if( b < 90):
                return
  
       
  
def round():
    
    global rz
    global rx
    global ry
    global r
    global frame

    abc = 400 

    abcy = 330
    frame = 0 
    rz = 0
    
    rx = 0

    ry = 0

    r = 250 

    while(rz<360):
        grass.draw(400,30)
        character.clip_draw(frame * 100,0,100,100,rx,ry)
        frame = (frame+1) % 8
        rz = rz + 5
        ry = math.sin(math.radians(rz))  * r + abcy
        rx = math.cos(math.radians(rz)) * r + abc
        update_canvas()
        clear_canvas()
        delay(0.02)
        if(rz == 360):
            return


i = 1


for i in range(1,10):
    haha()
    round()
