#HoP11.py
#Leap year calculator
#Jackson Lambert 1-4-19

def main() :
    print("This is a leap year calculator")
    year = int(input("Enter a year: "))
    century = year % 100
    if century == 0 :
        ans = year % 400
        if ans == 0 :
            print("This year is a leap year")
        else :
            print("This year is not a leap year")
    else :
        ans = year % 4
        if ans == 0 :
            print("This year is a leap year")
        else :
            print("This year is not a leap year")
main()
