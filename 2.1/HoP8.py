#HoP8
#Jackson Lambert 12-14-18
#Encodes and decodes a caesar cypher circular

def main() :
    #ask for input
    print("This script will encode and decode a mesage using the caesar cypher")
    msg = input("Input your message: ")
    key = eval(input("Input your key (Use a negative key to decode): "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    msgalt = ""
    #Translates each letter and adds to the encoded and decoded message
    for ch in msg :
        #subtracting the number val of a from the character value and it it to the key
        translation =(ord(ch) - ord('a')+key) % 26
        #the value translation in regards of the actual alphabet
        msgalt = msgalt + alphabet[translation]
    print(msgalt)
main()
