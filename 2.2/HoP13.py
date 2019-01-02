#HoP13.py
#Jackson Lambert 1-2-19
#Modifies each entry in the list by converting it to a number

strings = ["4200", "42","69"]

def toNumbers(strList) :
    for i in range(len(strList)) :
        print("Converted",strList[i],"to a number")
        print(eval(strList[i]))
        
def main() :
    toNumbers(strings)
main()
