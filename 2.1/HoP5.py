#HoP5.py
#Jackson Lambert 12-13-18
#Numerical value of name generator

def main() :
    print("This script will get the numerical value of your name")
    name = input("Input your first name(all lowercase): ")
    v = 0
    for i in name :
        a = ord(i) - 96
        v = a + v
    print("The numerical value of the name", name.capitalize(), "is", v)
    
main()
