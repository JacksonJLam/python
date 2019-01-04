#HoP4.py
#Jackson Lambert 1-4-19
#Figuring out clcass standing depending on credits
standing = ["Freshman","Sophomore","Junior","Senior"] 
def main() :
    print("This script will figure our class standing via credits earned")
    cred = int(input("Enter the amount of credits earned: "))
    if cred < 7 :
        print("Those credits correspond with those of a", standing[0])
    elif cred >= 7 and cred < 16 :
        print("Those credits correspond with those of a", standing[1])
    elif cred >= 16 and cred < 26 :
        print("Those credits correspond with those of a", standing[2])
    elif cred >= 26 :
        print("Those credits correspond with those of a", standing[3])
main()
        
        
