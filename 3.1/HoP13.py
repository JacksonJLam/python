#HoP13.py
#Jackson Lambert 1-4-19
#numbered day calculator
def main() :
    print("This script will find if a date is valid or not")
    date = input("Enter a date in MM/DD/YYYY format: ")
    month,day,year = date.split("/")
    year = int(year)
    day = int(day)
    month = int(month)
    #leap year equation checks
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
    dayNum = 31*(month - 1) + day
    #if feb and leap ifs
    if month > 2 :
        dayNum = dayNum - (4*month + 23) // 10
        if leap == 1 :
            dayNum = dayNum + 1
    print(dayNum)
main()
