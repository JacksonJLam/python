#HoP11.py
#12-14-18 Jackson Lambert
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    print("Input will be asked for twice")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    print(" ")
    print("{0:<0} {1:^10} {2:>10}".format("index", x, y))
    print(" ")
    for i in range(10) :
        y = 3.9 * y * (1 - y)
        x = 3.9 * x * (1 - x)
        y = round(y, 7)
        x = round(x, 7)
       
        print("{0:<0} {1:^15} {2:>15}".format(i, x, y))
main()
