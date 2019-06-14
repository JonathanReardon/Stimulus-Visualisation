#!/usr/bin/python3
from psychopy import visual, core, gui, event

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
        """Create visual components of the fixation"""
        self.circle=visual.Circle(win,radius=.5, edges=32, fillColor='white') 
        self.circle2=visual.Circle(win,radius=.1, edges=32, fillColor='white') 
        self.linev = visual.Line(win, start=(0,.8), end=(0,-.8), lineWidth=6, lineColor='black') 
        self.lineh = visual.Line(win, start=(.8,0), end=(-.8,0),
        lineWidth=6, lineColor='black') 
        
        self.components = [self.circle,self.linev,self.lineh, self.circle2] 

    def draw(self): 
        """Draw all components of the fixation on the screen.""" 
        [component.draw() for component in self.components] 

triangle1 = visual.ShapeStim(win, units = 'deg', vertices = ((grid1),(grid3),(grid2)) , lineColor='white', fillColor='white')

triangle2 = visual.ShapeStim(win, units = 'deg', vertices = ((grid4),(grid6),(grid5)) , lineColor='white', fillColor='white')

triangle3 = visual.ShapeStim(win, units = 'deg', vertices = ((grid7),(grid9),(grid8)) , lineColor='white', fillColor='white')

triangle4 = visual.ShapeStim(win, units = 'deg', vertices = ((grid10),(grid12),(grid11)) , lineColor='white', fillColor='white')

        
class Line1(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid13),(grid14)) , lineColor='green')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Line2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid15),(grid16)) , lineColor='green')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Line3(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid17),(grid18)) , lineColor='green')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Line4(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid19),(grid20)) , lineColor='green')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Line5(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((horiz_lineA),(horiz_lineB)) , lineColor='blue')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Line6(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((vert_lineA),(vert_lineB)) , lineColor='blue')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer1(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer1), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer2), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
       
class Main1(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid1), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid2), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main3(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid3), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer3(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer3), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer4(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer4), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main4(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid4), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main5(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid5), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main6(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid6), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
       
class Outer5(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer5), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer6(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer6), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main7(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid7), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main8(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid8), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main9(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid9), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main10(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid10), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main11(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid11), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main12(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid12), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer7(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer7), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer8(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer8), radius=circle_rad, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
       
fix=Fixation()

line1 = Line1()
line2 = Line2()
line3 = Line3()
line4 = Line4()
line5 = Line5()
line6 = Line6()
outer1= Outer1()
outer2= Outer2()
main1 = Main1()
main2 = Main2()
main3 = Main3()
outer3 = Outer3()
outer4 = Outer4()
main4 = Main4()
main5 = Main5()
main6 = Main6()
outer5 = Outer5()
outer6 = Outer6()
main7 = Main7()
main8 = Main8()
main9 = Main9()
outer7 = Outer7()
outer8 = Outer8()

main10 = Main10()
main11 = Main11()
main12 = Main12()

running = True

while running:
    
    allKeys = event.getKeys(keyList = ('q'))
    
    line1.draw()
    line2.draw()
    line3.draw()
    line4.draw()
    line5.draw()
    line6.draw()
    outer1.draw()
    outer2.draw()
    main1.draw()
    main2.draw()
    main3.draw()
    outer3.draw()
    outer4.draw()
    main4.draw()
    main5.draw()
    main6.draw()
    outer5.draw()
    outer6.draw()
    main7.draw()
    main8.draw()
    main9.draw()
    outer7.draw()
    outer8.draw()
    
    main10.draw()
    main11.draw()
    main12.draw()
    fix.draw()

    triangle1.draw()
    triangle2.draw()
    triangle3.draw()
    triangle4.draw()
    
    circle4deg.draw()
    circle6deg.draw()
    win.flip()
    
   
    for thisKey in allKeys:
        if thisKey == 'q':
            window.close()
            core.quit()
                    
win.close()
