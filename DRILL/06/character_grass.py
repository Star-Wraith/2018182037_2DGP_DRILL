from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
 x=0
    
 while(x<750):
     clear_canvas_now()
     grass.draw_now(400,30)
     character.draw_now(x,90)
     x=x+2
     delay(0.01)

 y=90
 while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y+2
    delay(0.01)
 while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x-2
    delay(0.01)
 while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y-2
    delay(0.01)  
 while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+2
    delay(0.01)
#원 그리기 
 while(y<300):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+1
    y=y+math.cos(60/360*math.pi)
    delay(0.01)
 while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x-math.cos(30/360*math.pi)
    y=y+math.cos(60/360*math.pi)
    delay(0.01)
 while(y>300):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x-math.cos(30/360*math.pi)
    y=y-math.cos(60/360*math.pi)
    delay(0.01)
 while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+math.cos(30/360*math.pi)
    y=y-math.cos(60/360*math.pi)
    delay(0.01)    
close_canvas()
