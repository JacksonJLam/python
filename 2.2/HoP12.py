#HoP12.py
#Jackson Lambert
#squaring each entry in a list

# a list of numbers
numbers = [0,1,2,3,4,5,6,7,8,9,10]
#adds the numbers in the lists together
def sumList(nums) :
    total = 0
    for i in nums :
        total = total + nums[i]
    print("The sum is",total)
#run square each
def main() :
    print("This script will add a list of numbers")
    print("The list of numbers is", numbers)
    sumList(numbers)
main()
