#!/usr/bin/python3
from psychopy import visual, core, gui, event
import numpy as np

import random

win = visual.Window([1000,800],color=(1,1,1), colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False)

circle_rad = .9
    
grid1 = (2.82, 2.82)
grid2 = (4.75185165258, 3.337638090205)
grid3 = (3.337638090205, 4.75185165258)

outer1 = (6.68370330516, 3.8552761804099998)
outer2 = (3.8552761804099998, 6.68370330516)

grid4 = (-2.82,2.82)
grid5 = (-4.75185165258, 3.337638090205)
grid6 = (-3.337638090205,4.75185165258)

outer3 = (-6.68370330516, 3.8552761804099998)
outer4 = (-3.8552761804099998, 6.68370330516)

grid7 = (-2.82,-2.82)
grid8 = (-4.75185165258, -3.337638090205)
grid9 = (-3.337638090205, -4.75185165258)

outer5 = (6.68370330516, -3.8552761804099998)
outer6 = (3.8552761804099998, -6.68370330516)

grid10 = (2.82, -2.82)
grid11 = (4.75185165258, -3.337638090205)
grid12 = (3.337638090205, -4.75185165258)

outer7 = (-6.68370330516, -3.8552761804099998)
outer8 = (-3.8552761804099998, -6.68370330516)

grid13 = (-3.5,3.5)
grid14 = (3.5,3.5)

grid15 = (3.5,3.5)
grid16 = (3.5,-3.5)

grid17 = (3.5,-3.5)
grid18 = (-3.5,-3.5)

grid19 = (-3.5,-3.5)
grid20 = (-3.5,3.5)

horiz_lineA = (-18,0)
horiz_lineB = (18,0)

vert_lineA = (0,-12)
vert_lineB = (0,12)

circle4deg = visual.Circle(win, units = 'deg', radius=4, lineColor='blue')
circle6deg = visual.Circle(win, units = 'deg', radius=6, lineColor='blue')

class Fixation(object): 
    def __init__(self): 
        """Create visual components of the fixation cross"""
        self.circle=visual.Circle(win,radius=.5, edges=32, fillColor='white') 
        self.circle2=visual.Circle(win,radius=.1, edges=32, fillColor='white') 
        self.linev = visual.Line(win, start=(0,.8), end=(0,-.8), lineWidth=6, lineColor='black') 
        self.lineh = visual.Line(win, start=(.8,0), end=(-.8,0), lineWidth=6, lineColor='black') 
        
        self.components = [self.circle, self.circle2, self.linev, self.lineh] 

    def draw(self): 
        """Draw all components to screen.""" 
        [component.draw() for component in self.components] 
        
tri_colors = ['white', 'blue', 'yellow', 'orange', 'green']
#random.shuffle(tri_colors)

triangle1 = visual.ShapeStim(win, units = 'deg', vertices = ((grid1),(grid3),(grid2)) ,    lineColor=tri_colors[0], fillColor=tri_colors[0])
triangle2 = visual.ShapeStim(win, units = 'deg', vertices = ((grid4),(grid6),(grid5)) ,    lineColor=tri_colors[0], fillColor=tri_colors[0])
triangle3 = visual.ShapeStim(win, units = 'deg', vertices = ((grid7),(grid9),(grid8)) ,    lineColor=tri_colors[0], fillColor=tri_colors[0])
triangle4 = visual.ShapeStim(win, units = 'deg', vertices = ((grid10),(grid12),(grid11)) , lineColor=tri_colors[0], fillColor=tri_colors[0])

triangles = [triangle1, triangle2, triangle3, triangle4]

class Green_rect(object):
    def __init__(self):
        """create visual components"""
        self.line1 = visual.ShapeStim(win, units = 'deg', vertices = ((grid13),(grid14)), lineColor='green')
        self.line2 = visual.ShapeStim(win, units = 'deg', vertices = ((grid15),(grid16)), lineColor='green')
        self.line3 = visual.ShapeStim(win, units = 'deg', vertices = ((grid17),(grid18)), lineColor='green')
        self.line4 = visual.ShapeStim(win, units = 'deg', vertices = ((grid19),(grid20)), lineColor='green')

        self.components = [self.line1, self.line2, self.line3, self.line4]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Circle_inner(object):
    def __init__(self):
        """create visual components"""
        self.bluecircle1 = visual.ShapeStim(win, units = 'deg', vertices = ((horiz_lineA),(horiz_lineB)) , lineColor='blue')
   
        self.components = [self.bluecircle1]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
        
class Circle_outer(object):
    def __init__(self):
        """create visual components"""
        self.bluecircle2 = visual.ShapeStim(win, units = 'deg', vertices = ((vert_lineA),(vert_lineB)) , lineColor='blue')
   
        self.components = [self.bluecircle2]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer1(object):
    def __init__(self):
        """create visual components"""
        self.circle1 = visual.Circle(win, units = 'deg', pos=(outer1), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle2 = visual.Circle(win, units = 'deg', pos=(outer2), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle1, self.circle2]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
       
class Main1(object):
    def __init__(self):
        """create visual components"""
        self.circle1 = visual.Circle(win, units = 'deg', pos=(grid1), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle2 = visual.Circle(win, units = 'deg', pos=(grid2), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle3 = visual.Circle(win, units = 'deg', pos=(grid3), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle1, self.circle2, self.circle3]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
        
class Outer2(object):
    def __init__(self):
        """create visual components"""
        self.circle3 = visual.Circle(win, units = 'deg', pos=(outer3), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle4 = visual.Circle(win, units = 'deg', pos=(outer4), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle3, self.circle4]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main2(object):
    def __init__(self):
        """create visual components"""
        self.circle4 = visual.Circle(win, units = 'deg', pos=(grid4), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle5 = visual.Circle(win, units = 'deg', pos=(grid5), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle6 = visual.Circle(win, units = 'deg', pos=(grid6), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle4, self.circle5, self.circle6]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
       
class Outer3(object):
    def __init__(self):
        """create visual components"""
        self.circle5 = visual.Circle(win, units = 'deg', pos=(outer5), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle6 = visual.Circle(win, units = 'deg', pos=(outer6), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle5, self.circle6]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main3(object):
    def __init__(self):
        """create visual components"""
        self.circle7 = visual.Circle(win, units = 'deg', pos=(grid7), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle8 = visual.Circle(win, units = 'deg', pos=(grid8), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle9 = visual.Circle(win, units = 'deg', pos=(grid9), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle7, self.circle8, self.circle9]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
        
class Main4(object):
    def __init__(self):
        """create visual components"""
        self.circle10 = visual.Circle(win, units = 'deg', pos=(grid10), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle11 = visual.Circle(win, units = 'deg', pos=(grid11), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle12 = visual.Circle(win, units = 'deg', pos=(grid12), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle10, self.circle11, self.circle12]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
        
class Outer4(object):
    def __init__(self):
        """create visual components"""
        self.circle7 = visual.Circle(win, units = 'deg', pos=(outer7), radius=circle_rad, lineColor="red", fillColor="red")
        self.circle8 = visual.Circle(win, units = 'deg', pos=(outer8), radius=circle_rad, lineColor="red", fillColor="red")

        self.components = [self.circle7, self.circle8]
        
    def draw(self):
        """Draw all components to screen.""" 
        [component.draw() for component in self.components]
       
fix=Fixation()

green_rect   = Green_rect()
circle_inner = Circle_inner()
circle_outer = Circle_outer()

main1 = Main1()
main2 = Main2()
main3 = Main3()
main4 = Main4()

outer1= Outer1()
outer2= Outer2()
outer3 = Outer3()
outer4 = Outer4()

misc_shapes = [green_rect, circle_inner, circle_outer]
main        = [main1, main2, main3, main4]
outer       = [outer1, outer2, outer3, outer4]

running = True
while running == True:
    
    allKeys = event.getKeys(keyList = ('q'))
    
    for shape in misc_shapes:
        shape.draw()
        
    for shape in main:
        shape.draw()
        
    for shape in outer:
        shape.draw()
        
    for triangle in triangles:
        triangle.draw()
 
    fix.draw()
    
    circle4deg.draw()
    circle6deg.draw()
    win.flip()
    
    for thisKey in allKeys:
        if thisKey == 'q':
            win.close()
            core.quit()
                    
win.close()
core.quit()
