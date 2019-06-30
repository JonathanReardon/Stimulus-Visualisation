#!/usr/bin/python3

from psychopy import visual, core, event, sound
import random
import matplotlib.pyplot as plt
import math

win = visual.Window([750,650], color=("black"), colorSpace='rgb', rgb=None, allowGUI=True, 
                    monitor='testMonitor', units='deg', fullscr=False, screen=2)
win.mouseVisible = False

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
    
multi_line_color1 = "red"
multi_line_color2 = "red"
  
linea = visual.Line(win, start=(zdot_list[0]), end=(4,0), lineColor=multi_line_color1)
lineb = visual.Line(win, start=(zdot_list[1]), end=(4,0), lineColor=multi_line_color2)
linec = visual.Line(win, start=(zdot_list[2]), end=(4,0), lineColor=multi_line_color1)
lined = visual.Line(win, start=(zdot_list[3]), end=(4,0), lineColor=multi_line_color2)
linee = visual.Line(win, start=(zdot_list[4]), end=(4,0), lineColor=multi_line_color1)
linef = visual.Line(win, start=(zdot_list[5]), end=(4,0), lineColor=multi_line_color2)
lineg = visual.Line(win, start=(zdot_list[6]), end=(4,0), lineColor=multi_line_color1)
lineh = visual.Line(win, start=(zdot_list[7]), end=(4,0), lineColor=multi_line_color2)
linei = visual.Line(win, start=(zdot_list[8]), end=(4,0), lineColor=multi_line_color1)
linej = visual.Line(win, start=(zdot_list[9]), end=(4,0), lineColor=multi_line_color2)
linek = visual.Line(win, start=(zdot_list[10]), end=(4,0), lineColor=multi_line_color1)
linel = visual.Line(win, start=(zdot_list[11]), end=(4,0), lineColor=multi_line_color2)
linem = visual.Line(win, start=(zdot_list[12]), end=(4,0), lineColor=multi_line_color1)
linen = visual.Line(win, start=(zdot_list[13]), end=(4,0), lineColor=multi_line_color2)
lineo = visual.Line(win, start=(zdot_list[14]), end=(4,0), lineColor=multi_line_color1)
linep = visual.Line(win, start=(zdot_list[15]), end=(4,0), lineColor=multi_line_color2)
lineq = visual.Line(win, start=(zdot_list[16]), end=(4,0), lineColor=multi_line_color1)
liner = visual.Line(win, start=(zdot_list[17]), end=(4,0), lineColor=multi_line_color2)
lines = visual.Line(win, start=(zdot_list[18]), end=(4,0), lineColor=multi_line_color1)
linet = visual.Line(win, start=(zdot_list[19]), end=(4,0), lineColor=multi_line_color2)
lineu = visual.Line(win, start=(zdot_list[20]), end=(4,0), lineColor=multi_line_color1)
linev = visual.Line(win, start=(zdot_list[21]), end=(4,0), lineColor=multi_line_color2)
linew = visual.Line(win, start=(zdot_list[22]), end=(4,0), lineColor=multi_line_color1)
linex = visual.Line(win, start=(zdot_list[23]), end=(4,0), lineColor=multi_line_color2)
liney = visual.Line(win, start=(zdot_list[24]), end=(4,0), lineColor=multi_line_color1)
linez = visual.Line(win, start=(zdot_list[25]), end=(4,0), lineColor=multi_line_color2)
lineaa = visual.Line(win, start=(zdot_list[26]), end=(4,0), lineColor=multi_line_color1)
linebb = visual.Line(win, start=(zdot_list[27]), end=(4,0), lineColor=multi_line_color2)
linecc = visual.Line(win, start=(zdot_list[28]), end=(4,0), lineColor=multi_line_color1)
linedd = visual.Line(win, start=(zdot_list[29]), end=(4,0), lineColor=multi_line_color2)
lineee = visual.Line(win, start=(zdot_list[30]), end=(4,0), lineColor=multi_line_color1)
lineff = visual.Line(win, start=(zdot_list[31]), end=(4,0), lineColor=multi_line_color2)
linegg = visual.Line(win, start=(zdot_list[32]), end=(4,0), lineColor=multi_line_color1)
linehh = visual.Line(win, start=(zdot_list[33]), end=(4,0), lineColor=multi_line_color2)
lineii = visual.Line(win, start=(zdot_list[34]), end=(4,0), lineColor=multi_line_color1)
linejj = visual.Line(win, start=(zdot_list[35]), end=(4,0), lineColor=multi_line_color2)
linekk = visual.Line(win, start=(zdot_list[36]), end=(4,0), lineColor=multi_line_color1)
linell = visual.Line(win, start=(zdot_list[37]), end=(4,0), lineColor=multi_line_color2)
linemm = visual.Line(win, start=(zdot_list[38]), end=(4,0), lineColor=multi_line_color1)
linenn = visual.Line(win, start=(zdot_list[39]), end=(4,0), lineColor=multi_line_color2)
lineoo = visual.Line(win, start=(zdot_list[40]), end=(4,0), lineColor=multi_line_color1)

left_lines = [linea, lineb, linec, lined, linee, linef, lineg, lineh, linei, linej, linek,
             linel, linem, linen, lineo, linep, lineq, liner, lines, linet, lineu, linev,
             linew, linex, liney, linez, lineaa, linebb, linecc, linedd, lineee, lineff,
             linegg, linehh, lineii, linejj, linekk, linell, linemm, linenn, lineoo]
             

circle  = visual.Circle(win, units = 'deg', radius=.5, fillColor="red",  interpolate=True, lineColor="black")
circle2 = visual.Circle(win, units = 'deg', radius=.5, fillColor="red",  interpolate=True, lineColor="black")
circle3 = visual.Circle(win, units = 'deg', radius=.5, fillColor="red",  interpolate=True, lineColor="black")
circle4 = visual.Circle(win, units = 'deg', radius=.5, fillColor="red",  interpolate=True, lineColor="black")

fix = visual.Circle(win, units = 'deg', radius=.1, lineWidth=0, lineColor='black', fillColor="black", pos=(0,0))

circles = [circle, circle2, circle3]

circle4deg         = visual.Circle(win, units = 'deg', radius=4, pos=(0,0),  fillColor="red", opacity= .25, interpolate=True, lineColor="red", lineWidth=2.5)
circle4deg_2       = visual.Circle(win, units = 'deg', radius=4, pos=(4,0),  fillColor="black", opacity=.65,  interpolate=True, lineColor="red", lineWidth=2.5)
circle4deg_minus2  = visual.Circle(win, units = 'deg', radius=4, pos=(-4,0), fillColor="black", opacity= .65, interpolate=True, lineColor="red", lineWidth=2.5)
circle6deg         = visual.Circle(win, units = 'deg', radius=6, pos=(0,0),  fillColor="black", opacity= 1,   interpolate=True, lineColor="red", lineWidth=2.5)

line = visual.Line(win, start=(0,0), end=(4,0),   lineColor="red")
line2 = visual.Line(win, start=(-4,0), end=(4,0), lineColor="red")
line3 = visual.Line(win, start=(4,0), end=(4,0),  lineColor="red")
line4 = visual.Line(win, start=(-4,0), end=(4,0), lineColor="red")

line_connect = visual.Line(win, start=(-4,0), end=(4,0), lineColor="red")

class Gridlines(object):
    def __init__(self):
        """create visual components"""
        self.vertline = visual.ShapeStim(win, units = 'deg', vertices = ((horiz_lineA),(horiz_lineB)) , lineColor='red',   lineWidth=3.5)
        self.hozline  = visual.ShapeStim(win, units = 'deg', vertices = ((vert_lineA),(vert_lineB)) ,   lineColor='red',   lineWidth=3.5)

        self.components = [self.vertline, self.hozline]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
        
horiz_lineA = (-18,0)
horiz_lineB = (18,0)

vert_lineA = (0,-12)
vert_lineB = (0,12)
        
gridlines = Gridlines()

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
        
        gridlines.draw()
        
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
        
        win.getMovieFrame(buffer='back') # for getting for e.g. gif         
        win.flip()
        
        dots.pop(0)
        dots2.pop(0)
        dots3.pop(0)
        dots4.pop(0)
        
        key = event.getKeys()
        # quit
        if len(key) > 0:
            win.saveMovieFrames('orbits.gif') # save frames for e.g. gif
            win.close()
            core.quit()
    
win.close()
core.quit()
