#seriesavg.py
#finds the average of a series of numbers selected by the user
#Jackson Lambert 11-15-18

def main() :
        print("This script asks for a series of numbers, then finds the average of these numbers")
        total = 0
        loops = eval(input("How many numbers do you want to enter: "))
        for i in range(loops) :
            x = eval(input("Enter a Number: "))
            print("You added a ", x)
            total = total + x
            avg = total/loops
        print("The average is", avg)
main()
print("Hit enter to exit")
        
