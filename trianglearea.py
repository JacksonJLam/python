#trianglearea.py
#calculates the area of a triangle given te lenght of three sides
#Jackson Lambert 11-15-18
import math
def main() :
    print("This script calculates the area of the triangle by its 3 side lengths")
    a = eval(input("Enter a side length: "))
    b = eval(input("Enter another side length: "))
    c = eval(input("Enter the 3rd side length: "))
    s = (a + b + c) / 2
    a = math.sqrt(s * (s - a)*(s-b)*(s-c))
    print("The area of the triangle is", a)
main()
