#chal4.py
#Jackson Lambert 1-14-19
#password security

def main() :
    print("This script will evaluate password strength")
    pw = input("Input a password: ")
    length = len(pw)
    if length >= 12 :
        print("That password is Very Strong")
    elif length >=8 and length < 12 :
        print("This password is moderately strong")
    elif length <= 8 :
        print("This password is weak")
main()
