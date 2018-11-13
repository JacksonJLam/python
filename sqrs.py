#sqrs.py
#Created by Jackson Lambert 11-13-18
#prints squares of integers 1-10

def sqrs() :
    for i in range(10) :
        x = 1
        #X Plus the loop number
        x = x + i
        #Squares X
        x = x**2
        print(x)
sqrs()
