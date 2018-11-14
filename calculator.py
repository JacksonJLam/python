#calculator.py
#A Calculator script
#Created by Jackson Lambert 11-14-18

def main():
    #Greetings
    print("Welcome to my calculator")
    #White space, makes it easier to read
    print(" ")
    #Loop 100 times for lots of equations
    for i in range(100) :
        print(" ")
        #ask for input
        x = eval(input("Input a mathematical equation: "))
        print(" ")
        #print the expression, since python automatically does the math
        print( x )
main()
    
