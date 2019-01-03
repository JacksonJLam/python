#HoP16.py
#Photo anonymizer
#Jackson Lambert 1-3-19
from graphics import *
import math
def drawFace(center, size, win):
    #Drawing circles and ovals relative to the size of the face
    head = Circle(Point(center.getX(),center.getY()), size).draw(win)
    head.setFill("tan")
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
    print("Your first click in the graphing box will be the center of the faace")
    print("The seocnd will be the size of the circle")
    print("once all the faces are drawn, double click to exit")
    pic = input("Enter a picture filename: ")
    loops = eval(input("How many faces do you want to cover?"))
    image = Image(Point(1,1), pic) # setting the image val so i can get height and width
    width = image.getWidth()
    height = image.getHeight()
    win = GraphWin('Faces', width, height) # setting graph to pic size
    image = Image(Point(width / 2 , height / 2), pic).draw(win) #drawing pic in the center
    #Loops each time to get the values for parameters center and size
    for i in range(loops) :
        center = win.getMouse()
        p = Circle(Point(center.getX(),center.getY()), 2).draw(win)
        radius = win.getMouse()
        #Formula to find length between two points to get the size
        size = float(math.sqrt((center.getX()-radius.getX())**2 + (center.getY()-radius.getY())**2))
        p.undraw()
        drawFace(center,size,win)
    #exit interface   
    win.getMouse()
    win.getMouse()
    win.close()
        
main()
