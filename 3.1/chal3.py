#chal3.py
#Jackson Lambert 1-14-19
#Vote Pass

def deciding(area,votes) :
    if area == 1 :
        total = 100
        decide = votes / 100
        if decide > .5 :
            print("The Senate vote has passed")
        else :
            print("The Senate vote did not pass")
    elif area == 2 :
        total = 435
        decide = votes / 435
        if decide > .5 :
            print("The House of Representatives vote has passed")
        else :
            print("The House of Representatives vote did not pass")

def main() :
    print("This script will figure out if a vote passes in the HoR or Senate")
    area = int(input("Which area is voting?(1=Senate/2=HoR): "))
    votes = int(input("How many Yea votes are there?: "))
    deciding(area,votes)
    
main()
