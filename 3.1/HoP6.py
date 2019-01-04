#HoP6.py
#Lazytown speeding ticket
#Jackson Lambert 1-4-19

def main() :
    print("This script will find if you were speeding and will fine you if you do")
    limit = int(input("Input speed limit: "))
    speed = int(input("What speed was the vehicle clocked at?: "))
    if speed <= limit :
        print("You were going a legal speed.")
    elif speed > limit and speed < 90 :
        over = speed - limit
        ticket = 50 + 5*over
        print("You went", over,"over the speed limit and your ticket is", ticket)
    elif speed > limit and speed > 90 :
        over = speed - limit
        ticket = 250 + 5*over
        print("You went", over,"over the speed limit and your ticket is", ticket)

main()
