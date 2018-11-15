#sav.py
#Calculates the surface area and volume of a sphere
#Jackson Lambert 11-15-18
import math

def main() :
    #Welcome message
    print("Welcome, This script calculates the volume and surface area of a sphere, given it's radius.")
   #Asks for input
    r = eval(input("Enter the radius: "))
    #Next two lines are the equations for volume and surface area
    v = 4 / 3 * math.pi * r ** 3
    sa = 4 * math.pi * r**2
    #Output
    print("The volume is", v, "and the surface area is", sa)
#invoke
main()
