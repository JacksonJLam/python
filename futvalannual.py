# futvalannual.py
# Improved by Jackson Lambert 11.14.18
# A program to compute the value of an investment
# carried a selectable amount of years in the future

def main():
    #Greetings
    print("This program calculates the future value")
    print("of a an investment over a selectable amount of years.")
    #Asking for input for each variable
    principal = eval(input("Enter the amount you will invest every year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the amount of time (in years) the investment stays: "))
    principal = principal * years
    #Above is finding the ammount you put in and below is tha amount in plus interest rates
    for i in range(years):
        principal = principal * (1 + apr)
    #Print Results
    print("The value in", years, "years is: ", principal)

main()
