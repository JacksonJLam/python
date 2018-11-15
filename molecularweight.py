#molecularweight.py
#Calculates the molecular weight of a carbohydrate depending on variables
#Jackson Lambert 11-15-18

def main() :
    #Welcome message
    print("Welcome, This script will calculate the molecular weight of a carbohydrate")
    #asking for input
    h = eval(input("How many hydrogen atoms are in the molecule?: "))
    c = eval(input("How many carbon atoms are in the molecule?: "))
    o = eval(input("How many oxeygen atoms are in the molecule?: "))
    #Multiplying the input by the weight per atom
    h_total = h * 1.00794
    c_total = c * 12.0107
    o_total = o * 15.9994
    weight = h_total + c_total + o_total
    #Output to show results
    print("The total weight of the molecule is", weight, "grams / mole")
    print("Weight coming from hydrogen is", h_total, "grams / mole")
    print("Weight coming from carbon is", c_total, "grams / mole")
    print("Weight coming from oxeygen is", o_total, "grams / mole" )
main()
#Exit input
input("Hit enter to exit")
