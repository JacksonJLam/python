#HoP9.py
#Jackson Lambert 1-4-19
#calculates easter date

def main() :
    print("This script will find the date of easter in a given year")
    year = int(input("Enter a year: "))
    if year >=1982 and year <=2048 :
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        date = 22 + d + e
        date = date - 31
        print("Easter is on April",date,"in", year)
    else :
        print("Year out of range")
main()
