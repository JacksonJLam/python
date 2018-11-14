#convert.py
#A program to convert Celsius temps to Fahrenheit
#by: Jackson Lambert 11-14-18
def main() :
    #Greeting
    print("Welcome to the Celsius to Fahrenheit converter")
    #Take input for celsius
    celsius = eval(input("What is the Celsius temperature? "))
    #Equation to get Farenheit from celsius
    fahrenheit = 9 / 5 * celsius + 32
    #Display the farenheit
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main ()
