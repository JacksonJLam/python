#Chal2.py
#calculates ERA
#Jackson Lambert 1-3-9

def era(runs,innings) :
    ERA = (9*runs) / innings
    ERA = round(ERA, 2)
    print("The Pitchers ERA is", ERA)
def main() :
    print("This script will find the ERA when given input")
    runs = eval(input("How many runs did the pitcher give up?: "))
    innings = eval(input("How many innings did they pitch?: "))
    era(runs,innings)
main()
