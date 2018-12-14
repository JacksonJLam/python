#HoP9
#Jackson Lambert 12-14-18
#Counts the number of words in a sentence

def main() :
    print("This script will tell the numbers of words in a sentence")
    sent = input("Enter your sentence: ")
    sent.split(" ")
    length = len(sent.split(" "))
    print("There are",length,"words in this sentence")
main()
