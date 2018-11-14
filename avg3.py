# avg3.py
# Jackson Lambert, theft script
# A simple program to average 3 exam scores
# Illustrates use of multiple input

def main():
    print("This program computes the average of two exam scores. ")
    #Taking 3 values
    score1, score2, score3 = eval(input("Enter three scores separated by a commas: "))
    #Add 3 scores and divide by 3 to get the average
    average = (score1 + score2 + score3) / 3
    #show the average
    print("The average of the scores is: ", average)

main()
