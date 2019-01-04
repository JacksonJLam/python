#HoP3.py
#Jackson Lambert 1-4-19
#Grades if statements

def main() :
    print("This quiz will give you a letter grade depending on a score of 0-100")
    numgrd = eval(input("Enter your number grade: "))
    if numgrd > 89 :
        print("Your grade is an A")
    elif numgrd > 79 :
        print("Your grade is a B")
    elif numgrd > 69 :
        print("Your grade is a C")
    elif numgrd > 59 :
        print("Your grade is a D")
    elif numgrd < 60 :
        print("Your grade is a F")
main()
