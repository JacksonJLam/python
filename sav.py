#sav.py
#Calculates the surface area and volume of a sphere
#Jackson Lambert 11-15-18
import math

def main() :
    print("Welcome, This script calculates the volume and surface area of a sphere, given it's radius.")
    r = eval(input("Enter the radius: "))
    v = 4 / 3 * math.pi * r ** 3
    sa = 4 * math.pi * r**2

    print("The volume is", v, "and the surface area is", sa)
main()
