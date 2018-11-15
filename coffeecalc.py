#coffeecalc.py
#This script calculates how much x pounds of Konditorei coffe costs plus shipping
#Jackson Lambert 11-15-18

def main():
    #Welcome & Explanation
    print("Welcome to the Konditorei Coffee Calculator")
    print("We'll calculate the amount an amount of coffee costs plus shipping")
    #User input to get lbs of coffee
    order = eval(input("How many pounds of coffee would you like to purchase?: "))
    #Cost and total cost, used later to explain coffee cost + shipping
    cost = order * 0.86
    total_cost = cost + 1.50
    #Output to show cost of x amount of coffee,
    print("The total cost of", order, "pounds of coffee is")
    print(total_cost, "USD")
    print("The coffee itself cost,", cost, "with $1.50 shipping")
#invoke
main()
#exit input
input("Hit enter to exit")

