#chal1.py
#Jackson Lambert 1-14-19
#Finds the credit card system depending on number

def main() :
    number = []
    print("This script will find your credit card issuer")
    num = input("Enter a credit card number: ")
    number.append(num)
    ident = int(number[0][0])
    if ident == 2 :
        print("That card is as Mastercard(2017)")
    elif ident == 3 :
        print("That card is an American Express")
    elif ident == 4 :
        print("This card is a visa")
    elif ident == 5 :
        print("This card is a Mastercard")
    elif ident == 6 :
        print("This card is a Discover")
    elif ident == 1 :
        print("This card is most likely issued by an airline")
    elif ident == 7 :
        print("This card is most likely issued by a petroleum company")
    elif ident == 8 :
        print("This card is most likely issued by a telecom or health care company")
    else :
        print("Unkown Card Type")
main()
