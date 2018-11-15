#ladder.py
#Calculates the length of a ladder to reach a given height when leaned against a house
#Jackson Lambert 11-15-18
import math
def main() :
    print("This script will find out how tall of a latter you need to reach a specific height")
    h_height = eval(input("How Tall is the house (in feet): "))
    l_angle = eval(input("What angle is the latter leaning at: "))
    r = (math.pi / 180) * l_angle
    l_length = h_height / math.sin(l_angle)
    l_length = round(l_length, 3)
    print("A ladder", l_length, " feet tall to reach a ", h_height, "foor tall roof")
main()
input("Hit enter to exit")
