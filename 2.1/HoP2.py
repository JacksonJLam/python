#HoP2.py
#Jackson Lambert 12-13-18
#Gives out quiz grades

def main() :
    print("This script will display your quiz grade when a value 1-5 is given")
    grade = eval(input("What was your grade?(0-5): "))
    ltrgrd = ["F","F","D","C","B","A"]
    actgrad = ltrgrd[int(grade)]
    print("Your Grade is: {0}".format(actgrad))
main()
