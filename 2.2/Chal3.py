#Chal3.py
#calculates the price on an item with sale
#Jackson Lambert 1-3-9

def main() :
    print("This script will calculate an item that is x percent off")
    #vars
    price = eval(input("What's the regular price of the item"))
    sale = eval(input("What's the saale amount (decimal)"))
    #math
    sales = price - (price * sale)
    print(sales)
main()
