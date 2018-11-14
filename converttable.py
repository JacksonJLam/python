#converttable.py
#A program to convert Celsius temps to Fahrenheit
#by: Jackson Lambert 11-14-18
def main() :
    #Greetings
    print("Welcome to the Celsius to Fahrenheit converter")
    #All (" ") Is whitespace to improve readability
    print(" ")
    #Looping the equation 11 times to get every 10 degrees from 0-100
    for i in range(11) :
        x = i * 10
        #Equation to get fahrenheit
        fahrenheit = 9 / 5 * x + 32
        #Print the outcome
        print( x, "degrees Celsius is equivalent to", fahrenheit, "degrees fahrenheit")
        print(" ")
        
main ()
#Exit prompt so the module does not exit on its own
input("Hit enter to exit script")
