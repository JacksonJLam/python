#HoP7
#Jackson Lambert 12-14-18
#Encodes and decodes a caesar cypher

def main() :
    print("This script will encode and decode a mesage using the caesar cypher")
    msg = input("Input your message: ")
    key = eval(input("Input your key (Use a negative key to decode): "))
   
    msgalt = ""
    #Translates each letter and adds to the encoded and decoded message
    for ch in msg :
        translation = chr(ord(ch)+key)
        msgalt = translation + msgalt
    print(msgalt)
main()
