#HoP8.py
#Senate / House eligibility
#Jackson Lambert 1-4-19

def main() :
    print("This script will find the eligibility to be a part of U.S House or Senate")
    age = int(input("Enter your age: "))
    cit = int(input("Enter how long you've been a U.S citizen: "))
    if age >= 30 and cit >= 9 :
        print("You are eligible for a US senator position")
    else :
        print("You are not eligible for a US senator postition")
    if age >=25 and cit >=7 :
        print("You are eligible for a US house of representatives position")
    else :
        print("You are not eligible for a US house of representatives position")
main()
