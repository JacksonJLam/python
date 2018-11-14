#convertexit.py
#A program to convert Celsius temps to Fahrenheit
#by: Jackson Lambert 11-14-18
def main() :
    #Greeting
    print("Welcome to the Celsius to Fahrenheit converter")
    #Asking for degrees celsius input
    celsius = eval(input("What is the Celsius temperature? "))
    #Equation to convert
    fahrenheit = 9 / 5 * celsius + 32
    #Print the result
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    #input so the script does not instantly close
    input("Hit Enter to exit script")

main ()
