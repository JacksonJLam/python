#HoP7.py
#babysitter charges
#Jackson Lambert 1-4-19

def main() :
    print("This script will find the cost of a babysitter dpending on time")
    start = int(input("Enter the starting time(1-24): "))
    end = int(input("Enter the end tine(1-24): "))
    time = end - start
    if end - 21 > 0 :
        difrate = end - 21
        nrt = time - difrate
        pay = nrt * 2.50 + difrate * 1.75
    elif end - 21 <= 0 :
        pay = time * 2.50
    pay = str(pay)
    print("The total pay is $" + pay)
main()
