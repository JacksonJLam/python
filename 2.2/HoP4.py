#HoP4.py
#Sum of N and sum of N**3 functions defining
#Jackson Lambert 1-2-19


def sumN(n) :
    val = 0
    for i in range(n + 1) :
        val = val + i
    print("The sum of the first ",n," natural numbers is",val)
def sumNCubes(n) :
    val = 0
    for i in range(n + 1) :
        val = val + i**3
    print("The sum of the first ",n," natural numbers cubed is",val)
def main() :
    print("This program will find the sum of the first nth natural numbers")
    print("It will also find the sum when cubed")
    loop = eval(input("Enter a number: "))
    sumN(loop)
    sumNCubes(loop)
main()
