from pico2d import*
import os
import math

os.getcwd()

os.chdir('C:\\Users\\Foresty\\2dgame')
os.listdir()

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

z = 0
x = 0
y = 0
r = 250 
abc = 400 
abcy = 330 
frame = 0

while(z<360):
    grass.draw(400,30)
    character.clip_draw(frame * 100,0,100,100,x,y)
    frame = (frame+1) % 8
    z = z + 5
    y = math.sin(math.radians(z))  * r + abcy
    x = math.cos(math.radians(z)) * r + abc
    update_canvas()
    clear_canvas()
    if(z == 360):
        z = 0
    delay(0.02)
    get_events()



close_canvas()
