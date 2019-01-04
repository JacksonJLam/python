#HoP10.py
#Jackson Lambert 1-4-19
#calculates easter date

#Modified calculatet to fix specific dates being off
def maths(year) :
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    date = 22 + d + e
    date = date - 31
    print("The date of Easter in",year,"is April",date)
#calculates date
def mathsmod(year) :
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        date = 22 + d + e
        date = date - 38
        print("The date of Easter in",year,"is April",date)
def main() :
    print("This script will find the date of easter in a given year")
    #loop until a correct date is put in
    loop = 0
    while loop == 0 :
        year = int(input("Enter a year: "))
        if year >=1900 and year <=2099 :
            loop = 1
            #ifs for modififed maths
            if year == 1954 :
                    mathsmod(year)
            elif year == 1981 :
                   mathsmod(year)
            elif year == 2049 :
                    mathsmod(year)
            elif year == 2076 :
                    mathsmod(year)
            #do maths for everything else
            else :
                    maths(year)
        else :
            print("Year out of range")
            print("Try again")
        
main()
