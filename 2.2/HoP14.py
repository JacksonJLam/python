#Hop14.py
#Jackson Lambert 1-2-19
#Reads stuff from a file and squares and adds it

#combined previous maths for easier access and don't replace in list
def squareAdd(nums) :
    total = 0
    for i in range (len(nums)) :
        sqr = eval(nums[i])**2
        #add sqr to total each time
        total = total + sqr
    print("The squared and summed value of", nums,)
    print("is", total)

def main() :
    print("This program will sqaure and add each number in a file")
    fileName = input("Input a file name: ")
    n = open(fileName, "r")
    read = n.readline()
    nums = read.split(" ")
    
    squareAdd(nums)
    n.close()
main()
    
