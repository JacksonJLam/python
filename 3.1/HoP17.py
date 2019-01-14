#HoP17.py
#Animated circle
#Jackson Lambert 1-14-19
from graphics import *
def main() :
    dx = 1
    dy = 1
    win = GraphWin("Animated Circle", 500,500)
    win.setCoords(-20,-20,20,20)
    circle = Circle(Point(0, 0), 2).draw(win)
    for i in range(100000000000000000) :
        circle.move(dx,dy)
        center = circle.getCenter()
        if center.getX() == 20 or center.getX() == -20 :
            dx = dx * -1
        if center.getY() == 20 or center.getY() == -20 :
            dy = dy * -1
        update(25)
main()
