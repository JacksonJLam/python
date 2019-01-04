#HoP1.py
#Jackson Lambert
#Calculates the amount made accounting for overtime increased pay

def main() :
    print("This program will find the total wages depending on rates and time worked")
    print(" ")
    hours = eval(input("How many hours were worked?: "))
    rate = eval(input("What is the hourly rate?: "))
    #what to do if there is overtime hours
    if hours > 40 :
        ot = hours - 40
        pay = (40 * rate) + (ot * (rate * 1.5))
    #what to do if it is 40 hours or below
    else :
        pay = hours * rate
    pay = str(pay)
    print("Total wages this week are: ", "$" + pay)
main()
