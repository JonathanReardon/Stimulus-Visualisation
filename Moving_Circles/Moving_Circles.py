from psychopy import visual, core, event, sound
import random
import matplotlib.pyplot as plt
import math

win = visual.Window([800,600],color=(0,0,0), colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False, screen=0)

refresh_rate = 60.0
stim_dur = 10

frames = stim_dur * refresh_rate
frames = int(frames)


def pol_to_cart(distance, angle, x_origin=0, y_origin=0):

    x=distance*math.cos(math.radians(angle))
    y=distance*math.sin(math.radians(angle))

    return x +x_origin, y + y_origin

circle  = visual.Circle(win, units = 'deg', radius=.5, fillColor="violet", interpolate=True)
circle2 = visual.Circle(win, units = 'deg', radius=.5, fillColor="purple", interpolate=True)
circle3 = visual.Circle(win, units = 'deg', radius=.5, fillColor="orange", interpolate=True)

fix = visual.Circle(win, units = 'deg', radius=.1, lineWidth=0, lineColor='black', fillColor="black", pos=(0,0))

circles = [circle, circle2, circle3]

circle4deg         = visual.Circle(win, units = 'deg', radius=4, pos=(0,0),  fillColor="red",  opacity=1, interpolate=True)
circle4deg_2       = visual.Circle(win, units = 'deg', radius=4, pos=(4,0),  fillColor="blue", opacity=1, interpolate=True)
circle4deg_minus2  = visual.Circle(win, units = 'deg', radius=4, pos=(-4,0), fillColor="blue", opacity=1, interpolate=True)

line = visual.Line(win, start=(0,0), end=(4,0), lineColor="white")
line2 = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white")
line3 = visual.Line(win, start=(4,0), end=(4,0), lineColor="white")

line4 = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white")

angle = 0

running = True

while running == True:
    
    dots = []
    dots2 = []
    dots3 = []

    n_dots = 360*10
    
    for i in range(n_dots):
        
        cart = pol_to_cart(4,angle, -4, 0)
        cart2 = pol_to_cart(4, angle, 4, 0)
        cart3 = pol_to_cart(4, angle, 0, 0)
        
        dot_x = cart[0]
        dot_y = cart[1]
        dots.append([dot_x, dot_y])
        
        dot_x2 = cart2[0]
        dot_y2 = cart2[1]
        dots2.append([dot_x2, dot_y2])
        
        dot_x2 = cart3[0]
        dot_y2 = cart3[1]
        dots3.append([dot_x2, dot_y2])
        
        angle +=2
       
    routine = True
    while routine == True:
        
        circle.pos=dots[0]
        circle2.pos=dots2[0]
        circle3.pos=dots3[0]
        
        circle4deg.draw()
        circle4deg_2.draw()
        circle4deg_minus2.draw()
        fix.draw()
        circle.draw()
        circle2.draw()
        circle3.draw()
        
        line.end=(dots3[0])
        line2.end=(dots[0])
        line3.end=(dots2[0])
        
        line4.end=(dots[0])
        
        line.draw()
        line2.draw()
        line3.draw()
        
        win.flip()
        
        dots.pop(0)
        dots2.pop(0)
        dots3.pop(0)
        
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
                win.close()
    
win.close()
core.quit()
