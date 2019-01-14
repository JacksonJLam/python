#chal5.py
#Jackson Lambert 1-14-19
#Determines whether a number is valid or not
import string
def main() :
    #a string of characters to exclude
    exclude = set(string.punctuation)
    #input
    x = input("Enter a phone number: ")
    #find the true length of the string
    xtrue = ''.join(ch for ch in x if ch not in exclude)
    #if = 10, then its a real number
    if len(xtrue) == 10 :
        print(x,"Is a valid phone number")
    else :
        print("This phone number is invalid")
main()
