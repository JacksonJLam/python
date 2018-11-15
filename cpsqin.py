#cpsqin
#cost per square inch of a pizza
#Jackson Lambert 11-15-18
import math
def main() :
        print("This script calculates the cost per square inch of a pizza")
        #input for variables
        dia = eval(input("How big is the diameter of the pizza?: "))
        price = eval(input("What's the price of the pizza?: "))
        #Getting the radius from the diameter
        r = dia/2
        #finding the area of the pizza
        area = math.pi * r**2
        #Price over area to get the cost per square inch
        cost = price / area
        #Rounding down to 2 decimal place, since we count cents in .00-.99
        cost = round(cost, 2)
        #print output
        print("The cost per square inch of that pizza is", cost)
main()
#input to exit
input("Hit enter to exit")
        
