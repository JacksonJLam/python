#seriessum.py
#finds the sum of a series of numbers selected by the user
#Jackson Lambert 11-15-18

def main() :
        print("This script asks for a series of numbers, then adds the numbers")
        total = 0
        loops = eval(input("How many numbers do you want to enter: "))
        for i in range(loops) :
            x = eval(input("Enter a Number: "))
            print("You added a ", x)
            total = total + x
        print("The total is", total)
main()
print("Hit enter to exit")
        
