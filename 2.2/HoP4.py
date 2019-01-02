#HoP4.py
#Sum of N and sum of N**3 functions defining
#Jackson Lambert 1-2-19


def sumN(n) :
    val = 0
    for i in range(n + 1) :
        val = val + i
    print(val)
def sumNCubes(n) :
    val = 0
    for i in range(n + 1) :
        val = val + i**3
    print(val)
