#HoP11.py
#Jackson Lambert
#squaring each entry in a list

# a list of numbers
numbers = [0,1,2,3,4,5,6,7,8,9,10]
#math to square these numbers, then replace their originals with the sqared
def squareEach(nums) :
    for i in nums :
        sqr = nums[i]**2
        nums[i] = sqr
    print("The new numbers are",nums)
#run square each
def main() :
    print("This script will square a list of numbers")
    print("and replace their originals in the list")
    print("The Original numbers are",numbers)
    squareEach(numbers)
main()
