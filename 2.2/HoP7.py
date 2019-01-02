#HoP7.py
#Jackson Lambert 1-2-19
#Finds the nth term in the fibonacci sequence

import math
def maths(n) :
    a, b = 0, 1
    for i in range(n):
        a,b = b, a + b
    n = str(n)
    print("The", n + "th term in the fibonacci sequence is", a)
    print("")
    input("Hit Enter to Exit")

def main() :
    print("Welcome to my Fibonacci Sequence script")
    print("This script will find the nth term in the Fibonacci Sequence")
    n = eval(input("Enter the term number you want to find: "))

    maths(n)
main()
