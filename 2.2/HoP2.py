#HoP2.py
#Prints the ants go marching in 10 verses of ants go marching
#Jackson Lambert

act = ["suck his thumb","tie his shoe","scream REEE","cry cus he's poor","tell his teammates to go dive","get them fat picks","legally change his name to kevin","find teammates to bait","hit shots like Pine","admire men"]
num = [1,2,3,4,5,6,7,8,9,10]
def verse(activity, numb) :
    print("The ants go marching ",numb,"by",numb,", hurrah! Hurrah!")
    print("The ants go marching ",numb,"by",numb," hurrah! Hurrah!")
    print("The ants go marching ",numb,"by",numb,) 
    print("The little one stops to " ,activity,)
    print("And they all go marching down ...")
    print("In the ground...")
    print("To get out ...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def main() :
        #loop for the 10 verses, replacing numb and activity
        #with whatever value i corresponds to in the arrays
       for i in range(10):
           verse(act[i], num[i])
main()
           
