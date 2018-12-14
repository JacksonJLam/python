#HoP5.py
#Jackson Lambert 12-13-18
#Acronym generator

def main() :
    print("This script will get the numerical value of your name")
    name = input("Input your name(all lowercase): ")
    first, middle, last = name.split()
    v = 0
    for i in first :
        a = ord(i) - 96
        v = a + v
    for l in middle :
        b = ord(l) - 96
        v = b + v
    for j in last :
        c = ord(j) - 96
        v = c + v
    print("The numerical value of the name", first.capitalize(),middle.capitalize(),last.capitalize(),"is", v)
    
main()
