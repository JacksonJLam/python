#HoP2.py
#Jackson Lambert 1-4-19
#Grades if statements

def main() :
    print("This quiz will give you a letter grade depending on a score of 1-5")
    numgrd = eval(input("Enter your number grade: "))
    if numgrd == 5 :
        print("Your grade is an A")
    if numgrd == 4 :
        print("Your grade is a B")
    if numgrd == 3 :
        print("Your grade is a C")
    if numgrd == 2 :
        print("Your grade is a D")
    if numgrd == 1 :
        print("Your grade is a F")
    if numgrd == 0 :
        print("Your grade is a F")
main()
