#leibinz.py
#Jackson Lambert 12-11-18
#finds the Nth term in pi

import math

def main() :
    print("Welcome! This script will find the sum of nth terms in the leibniz sequence")
    nth = eval(input("Enter the term number: "))
    final = 0
    for i in range(0,nth,2) :
        final += ((1.0/(i+i+1))-(1.0)/(i+i+3))
        finalval = 4*final
    pival = math.pi - finalval
    print("The Answer is", finalval)
    print(finalval, "Subtracted from pi = ", pival)
    input("Press Enter to Exit")
main()

    
