#!/usr/bin/python3

from psychopy import visual, core, event, sound
import random
import math
from math import sqrt

win = visual.Window([700,600], color="white", colorSpace='rgb', rgb=None, allowGUI=True, 
                     monitor='testMonitor', units='deg', fullscr=False, screen=2)
win.mouseVisible = False

rect_x, rect_y = [-5,0]
Rect = visual.Rect(win, width=10, height=14, fillColor="black", pos=(rect_x, rect_y), units="deg")

def pol_to_cart(distance, angle, x_origin=0, y_origin=0):
    x=distance*math.cos(math.radians(angle))
    y=distance*math.sin(math.radians(angle))
    return x +x_origin, y + y_origin
    
def euclidean_distance(x1, y1, x2, y2):
    distance = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
    return distance
    
circle_colors = ["red", "green", "orange", "blue", "violet"]
#circle_colors = ["black", "white"]

tracking_circle_width=4
circle_connector_line_Width=3

center_circle = visual.Circle(win, units = 'deg', radius=.7, fillColor="black", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

circle  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle_outline  = visual.Circle(win, units = 'deg', radius=6, lineColor="white", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

circle1  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle1_outline  = visual.Circle(win, units = 'deg', radius=4, lineColor="black", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

circle2  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle2_outline  = visual.Circle(win, units = 'deg', radius=3, lineColor="white", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

circle3  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle3_outline  = visual.Circle(win, units = 'deg', radius=2, lineColor="black", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

line_color="red"
line_connector = visual.Line(win, start=(-4,0), end=(4,0), lineColor=line_color, lineColorSpace='rgb', lineWidth=circle_connector_line_Width)
line_connector1 = visual.Line(win, start=(-4,0), end=(4,0), lineColor=line_color, lineColorSpace='rgb', lineWidth=circle_connector_line_Width)
line_connector2 = visual.Line(win, start=(-4,0), end=(4,0), lineColor=line_color, lineColorSpace='rgb', lineWidth=circle_connector_line_Width)

''' circle '''
circle_position = []
angle=0
n_dots = 360*2
    
for i in range(n_dots):
    
    circle_position.append(pol_to_cart(6,angle, 0, 0))
    angle+=4

''' circle1 '''
circle1_position = []
angle=0
n_dots = 360*2
    
for i in range(n_dots):
        
    circle1_position.append(pol_to_cart(4,angle, 0, 0))
    angle+=4
    
''' circle2 '''
circle2_position = []
angle=0
n_dots = 360*2
    
for i in range(n_dots):
        
    circle2_position.append(pol_to_cart(3,angle, 0, 0))
    angle+=4
    
''' circle3 '''
circle3_position = []
angle=0
n_dots = 360*2
    
for i in range(n_dots):
        
    circle3_position.append(pol_to_cart(2,angle, 0, 0))
    angle+=4
    
routine = True
while routine == True:
    
    if len(circle_position) == 0:
        break
    
    Rect.pos = [rect_x, rect_y]
    Rect.draw()
    
    circle.pos=circle_position[0]
    circle1.pos=circle1_position[-1]
    circle2.pos=circle2_position[0]
    circle3.pos=circle3_position[-1]
    
    circle.fillColor=random.choice(circle_colors)
    circle1.fillColor=random.choice(circle_colors)
    circle2.fillColor=random.choice(circle_colors)
    circle3.fillColor=random.choice(circle_colors)
    
    line_connector.start = circle.pos
    line_connector.end = circle1.pos
    
    line_connector1.start = circle1.pos
    line_connector1.end = circle2.pos
    
    line_connector2.start = circle2.pos
    line_connector2.end = circle3.pos
    
    center_circle.draw()
    
    circle_outline.draw()
    circle.draw()
    
    circle1_outline.draw()
    circle1.draw()
    
    circle2_outline.draw()
    circle2.draw()
    
    circle3_outline.draw()
    circle3.draw()
    
    line_connector.draw()
    line_connector1.draw()
    line_connector2.draw()
   
    #win.getMovieFrame(buffer='back')
    win.flip()
    
    circle_position.pop(0)
    circle1_position.pop(-1)
    circle2_position.pop(0)
    circle3_position.pop(-1)
    
    rect_x = rect_x+.012

#win.saveMovieFrames('orbit_block.gif')
win.close()
core.quit()
    
