#!/usr/bin/env python3

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
#circle_colors = ["black", "red"]

tracking_circle_width=4
circle_connector_line_Width=3

center_circle = visual.Circle(win, units = 'deg', radius=.7, fillColor="black", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

circle1  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle2  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle3  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')
circle4  = visual.Circle(win, units = 'deg', radius=.7, fillColor="blue", interpolate=True, fillColorSpace='rgb')

circle1_track  = visual.Circle(win, units = 'deg', radius=6, lineColor="white", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)
circle2_track  = visual.Circle(win, units = 'deg', radius=4, lineColor="black", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)
circle3_track  = visual.Circle(win, units = 'deg', radius=3, lineColor="white", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)
circle4_track  = visual.Circle(win, units = 'deg', radius=2, lineColor="black", interpolate=True, fillColorSpace='rgb', lineWidth=tracking_circle_width)

tracks  = [center_circle, circle1_track, circle2_track, circle3_track,  circle4_track]
circles = [circle1, circle2, circle3, circle4]

line_color="red"
line_connector1 = visual.Line(win, start=(-4,0), end=(4,0), lineColor=line_color, lineColorSpace='rgb', lineWidth=circle_connector_line_Width)
line_connector2 = visual.Line(win, start=(-4,0), end=(4,0), lineColor=line_color, lineColorSpace='rgb', lineWidth=circle_connector_line_Width)
line_connector3 = visual.Line(win, start=(-4,0), end=(4,0), lineColor=line_color, lineColorSpace='rgb', lineWidth=circle_connector_line_Width)
lines           = [line_connector1, line_connector2, line_connector3]

circle1_position, circle2_position, circle3_position, circle4_position = [], [], [], []
angle=0
n_dots = 360*2
    
''' circle positions '''
for i in range(n_dots):
    circle1_position.append(pol_to_cart(6,angle, 0, 0))
    circle2_position.append(pol_to_cart(4,angle, 0, 0))
    circle3_position.append(pol_to_cart(3,angle, 0, 0))
    circle4_position.append(pol_to_cart(2,angle, 0, 0))
    angle+=4

''' main routine '''
routine = True
while routine == True:
    
    if len(circle1_position) == 0:
        break
    
    Rect.pos = [rect_x, rect_y]
    Rect.draw()
    
    circle1.pos=circle1_position[0]
    circle2.pos=circle2_position[-1]
    circle3.pos=circle3_position[0]
    circle4.pos=circle4_position[-1]
    
    line_connector1.start = circle1.pos
    line_connector1.end = circle2.pos
    
    line_connector2.start = circle2.pos
    line_connector2.end = circle3.pos
    
    line_connector3.start = circle3.pos
    line_connector3.end = circle4.pos
 
    for track in tracks:
        track.draw()
    for circle in circles:
        circle.fillColor=random.choice(circle_colors)
        circle.draw()
    for line in lines:
        line.draw()
   
    #win.getMovieFrame(buffer='back')
    win.flip()
    
    circle1_position.pop(0)
    circle2_position.pop(-1)
    circle3_position.pop(0)
    circle4_position.pop(-1)
    
    rect_x = rect_x+.012

#win.saveMovieFrames('orbit_block.gif')
win.close()
core.quit()
    
