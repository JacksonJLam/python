#HoP6.py
#Finds the area of a pizza nd the cost per square inch
#Jackson Lambert 1-2-19
import math
def area(dia) :
    global ar 
    ar = (dia / 2)**2 * math.pi
    print("The area is ",ar)
def cost(cos, dia) :
    co = cos / ar
    print("The cost per square inch is " ,round(co, 2))
    
def main() :
    print("This program will find a pizza's area and cost per square inch")
    dia = eval(input("How big is the pizza?(in inches): "))
    cos = eval(input("How much did it cost?: "))
    area(dia)
    cost(cos, dia)
main()
    
    
