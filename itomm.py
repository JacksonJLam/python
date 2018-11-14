#itomm.py
#Inch to Millimeter converter
#Created by Jackson Lambert 11-14-18
def main () :
    print("This is an Inch to millimeter converter")
    #ask for input
    inch = eval(input("What is the distance in inches: "))
    #conversion equation
    mm = 25.4 * inch
    print(inch, "inches is equivalent to", mm, "millimeters")

main ()
#exit input
input("Hit enter to exit")
