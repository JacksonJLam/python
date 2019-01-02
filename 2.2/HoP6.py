#HoP6.py
#Finds the area of a triangle given the length of its three sides
#Jackson Lambert
import math
def maths(a,b,c) :
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a)*(s-b)*(s-c))
    print("The area of the triangle is", area)
def main() :
    print("This script calculates the area of the triangle by its 3 side lengths")
    a = eval(input("Enter a side length: "))
    b = eval(input("Enter another side length: "))
    c = eval(input("Enter the 3rd side length: "))
    maths(a,b,c)
main()
