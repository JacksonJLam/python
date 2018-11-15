#nnatnum.py
#finds the sum of the first n natural numbers
#Jackson Lambert

def main() :
    #Welcome
    print("This script will add all natural numbers up until a specified number")
    n = eval(input("Enter the number you want to add until: "))
    #Add 1 so it counts to the number specified except for just below
    whole = 0
    n = n + 1
    #loop from 1 to n
    for i in range(1, n) :
            #whole sum is added to by the current loop # each time
             whole = i + i
             whole = whole + i
    print("The sum of all natural numbers 1 -", n - 1, "is",whole)
main()
input("Hit enter to exit")


                 
             
        
    
