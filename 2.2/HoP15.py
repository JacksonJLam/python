#HoP15.py
#Jackson Lambet 1-3-19
#draws a simple face of the given size in win
from graphics import *
import math

def drawFace(center, size, win):
    #Drawing circles and ovals relative to the size of the face
    Circle(Point(center.getX(),center.getY()), size).draw(win)
    i1 = Circle(Point(center.getX() - (size / 3) , center.getY() - (size / 4)), size / 5)
    i1.setFill("white")
    i2 = Circle(Point(center.getX() + (size / 3) , center.getY() - (size / 4)), size / 5)
    i2.setFill("white")
    in1 = Circle(Point(center.getX() - (size / 3) , center.getY() - (size / 4)), size / 10)
    in1.setFill("brown")
    in2 = Circle(Point(center.getX() + (size / 3) , center.getY() - (size / 4)), size / 10)
    in2.setFill("brown")
    p1 = Circle(Point(center.getX() - (size / 3) , center.getY() - (size / 4)), size / 24)
    p1.setFill("black")
    p2 = Circle(Point(center.getX() + (size / 3) , center.getY() - (size / 4)), size / 24)
    p2.setFill("black")
    mouth = Oval(Point(center.getX() + (size / 1.5) , center.getY() + (size / 6)), Point(center.getX() - (size / 1.5) , center.getY() + (size / 2)))
    mouth.setFill("black")
    i1.draw(win)
    i2.draw(win)
    in1.draw(win)
    in2.draw(win)
    p1.draw(win)
    p2.draw(win)
    mouth.draw(win)
                
        
def main() :
    print("This script draws 10 faces depending on where you click")
    win = GraphWin('Faces', 500,500)
    #Loops each time to get the values for parameters center and size
    for i in range(6) :
        txt1 = Text(Point(200,30), "Your first click will decide the center point").draw(win)
        center = win.getMouse()
        p = Circle(Point(center.getX(),center.getY()), 2).draw(win)
        txt1.undraw()
        txt2 = Text(Point(200,30), "Your next click will choose the size.").draw(win) 
        radius = win.getMouse()
        #Formula to find length between two points to get the size
        size = float(math.sqrt((center.getX()-radius.getX())**2 + (center.getY()-radius.getY())**2))
        p.undraw()
        txt2.undraw()
        drawFace(center,size,win)
    #exit interface   
    txt1 = Text(Point(200,30), "Click Twice to exit").draw(win)
    win.getMouse()
    win.getMouse()
    win.close()
        
main()
