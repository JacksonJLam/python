#convertloop.py
#A program to convert Celsius temps to Fahrenheit
#by: Jackson Lambert 11-14-18
def main() :
    #Greetings
    print("Welcome to the Celsius to Fahrenheit converter")
    #All (" ") Is whitespace to improve readability
    print(" ")
    #Telling the user how many times it'll loop
    print("This script will run 3 times before exiting")
    print(" ")
    #Looping the equation 3 times
    for i in range(3) :
        #Ask for user input
        celsius = eval(input("What is the Celsius temperature? "))
        print(" ")
        #Equation to get fahrenheit
        fahrenheit = 9 / 5 * celsius + 32
        #Print the outcome
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print(" ")
        
main ()
#Exit prompt so the module does not exit on its own
input("Hit enter to exit script")
