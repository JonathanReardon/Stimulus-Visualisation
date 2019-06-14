#!/usr/bin/python3

from psychopy import visual, core, event, sound
import random
import math
from math import sqrt

#set window/mouse objects & refresh rate
win = visual.Window([1000,800], color="black", colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False, screen=2)
myMouse = event.Mouse(visible=True,win=win)

refresh_rate = 60.0
stim_dur = 10

frames = stim_dur * refresh_rate
frames = int(frames)

# input polar (distance & angle), return cartesian. x&y origin = starting point of circle 
def pol_to_cart(distance, angle, x_origin=0, y_origin=0):

    x=distance*math.cos(math.radians(angle))
    y=distance*math.sin(math.radians(angle))

    return x +x_origin, y + y_origin
    
def euclidean_distance(x1, y1, x2, y2):
    
    distance = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
    
    return distance
   
circle  = visual.Circle(win, units = 'deg', radius=.5, fillColor="violet", interpolate=True, fillColorSpace='rgb')
circle2 = visual.Circle(win, units = 'deg', radius=.5, fillColor="purple", interpolate=True, fillColorSpace='rgb')
circle3 = visual.Circle(win, units = 'deg', radius=.5, fillColor="orange", interpolate=True, fillColorSpace='rgb')
light_circle = visual.Circle(win, units = 'deg', radius=.5, fillColor="red", interpolate=True, fillColorSpace='rgb')

circles = [circle, circle2, circle3, light_circle]

fix = visual.Circle(win, units = 'deg', radius=.1, lineWidth=0, lineColor='black', fillColor="black", pos=(0,0), lineColorSpace='rgb')

circle4deg         = visual.Circle(win, units = 'deg', radius=4, pos=(0,0),  fillColor="red",  opacity=1, interpolate=True, fillColorSpace='rgb')
circle4deg_2       = visual.Circle(win, units = 'deg', radius=4, pos=(4,0),  fillColor="blue", opacity=.7, interpolate=True, fillColorSpace='rgb')
circle4deg_minus2  = visual.Circle(win, units = 'deg', radius=4, pos=(-4,0), fillColor="blue", opacity=1, interpolate=True, fillColorSpace='rgb')

# set color picker circles
green_col = visual.Circle(win, units = 'deg', radius=1, fillColor="green", interpolate=True, pos=(-2,-6), fillColorSpace='rgb')
red_col = visual.Circle(win, units = 'deg',   radius=1, fillColor="red", interpolate=True, pos=(0,-6), fillColorSpace='rgb')
orange_col = visual.Circle(win, units = 'deg',   radius=1, fillColor="orange", interpolate=True, pos=(2,-6), fillColorSpace='rgb')

light_switch = visual.Circle(win, units = 'deg',   radius=2, fillColor="yellow", interpolate=True, pos=(-8,6), fillColorSpace='rgb')
light_switch_text = visual.TextStim(win, text="Light", pos=(-8,6), color=(-1,-1,-1), colorSpace='rgb')

hello_grid = visual.Rect(win, units="deg", fillColor="black", pos=(8,6), size=6, fillColorSpace='rgb')
hello_text = visual.TextStim(win, text="Hello", pos=(8,6), color=(1,1,1), colorSpace='rgb')

# line to connect 2 rightmost moving circles
line_connect = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white", lineColorSpace='rgb')

angle = 0
angle2=0

running = True

while running == True:
    
    dots = []
    dots2 = []
    dots3 = []
    light_dots=[]

    n_dots = 360*100
    
    for i in range(n_dots):
        
        cart = pol_to_cart(4,angle, -4, 0)
        cart2 = pol_to_cart(4, angle2, 4, 0)
        cart3 = pol_to_cart(4, angle, 0, 0)
        light_cart = pol_to_cart(2, angle, -8,6)
        
        dot_x = cart[0]
        dot_y = cart[1]
        dots.append([dot_x, dot_y])
        
        dot_x2 = cart2[0]
        dot_y2 = cart2[1]
        dots2.append([dot_x2, dot_y2])
        
        dot_x2 = cart3[0]
        dot_y2 = cart3[1]
        dots3.append([dot_x2, dot_y2])
        
        dot_x = light_cart[0]
        dot_y = light_cart[1]
        light_dots.append([dot_x, dot_y])
        
        angle +=4
        angle2+=1
        
    # get left-hand circle horizontal coordinates + assign to lines
    zdots = 41
    left_hoz_list = []
    j=(-8)
    
    for i in range(zdots):
        angle=0
        line_cart = pol_to_cart(j, angle)
        left_hoz_list.append(visual.Line(win, start=([line_cart[0], line_cart[1]]), end=(8,3), lineColor="white", lineColorSpace='rgb'))
        j += .2
        
    # get left-hand circle vertical coordinates + assign to lines
    left_vert_list = []
    j1 = 0
    angle_vert = 90
    
    for i in range(zdots):
        angle=0
        line_cart1 = pol_to_cart(j1, angle_vert, -4, -4)
        left_vert_list.append(visual.Line(win, start=([line_cart1[0], line_cart1[1]]), end=(8,3), lineColor="white", lineColorSpace='rgb'))
        j1 += .2
        
    # circle1 position [right hand side]
    string="hi"
    circle1label = visual.TextStim(win, text="circle1 Position: ", pos=(9,-3), height=.75, color="white", colorSpace='rgb')
    circle1textpos = visual.TextStim(win, pos=(13,-3), height=.75, color="white", colorSpace='rgb')
        
    # circle2 position [middle]
    string="hi"
    circle2label = visual.TextStim(win, text="circle2 Position: ", pos=(9,-4), height=.75, color="white", colorSpace='rgb')
    circle2textpos = visual.TextStim(win, pos=(13,-4), height=.75, color="white", colorSpace='rgb')
    
    # light circle position
    string="hi"
    lightcirclelabel = visual.TextStim(win, text="circle2 Position: ", pos=(9,-5), height=.75, color="white", colorSpace='rgb')
    lightcircletextpos = visual.TextStim(win, pos=(13,-5), height=.75, color="white", colorSpace='rgb')
    
    # mouse object position
    string="hi"
    mouseoblabel = visual.TextStim(win, text="Mouse Position: ", pos=(9,-6), height=.75, color="white", colorSpace='rgb')
    mouseobtextpos = visual.TextStim(win, pos=(13,-6), height=.75, color="white", colorSpace='rgb')
    
    # distance between mouse object and fixation
    string="hi"
    mouse_fix_distance_label = visual.TextStim(win, text="Mouse to Fix Dist: ", pos=(9,-5.8), height=1, color="white", colorSpace='rgb')
    mouse_fix_distance_pos = visual.TextStim(win, pos=(12.7,-5.8), height=1, color="white", colorSpace='rgb')
    
    routine = True
    while routine == True:
        
        mouse_loc = myMouse.getPos()
        
        green_col.draw()
        red_col.draw()
        orange_col.draw()
        light_switch.draw()
        hello_text.draw()
        hello_grid.draw()
        light_switch_text.draw()
        
        circle.pos=mouse_loc
        
        circle2.pos=dots2[0]
        circle3.pos=dots3[0]
        light_circle.pos=(light_dots[0])
       
        circle4deg.draw()
        circle4deg_2.draw()
        circle4deg_minus2.draw()
        fix.draw()
        
        for line in left_vert_list:
            line.end=mouse_loc
            line.draw()
   
        # circle1
        string1 = str(round(dots2[0][0],2))
        string2 = str(round(dots2[0][1],2))
        string=[string1, string2]
        circle1textpos.text=(string)
        #circle1textpos.draw()
        #circle1label.color=circle2.fillColor
        #circle1label.draw()
        
        # circle2
        string3 = str(round(dots3[0][0],2))
        string4 = str(round(dots3[0][1],2))
        string=[string3, string4]
        circle2textpos.text=(string)
        #circle2textpos.draw()
        #circle2label.color=circle3.fillColor
        #circle2label.draw()
        
        # circle2
        string5 = str(round(light_dots[0][0],2))
        string6 = str(round(light_dots[0][1],2))
        string=[string5, string6]
        lightcircletextpos.text=(string)
        #lightcircletextpos.draw()
        #lightcirclelabel.color=light_circle.fillColor
        #lightcirclelabel.draw()
        
        # mouse object position
        string7 = str(round(myMouse.getPos()[0],2))
        string8 = str(round(myMouse.getPos()[1],2))
        string=[string7, string8]
        mouseobtextpos.text=(string)
        #mouseobtextpos.draw()
        #mouseoblabel.color=circle.fillColor
        #mouseoblabel.draw()
        
        mouse_fix_distance = euclidean_distance(myMouse.getPos()[0], myMouse.getPos()[1], 0, 0)
        mouse_fix_distance=round(mouse_fix_distance, 2)
        mouse_fix_distance_pos.text=(mouse_fix_distance)
        mouse_fix_distance_pos.draw()
        mouse_fix_distance_label.draw()
            
        circle.draw()
        circle2.draw()
        circle3.draw()
        light_circle.draw()
            
        line_connect.start=(dots2[0])
        line_connect.end=(dots3[0])
        line_connect.draw()
        
        for line in left_hoz_list:
            line.end=mouse_loc
            line.draw()
            
        # color picker
        if  green_col.contains(myMouse.getPos()):
            circle4deg_minus2.fillColor = "green"
            circle4deg.fillColor="green"
            circle4deg_2.fillColor="green"
            green_col.opacity=(.5)
        elif  red_col.contains(myMouse.getPos()):
            circle4deg_minus2.fillColor = "red"
            circle4deg.fillColor="red"
            circle4deg_2.fillColor="red"
            red_col.opacity=(.5)
            
        elif  orange_col.contains(myMouse.getPos()):
            circle4deg_minus2.fillColor = "orange"
            circle4deg.fillColor="orange"
            circle4deg_2.fillColor="orange"
            orange_col.opacity=(.5)
        elif light_switch.contains(myMouse.getPos()):
             win.color=(0,0,0)
             hello_grid.opacity=(.5)
            
        else:
            circle4deg_minus2.fillColor = "blue"
            circle4deg.fillColor="red"
            circle4deg_2.fillColor="blue"
            green_col.opacity=(1)
            orange_col.opacity=(1)
            red_col.opacity=(1)
            win.color=(-1,-1,-1)
            hello_grid.opacity=(1)

        # win.getMovieFrame(buffer='back') # get movie frames
        win.flip()

        dots.pop(0)
        dots2.pop(0)
        dots3.pop(0)
        light_dots.pop(0)
        
        allKeys = event.getKeys(keyList = ('escape', 'q', 'w', 'a', 's', 'z', 'x'))
        for thisKey in allKeys:
            # quit
            if thisKey == 'escape':
                # win.saveMovieFrames('orbits.gif') # save movie frames
                win.close()
                core.quit()
            # change color
            elif thisKey == 'q':
                circle.fillColor="green"
                circle2.fillColor="yellow"
            elif thisKey == "w":
                circle.fillColor="indigo"
                circle2.fillColor="black"
            # change opacity
            elif thisKey == 'a':
                for item in circles:
                    item.opacity+=.1
            elif thisKey == 's':
                for item in circles:
                    item.opacity-=.1
            # change radius
            elif thisKey == 'z':
                for item in circles:
                    item.radius+=.1
            elif thisKey == 'x':
                for item in circles:
                    item.radius-=.1
win.close()
core.quit()
