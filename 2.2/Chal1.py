#Chal1.py
#Distance between cities with latitiude and longittude coordinates
#Jackson Lambert 1-3-19

import math
def maths(city1, city2) :
    long1,lat1 = city1.split(",")
    long2,lat2 = city2.split(",")
    long1 = eval(long1)
    long2 = eval(long2)
    lat1 = eval(lat1)
    lat2 = eval(lat2)
    #lat difference into miles
    distlat = abs(lat1 - lat2) * 69
    distlong = abs(long1 - long2) * 69
    #finding the diagonal distance to find a more accurate distance
    #round it down to 2 decimals
    dist = round(math.sqrt(distlong**2 + distlat**2), 2)
    print("The Distance is approximately:", dist,"miles away")

def main() :
    print("This script will find the distance in miles according to \nlattitude and longitude")
    print("longitude and latitude should be separated by commas")
    print("a negative value will represent east lat or a south long")
    city1 = input("Enter the 1st city's longitude and lattitude: ")
    city2 = input("Enter the 2nd city's longitude and lattitude: ")
    maths(city1,city2)

main()

