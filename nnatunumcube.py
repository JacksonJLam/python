#nnatnumcube.py
#finds the sum of the cube of first n natural numbers
#Jackson Lambert

def main() :
    #Welcome
    print("This script will add all natural numbers cubed up until a specified number")
    n = eval(input("Enter the number you want to add until: "))
    #Add 1 so it counts to the number specified except for just below
    n = n + 1
    whole = 0
    #loop from 1 to n
    for i in range(1, n) :
            #whole sum is added to by the current loop # each time
             current = i**3
             whole = whole + current
             
    print("The sum of all natural numbers 1 -", n - 1, "is",whole)
main()
input("Hit enter to exit")
