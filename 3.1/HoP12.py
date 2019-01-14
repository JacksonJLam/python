#HoP11.py
#Leap year calculator
#Jackson Lambert 1-4-19
import math
def allowed(day,days) :
    if day > days :
        print("This date is invalid")
    else :
        print("This is a valid date")
def main() :
    print("This script will find if a date is valid or not")
    date = input("Enter a date in MM/DD/YYYY format: ")
    month,day,year = date.split("/")
    year = int(year)
    day = int(day)
    month = int(month)
    century = year % 100
    if century == 0 :
        ans = year % 400
        if ans == 0 :
            leap = 1
        else :
            leap = 0
    else :
        ans = year % 4
        if ans == 0 :
           leap = 1
        else :
           leap = 0
    if month == 1 :
        days = 31
        allowed(day,days)
    if month == 2 :
        if leap == 1 :
            days = 29
        else :
            days = 28
        allowed(day,days)
    if month == 3 :
        days = 31
        allowed(day,days)
    if month == 4 :
        days = 30
        allowed(day,days)
    if month == 5 :
        days = 31
        allowed(day,days)
    if month == 6 :
        days = 30
        allowed(day,days)
    if month == 7 :
        days = 31
        allowed(day,days)
    if month == 8 :
        days = 31
        allowed(day,days)
    if month == 9 :
        days = 30
        allowed(day,days)
    if month == 10 :
        days = 31
        allowed(day,days)
    if month == 11 :
        days = 30
        allowed(day,days)
    if month == 12:
        days = 31
        allowed(day,days)
    
    
main()

