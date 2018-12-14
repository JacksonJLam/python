#HoP10.py
#Jackson Lambert 12-14-18
#Gets the average number of letters per word
def main() :
    
    print("This script will tell the average number of letters per word")
    sent = input("Enter your sentence: ")
    words = len(sent.split(" "))
    letters = len(sent.strip(" ")) - sent.count(" ")
    avg = letters / words
    print("There is an average of", avg, "letters per word")
main()
