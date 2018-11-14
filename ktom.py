#A program to convert Kilometers to Miles
#by: Jackson Lambert 11-14-18
def main () :
    print("This is a Kilometer to Mile converter")
    #ask for input
    kilom = eval(input("What is the distance in Kilometers? "))
    #conversion equation
    miles = .62 * kilom
    print(kilom, "Kilometers is equivalent to", miles, "miles")

main ()
#exit input
input("Hit enter to exit")
