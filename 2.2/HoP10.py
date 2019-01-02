#HoP10.py
#Acronym generator
#Jackson Lambert 1-2-19


def acc(phrase) :
    #spltting phrase
    words = phrase.split()
    #defining acc
    acc = " "
    for i in words :
        #add letters each loop, making each upercase.
        acc = acc + i[0].upper()

    print("Your acronym is", acc)
def main() :
    print("This script will create an acronym from a a phrase that is inputted")
    phrase = input("Input a phrase: ")
    acc(phrase)
main()
