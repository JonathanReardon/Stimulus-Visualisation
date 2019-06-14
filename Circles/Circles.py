from psychopy import visual, core, event, sound
import random
import math

#set window/mouse objects & refresh rate
win = visual.Window([800,600],color=(-1,-1,-1), colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False, screen=2)
myMouse = event.Mouse(visible=True,win=win)

refresh_rate = 60.0
stim_dur = 10

frames = stim_dur * refresh_rate
frames = int(frames)

# input polar (distance & angle), output cartesian. x&y origin = starting point of circle 
def pol_to_cart(distance, angle, x_origin=0, y_origin=0):

    x=distance*math.cos(math.radians(angle))
    y=distance*math.sin(math.radians(angle))

    return x +x_origin, y + y_origin
   
circle  = visual.Circle(win, units = 'deg', radius=.5, fillColor="violet", interpolate=True)
circle2 = visual.Circle(win, units = 'deg', radius=.5, fillColor="purple", interpolate=True)
circle3 = visual.Circle(win, units = 'deg', radius=.5, fillColor="orange", interpolate=True)
light_circle = visual.Circle(win, units = 'deg', radius=.5, fillColor="red", interpolate=True)

circles = [circle, circle2, circle3, light_circle]

fix = visual.Circle(win, units = 'deg', radius=.1, lineWidth=0, lineColor='black', fillColor="black", pos=(0,0))

circle4deg         = visual.Circle(win, units = 'deg', radius=4, pos=(0,0),  fillColor="red",  opacity=1, interpolate=True)
circle4deg_2       = visual.Circle(win, units = 'deg', radius=4, pos=(4,0),  fillColor="blue", opacity=.7, interpolate=True)
circle4deg_minus2  = visual.Circle(win, units = 'deg', radius=4, pos=(-4,0), fillColor="blue", opacity=1, interpolate=True)

# set color picker circles
green_col = visual.Circle(win, units = 'deg', radius=1, fillColor="green", interpolate=True, pos=(-2,-6))
red_col = visual.Circle(win, units = 'deg',   radius=1, fillColor="red", interpolate=True, pos=(0,-6))
orange_col = visual.Circle(win, units = 'deg',   radius=1, fillColor="orange", interpolate=True, pos=(2,-6))

light_switch = visual.Circle(win, units = 'deg',   radius=2, fillColor="yellow", interpolate=True, pos=(-8,6))
light_switch_text = visual.TextStim(win, text="Light", pos=(-8,6), color=(-1,-1,-1))

hello_grid = visual.Rect(win, units="deg", fillColor="black", pos=(8,6), size=6)
hello_text = visual.TextStim(win, text="Hello", pos=(8,6), color=(1,1,1))

# line to connect 2 rightmost moving circles
line_connect = visual.Line(win, start=(-4,0), end=(4,0), lineColor="white")

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
        
        angle +=2
        angle2+=4
        
        
    # get left-hand circle horizontal coordinates + assign to lines
    zdots = 41
    left_hoz_list = []
    j=(-8)
    
    for i in range(zdots):
        angle=0
        line_cart = pol_to_cart(j, angle)
        left_hoz_list.append(visual.Line(win, start=([line_cart[0], line_cart[1]]), end=(8,3), lineColor="white"))
        j += .2
        
    # get left-hand circle vertical coordinates + assign to lines
    left_vert_list = []
    j1 = 0
    angle_vert = 90
    
    for i in range(zdots):
        angle=0
        line_cart1 = pol_to_cart(j1, angle_vert, -4, -4)
        left_vert_list.append(visual.Line(win, start=([line_cart1[0], line_cart1[1]]), end=(8,3), lineColor="white"))
        j1 += .2
        
        
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

        win.flip()
        
        dots.pop(0)
        dots2.pop(0)
        dots3.pop(0)
        light_dots.pop(0)
        
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
