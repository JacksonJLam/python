# HoP12.py
# Jackson Lambet 12-14-18
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    print("{0:<5} {1:<10}".format("Year", "Value"))
    for i in range (11) :
        principal = principal * (1 + apr)
        principal = round(principal, 2)
        print("{0:<5} ${1:<10}".format(i, principal))

main()
