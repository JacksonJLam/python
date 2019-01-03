#HoP17.py
#moving circle
#Jackson Lambert 1-3-19
from graphics import *

win = GraphWin("Circles!", 500,500)
def moveTo(shape, newCenter) :
        c = shape.getCenter()
        #getting the value to move the circles to
        dx = newCenter.getX() - c.getX()
        dy = newCenter.getY() - c.getY()
        #set it to a global so main can undraw it 
        global shapeCopy
        shapeCopy = shape.clone()
        shapeCopy.move(dx,dy)
        shapeCopy.draw(win)
        shape.undraw()
        
    
def main() :
    print("This script will move a circle upon user mouse click")
    #loop it 10 times
    for i in range (10) :
        txt1 = Text(Point(250,100), "click somwhere to move the circle").draw(win)
        txt1.undraw()
        newCenter = win.getMouse()
        #undraw shape copy only after its been set
        if i > 0 :
            shapeCopy.undraw()
        shape = Circle(Point(newCenter.getX(), newCenter.getY()), 20)
        moveTo(shape, newCenter)
       
main()
        
        
    
