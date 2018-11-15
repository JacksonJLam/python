#gregep.py
#Calculates the gregorian epact of a given year
#Jackson Lambert
import math
def main() :
    print("This script will calculate the Gregorian epact for a given year")
    year = eval(input("Enter a year: "))
    C = (year // 100)
    epact = (8 + (C // 4) - C + ((8*C + 13)//25) + 11 * (year%19))%30
    print("The epact is", epact)
main()
input("Hit Enter to exit")
