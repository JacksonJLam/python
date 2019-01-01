#HoP14.py
#Word count, character count, line count
#Jackson Lambert 1-1-19

def main():
    print("This file will count words, lines and character count")
    # get the file name
    fileName = input("What file are the test scores in?")
    # open the files
    doc = open(fileName, "r")
    #Setting string values to nothing
    wc = 0
    lc = 0
    cc = 0
    for line in doc:
        #Split at the spaces
        words = line.split()
        #split at the end of lines
        lines = line.split(" \n")
        #add the character length of each line together
        cc = cc + sum(len(word) for word in lines)
        #add the # of lines up
        lc += len(lines)
        #amount of words
        wc += len(words)    
    print("There are:", wc, "words")
    print("There are:",lc, "lines")
    print("There are:",cc, "characters")
    doc.close()
main()
    
