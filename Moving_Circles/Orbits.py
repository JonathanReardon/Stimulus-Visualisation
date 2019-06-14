#!/usr/bin/python3

from psychopy import visual, core, event, sound
import random
import matplotlib.pyplot as plt
import math

win = visual.Window([1000,800],color=(0,0,0), colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False, screen=2)

refresh_rate = 60.0
stim_dur = 10

frames = stim_dur * refresh_rate
frames = int(frames)


def pol_to_cart(distance, angle, x_origin=0, y_origin=0):

    x=distance*math.cos(math.radians(angle))
    y=distance*math.sin(math.radians(angle))

    return x +x_origin, y + y_origin
    
# left most lines to left circle
    
zdots = 41
zdot_list = []
j=(-8)
for i in range(zdots):
    
    angle=0
    
    line_cart = pol_to_cart(j, angle)
    dotx = line_cart[0]
    doty = line_cart[1]
    zdot_list.append([dotx, doty])
    
    j += .2
    
print(zdot_list)

linea = visual.Line(win, start=(zdot_list[0]), end=(4,0), lineColor="white")
lineb = visual.Line(win, start=(zdot_list[1]), end=(4,0), lineColor="white")
linec = visual.Line(win, start=(zdot_list[2]), end=(4,0), lineColor="white")
lined = visual.Line(win, start=(zdot_list[3]), end=(4,0), lineColor="white")
linee = visual.Line(win, start=(zdot_list[4]), end=(4,0), lineColor="white")
linef = visual.Line(win, start=(zdot_list[5]), end=(4,0), lineColor="white")
lineg = visual.Line(win, start=(zdot_list[6]), end=(4,0), lineColor="white")
lineh = visual.Line(win, start=(zdot_list[7]), end=(4,0), lineColor="white")
linei = visual.Line(win, start=(zdot_list[8]), end=(4,0), lineColor="white")
linej = visual.Line(win, start=(zdot_list[9]), end=(4,0), lineColor="white")
linek = visual.Line(win, start=(zdot_list[10]), end=(4,0), lineColor="white")
linel = visual.Line(win, start=(zdot_list[11]), end=(4,0), lineColor="white")
linem = visual.Line(win, start=(zdot_list[12]), end=(4,0), lineColor="white")
linen = visual.Line(win, start=(zdot_list[13]), end=(4,0), lineColor="white")
lineo = visual.Line(win, start=(zdot_list[14]), end=(4,0), lineColor="white")
linep = visual.Line(win, start=(zdot_list[15]), end=(4,0), lineColor="white")
lineq = visual.Line(win, start=(zdot_list[16]), end=(4,0), lineColor="white")
liner = visual.Line(win, start=(zdot_list[17]), end=(4,0), lineColor="white")
lines = visual.Line(win, start=(zdot_list[18]), end=(4,0), lineColor="white")
linet = visual.Line(win, start=(zdot_list[19]), end=(4,0), lineColor="white")
lineu = visual.Line(win, start=(zdot_list[20]), end=(4,0), lineColor="white")
linev = visual.Line(win, start=(zdot_list[21]), end=(4,0), lineColor="white")
linew = visual.Line(win, start=(zdot_list[22]), end=(4,0), lineColor="white")
linex = visual.Line(win, start=(zdot_list[23]), end=(4,0), lineColor="white")
liney = visual.Line(win, start=(zdot_list[24]), end=(4,0), lineColor="white")
linez = visual.Line(win, start=(zdot_list[25]), end=(4,0), lineColor="white")
lineaa = visual.Line(win, start=(zdot_list[26]), end=(4,0), lineColor="white")
linebb = visual.Line(win, start=(zdot_list[27]), end=(4,0), lineColor="white")
linecc = visual.Line(win, start=(zdot_list[28]), end=(4,0), lineColor="white")
linedd = visual.Line(win, start=(zdot_list[29]), end=(4,0), lineColor="white")
lineee = visual.Line(win, start=(zdot_list[30]), end=(4,0), lineColor="white")
lineff = visual.Line(win, start=(zdot_list[31]), end=(4,0), lineColor="white")
linegg = visual.Line(win, start=(zdot_list[32]), end=(4,0), lineColor="white")
linehh = visual.Line(win, start=(zdot_list[33]), end=(4,0), lineColor="white")
lineii = visual.Line(win, start=(zdot_list[34]), end=(4,0), lineColor="white")
linejj = visual.Line(win, start=(zdot_list[35]), end=(4,0), lineColor="white")
linekk = visual.Line(win, start=(zdot_list[36]), end=(4,0), lineColor="white")
linell = visual.Line(win, start=(zdot_list[37]), end=(4,0), lineColor="white")
linemm = visual.Line(win, start=(zdot_list[38]), end=(4,0), lineColor="white")
linenn = visual.Line(win, start=(zdot_list[39]), end=(4,0), lineColor="white")
lineoo = visual.Line(win, start=(zdot_list[40]), end=(4,0), lineColor="white")

left_lines = [linea, lineb, linec, lined, linee, linef, lineg, lineh, linei, linej, linek,
             linel, linem, linen, lineo, linep, lineq, liner, lines, linet, lineu, linev,
             linew, linex, liney, linez, lineaa, linebb, linecc, linedd, lineee, lineff,
             linegg, linehh, lineii, linejj, linekk, linell, linemm, linenn, lineoo]
             
print(len(left_lines))

circle  = visual.Circle(win, units = 'deg', radius=.5, fillColor="violet", interpolate=True)
circle2 = visual.Circle(win, units = 'deg', radius=.5, fillColor="purple", interpolate=True)
circle3 = visual.Circle(win, units = 'deg', radius=.5, fillColor="orange", interpolate=True)
circle4 = visual.Circle(win, units = 'deg', radius=.5, fillColor="white",  interpolate=True)

fix = visual.Circle(win, units = 'deg', radius=.1, lineWidth=0, lineColor='black', fillColor="black", pos=(0,0))

circles = [circle, circle2, circle3]

circle4deg         = visual.Circle(win, units = 'deg', radius=4, pos=(0,0),  fillColor="red",    opacity= 1, interpolate=True)
circle4deg_2       = visual.Circle(win, units = 'deg', radius=4, pos=(4,0),  fillColor="blue",   opacity=.7, interpolate=True)
circle4deg_minus2  = visual.Circle(win, units = 'deg', radius=4, pos=(-4,0), fillColor="blue",   opacity= 1, interpolate=True)
circle6deg         = visual.Circle(win, units = 'deg', radius=6, pos=(0,0),  fillColor="yellow", opacity= 1, interpolate=True)

line = visual.Line(win, start=(0,0), end=(4,0), lineColor="white")
line2 = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white")
line3 = visual.Line(win, start=(4,0), end=(4,0), lineColor="white")

line4 = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white")

line_connect = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white")

angle  = 0
angle2 = 0
angle3 = 0
angle4 = 0

running = True
while running == True:
    
    dots  = []
    dots2 = []
    dots3 = []
    dots4 = []

    n_dots = 360*100
    
    for i in range(n_dots):
        
        cart  = pol_to_cart(4, angle, -4, 0)
        cart2 = pol_to_cart(4, angle2, 4, 0)
        cart3 = pol_to_cart(4, angle3, 0, 0)
        cart4 = pol_to_cart(6, angle4, 0, 0)
        
        dot_x = cart[0]
        dot_y = cart[1]
        dots.append([dot_x, dot_y])
        
        dot_x2 = cart2[0]
        dot_y2 = cart2[1]
        dots2.append([dot_x2, dot_y2])
        
        dot_x2 = cart3[0]
        dot_y2 = cart3[1]
        dots3.append([dot_x2, dot_y2])
        
        dot_x2 = cart4[0]
        dot_y2 = cart4[1]
        dots4.append([dot_x2, dot_y2])
        
        angle +=4
        angle2+=6
        angle3+=2
        angle4+=1
       
    routine = True
    while routine == True:
        
        circle.pos=dots[0]
        circle2.pos=dots2[0]
        circle3.pos=dots3[0]
        circle4.pos=dots4[0]
        
        circle6deg.draw()
        circle4deg.draw()
        circle4deg_2.draw()
        circle4deg_minus2.draw()
        fix.draw()
        
        
        for line in left_lines:
            line.end=(dots[0])
            line.draw()
            
        circle.draw()
        circle2.draw()
        circle3.draw()
        circle4.draw()
        
        line.end=(dots3[0])
        line2.end=(dots[0])
        line3.end=(dots2[0])
        line4.end=(dots[0])
            
        line_connect.start=(dots2[0])
        line_connect.end=(dots3[0])
        line_connect.draw()
        
        win.getMovieFrame(buffer='back')         
        win.flip()
        
        dots.pop(0)
        dots2.pop(0)
        dots3.pop(0)
        dots4.pop(0)
        
        allKeys = event.getKeys(keyList = ('escape', 'q', 'w', 'a', 's', 'z', 'x'))
        for thisKey in allKeys:
            
            # change color
            if thisKey == 'q':
                circle.fillColor="green"
                circle2.fillColor="yellow"
            if thisKey == "w":
                circle.fillColor="indigo"
                circle2.fillColor="black"
                
            # change opacity
            if thisKey == 'a':
                for item in circles:
                    item.opacity+=.1
            if thisKey == 's':
                for item in circles:
                    item.opacity-=.1
            # change radius
            if thisKey == 'z':
                for item in circles:
                    item.radius+=.1

            if thisKey == 'x':
                for item in circles:
                    item.radius-=.1
            # quit
            if thisKey == 'escape':
                win.saveMovieFrames('orbits.gif')
                win.close()
    
win.close()
core.quit()
