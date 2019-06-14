from psychopy import visual, core, gui, event, sound

win = visual.Window([800,600],color=(1,1,1), colorSpace='rgb', rgb=None, allowGUI=True, monitor='testMonitor', units='deg', fullscr=False)

circle_rad = 0.9

grid1 = (0,0) 
grid2 = (2,0)
grid3 = (1, 1.732)

grida = (0,0)
gridb = (4,0)
gridc = (2, 3.46410161514)

gridd = (0+2.82,0+2.82)
gride = (1.93185165258+2.82, 0.517638090205+2.82)
gridf = (0.517638090205+2.82, 1.93185165258+2.82)

print("def", gridd, gride, gridf)

gridh = (0+2.82,0+2.82)
gridi = (3.86370330516+2.82, 1.03527618041+2.82)
gridj = (1.03527618041+2.82, 3.86370330516+2.82)

print(gridh, gridi, gridj)

grid4 = (3.5, 3.5)
grid5 = (5.431, 4.017)
grid6 = (4.017, 5.431)

grid7 = (7.36370330516, 4.5352761804099995)
grid8 = (4.5352761804099995, 7.36370330516)


circ1 = visual.Circle(win, units = 'deg', pos=(grid4), radius=circle_rad, lineColor="red", fillColor="red")
circ2 = visual.Circle(win, units = 'deg', pos=(grid5), radius=circle_rad, lineColor="red", fillColor="red")
circ3 = visual.Circle(win, units = 'deg', pos=(grid6), radius=circle_rad, lineColor="red", fillColor="red")
circ4 = visual.Circle(win, units = 'deg', pos=(grid7), radius=circle_rad, lineColor="red", fillColor="red")
circ5 = visual.Circle(win, units = 'deg', pos=(grid8), radius=circle_rad, lineColor="red", fillColor="red")


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
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((grid1),(grid3),(grid2)) , lineColor='white', fillColor='red')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Triangle2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((gridh),(gridi),(gridj)) , lineColor='white', fillColor='black', opacity=.8)
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
class Triangle3(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((gridd),(gride),(gridf)) , lineColor='white', fillColor='green')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components] 
        
       
fix=Fixation()

triangle1 = Triangle1()
triangle2 = Triangle2()
triangle3 = Triangle3()
running = True

while running:
    
    allKeys = event.getKeys(keyList = ('escape'))

    fix.draw()
    
    circ1.draw()
    circ2.draw()
    circ3.draw()
    circ4.draw()
    circ5.draw()
    
    triangle1.draw()
    triangle2.draw()
    triangle3.draw()
    
    win.flip()
    
    for thisKey in allKeys:
        if thisKey == 'escape':
            win.close()
            core.quit()
                    
win.close()
