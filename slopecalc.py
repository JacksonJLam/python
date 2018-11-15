#slopecalc.py
#Calculates the slope of 2 points
#Jackson Lambert 11-15-18

def main() :
    #Welcome
    print("This calculator will find the slope between 2 points")
    #Getting input
    x1 = eval(input("What is the value of X for the first coordinate?: "))
    y1 = eval(input("What is the value of Y for the first coordniate?: "))
    x2 = eval(input("What is the value of X for the coordinates?: "))
    y2 = eval(input("What is the value of Y for the coordniates?: "))
    #Eqautions to get slope
    slope = (y2 - y1) / (x2 - x1)
    easier_y = (y2 - y1)
    easier_x = (x2 - x1)'
    #Output
    print("The slope is", slope)
    print("An easier way to read this slop is rise over run, and that would look like")
    print("These would be in fraction form if i knew how to do that")
    print(easier_y, "/", easier_x)

main()
#Exit input
input("Hit enter to exit")

    
