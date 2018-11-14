#battingavg.py
#calculates batting average
#Jackson Lambvert 11-14-18

def main() :
    name = input("Whats the player's name?: ")
    hits = eval(input("How many hits?: "))
    at_bats = eval(input("How many at-bats?: "))
    avg = hits/at_bats
    print( name, "has a batting average of", avg)
main()   
