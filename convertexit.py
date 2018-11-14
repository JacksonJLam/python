#convertexit.py
#A program to convert Celsius temps to Fahrenheit
#by: Jackson Lambert 11-14-18
def main() :
    print("Welcome to the Celsius to Fahrenheit converter")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Hit Enter to exit script")

main ()
