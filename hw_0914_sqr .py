from pico2d import*
import os
import math

os.getcwd()

os.chdir('C:\\Users\\Foresty\\2dgame')
os.listdir()

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')


x = 20
y = 90
frame = 0 
a = 770
b = 570

while(True):
    if( x <= 770 ):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100,0,100,100,x,90)
        frame = (frame+1) % 8
        x = x + 2
        update_canvas()
        delay(0.001)
        get_events()
        
    elif( y <= 570):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100,0,100,100,770,y)
        frame = (frame+1) % 8
        y = y + 2
        update_canvas()
        clear_canvas()
        delay(0.001)
        get_events()

    elif( a >= 20 ):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100,0,100,100,a,570)
        frame = (frame+1) % 8
        a = a - 2
        update_canvas()
        clear_canvas()
        delay(0.001)
        get_events()
    elif( b >= 90 ):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100,0,100,100,20,b)
        frame = (frame+1) % 8
        b = b - 2
        update_canvas()
        clear_canvas()
        delay(0.001)
        get_events()
        if(b == 90):
            x = 20
            y = 90
            a = 770
            b = 570
        



close_canvas()
