#HoP9.py
#Gives out quiz grades
#Jackson Lambert 1-14-19

def score(grade) :
        if grade == 100 :
            grade = str(grade)
            simpgrade = grade[0:2]
        elif grade > 100 :
            print("Invalid grade")
            print("Hit enter to restart")
            input("")
            main()
        elif grade == str :
            print("Invalid grade")
            print("Hit enter to restart")
            input("")
            main()
        else:
            grade = str(grade)
            simpgrade = grade[0]
        ltrgrd = ["F","F","F","F","F","F","D","C","B","A","A"]
        actgrad = ltrgrd[int(simpgrade)]
        print("Your Grade is: {0}".format(actgrad))

        
def main() :
    print("This script will display your quiz grade when a value 0-100 is given")
    try :
        grade = int(input("What was your grade?(0-100): "))
        score(grade)
    except ValueError :
        print("Entered a non number")
        print("Hit enter to restart")
        input("")
        main()
    
   
main()
