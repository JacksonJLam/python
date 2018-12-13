#HoP4.py
#Jackson Lambert 12-13-18
#Acronym generator

def main() :
    print("This script will create an acronym from a a phrase that is inputted")
    phrase = input("Input a phrase: ")
    words = phrase.split()
    acc = " "
    for i in words :
        acc = acc + i[0].upper()
        
    print("Your acronym is", acc)
main()
    
