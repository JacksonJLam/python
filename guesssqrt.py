#guesssqrt.py
#Jackson Lambert 12-11-18
#makes the guess/ approximation of a square root

import math

def main() :
    print(" ")
    print("Welcome, This script will prompt for a number to square root and")
    print(" ")
    print("make an approximation of the square root and show how far it was away")

    x = eval(input("Enter a value to square root: "))
    print(" ")
    guess = eval(input("How many times do you want the program to repeat: "))
    print(" ")

    for i in range(guess):
        guess = (guess + x/guess)/2

        sqrt = math.sqrt(x)
        dist = guess - sqrt

    print("The program guessed a number", guess, "and that is", dist,"away from")
    print("the actual answer of", sqrt)

main()
