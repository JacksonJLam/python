#HoP16.py
#Makes a histogram of test scores
#Jackson Lambert 1-1-19
from graphics import *

def main():
    # get the file name
    fileName = input("What file are the test scores in?")
    # open the files
    testscores = open(fileName, "r")
    win = GraphWin('Graphs',1100, 700 )
    val = Text(Point(550 , 400), "Scores")
    val.draw(win)

    for line in range(10) :
            #Read the line
            scores = testscores.readline()
            #split the values in the line
            score,amount = scores.split("/")
            #horizontal pos of bars and values
            horpos = line * 85 + 100
            #allows the amount to be used in math
            amount = eval(amount)
            #making amount bigger to make graphs look bigger
            amountgraph = amount * 20
            #draw the bar
            bar = Rectangle(Point(horpos, 350), Point(horpos + 50, 350 - amountgraph))
            bar.draw(win)
            bar.setFill("green")
            #draw the names
            name = Text(Point(horpos +25, 375), score)
            name.draw(win)
            #draw the scores
            amnt = Text(Point(horpos + 25, 340 - amountgraph), amount)
            amnt.draw(win)
    testscores.close()
main()
#file example

#histo.txt
#0/1
#1/1
#2/5
#3/4
#4/6
#5/8
#6/2
#7/9
#8/5
#9/4
#10/2
