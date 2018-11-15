#distancecalc.py
#finds the distance between to points
#Jackson Lambert 11-15-18

import math
def main() :
    #Welcome
    print("This calculator will find the slope between 2 points")
    #Getting input
    x1 = eval(input("What is the value of X for the first coordinate?: "))
    y1 = eval(input("What is the value of Y for the first coordniate?: "))
    x2 = eval(input("What is the value of X for the coordinates?: "))
    y2 = eval(input("What is the value of Y for the coordniates?: "))
    #Equations
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance between the two points is", distance)
main()
input("Hit enter to exit")
