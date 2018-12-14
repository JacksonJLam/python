# HoP13.py
# Jackson Lambert
# 12-14-18
# Program to creates a caesar cipher via batch files

def main():
    print("This program creates a file of usernames from a file of names.")

    # get the file names
    infileName = input("What file are the ciphers in? ")
    outfileName = input("What file should they be written to? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    msgalt = " "
    for line in infile:
        # get the key and msg
        key, msg = line.split("/")
        #set the key to evaluable
        key = eval(key)
    for ch in msg :
        translation = chr(ord(ch)+key)
        msgalt = translation + msgalt
        # write it t o the output file
    print(msgalt, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Cipher has been printed to", outfileName)

main()
