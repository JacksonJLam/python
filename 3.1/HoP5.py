#HoP5.py
#BMI Calculator
#Jackson Lambert 1-4-19
def main() :
    print("This script will calculate a person's BMI and determine if it is healthy or not")
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    bmi = round((weight*720) / height**2, 2)
    if bmi >= 19 and bmi <=25 :
        print("The BMI of", bmi,"is healthy")
    elif bmi < 19 :
        print("The BMI of", bmi,"is underweight and unhealthy")
    elif bmi > 25 :
        print("The BMI of", bmi,"is overweight and unhealthy")
main()
    
