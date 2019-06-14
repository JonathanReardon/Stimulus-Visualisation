from psychopy import visual, core, gui, event

win = visual.Window([800,600],color=(1,1,1), colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False)

grid1 = (3.5,3.5)
grid2 = (4.0125,5.625)
grid3 = (5.625,4.0125)

outer1 = (4.525, 7.75)
outer2 = (7.75, 4.525)

grid4 = (-3.5,3.5)
grid5 = (-4.0125,5.625)
grid6 = (-5.625,4.0125)

grid7 = (-3.5,-3.5)
grid8 = (-4.0125, -5.625)
grid9 = (-5.625, -4.0125)

grid10 = (3.5,-3.5)
grid11 = (4.0125, -5.625)
grid12 = (5.625, -4.0125)

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

class Triangle1(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid1),(grid3),(grid2)) , lineColor='white', fillColor='white')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Triangle2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid4),(grid6),(grid5)) , lineColor='black', fillColor='black')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Triangle3(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid7),(grid9),(grid8)) , lineColor='black', fillColor='black')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Triangle4(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid10),(grid12),(grid11)) , lineColor='black', fillColor='black')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
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
        self.circle = visual.Circle(win, units = 'deg', pos=(outer1), radius=.8, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Outer2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(outer2), radius=.8, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
       
class Main1(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid1), radius=.8, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid2), radius=.8, lineColor="red", fillColor="red")
   
        self.components = [self.circle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Main3(object):
    def __init__(self):
        """create visual components of triangle"""
        self.circle = visual.Circle(win, units = 'deg', pos=(grid3), radius=.8, lineColor="red", fillColor="red")
   
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

triangle1 = Triangle1()
triangle2 = Triangle2()
triangle3 = Triangle3()
triangle4 = Triangle4()

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
fix.draw()

triangle1.draw()
triangle2.draw()
triangle3.draw()
triangle4.draw()
win.flip()

event.waitKeys(keyList = ('escape'))

win.close()
