#futval3.py
#Created by Jackson Lambert
#Does compuound interest with nominal rates
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter your initial principal: "))
    rate = eval(input("Enter your yearly rate: "))
    period = eval(input("How many times a year it is compounded: "))
    for i in range (10 * period) :    
        principal = principal * (1 + rate/period)
    print("The value in 10 years is: ", principal)
main()

