#chal2.py
#Jackson Lambert 1-14-19
#output verifier

def main() :
    print("This script will prompt for 3 values an verify them")
    val1 = int(input("Input a number: "))
    val2 = int(input("Input a number: "))
    val3 = int(input("Input a number: "))
    if val1 == val2 :
        print(val1)
    elif val1 == val3 :
        print(val1)
    elif val2 == val3 :
        print(val2)
    else :
        print("ERROR")
main()
