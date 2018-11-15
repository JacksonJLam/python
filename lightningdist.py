#lightningdist.py
#Calculates the distance from a lightning strike by taking time elapsed between strike and thunfer
#Jackson Lambert 11-15-18

def main() :
    #Printing welcome and explanation
    print("Welcome, this script will calculate how far a lightning strike is away by how much time has passed")
    print("It will do this by asking how long between the strike and the sound of thunder")
    #asking for user input
    time = eval(input("How many seconds did it take to hear thunder after the lightning?: "))
    #Equation to get the distance in feet and going from feet to miles
    dist = (time * 1100)
    dist_in_miles = dist/5280
    #output
    print("The lightning is", dist, "feet , or ", dist_in_miles, "miles away")
#invoke the functiion
main()
#exit input
input("Hit enter to exit")
