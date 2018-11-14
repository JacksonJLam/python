#A program to convert Celsius temps to Fahrenheit
#by: Jackson Lambert 11-14-18
def main () :
    print("This is a Fahrenheit to Celsius converter")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius.")

main ()
input("Hit enter to exit")
