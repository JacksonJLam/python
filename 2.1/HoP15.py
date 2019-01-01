#HoP15.py
#Writes a program that plots test scores
#Jackson Lambert 1-1-19
from graphics import *

def main():
    # get the file name
    fileName = input("What file are the test scores in?")
    # open the files
    testscores = open(fileName, "r")
    #Loop for the amount of student test scores
    loops = eval(testscores.readline(1))
    #set the height of the graph depending on test scores
    height = loops * 125
    win = GraphWin('Graphs',500, height)
    for line in range(loops + 1) :
            #Read the line
            scores = testscores.readline()
            #split the values in the line
            name,score = scores.split("/")
            #the vertical position of the bars and names
            vertpos = line * 85
            score = eval(score)
            scoregraph = score * 3
            #draw the bar
            bar = Rectangle(Point(100, vertpos), Point(scoregraph + 100, vertpos + 50))
            bar.draw(win)
            bar.setFill("green")
            #draw the names
            name = Text(Point(50, vertpos + 25), name)
            name.draw(win)
            #draw the scores
            drawnscore = Text(Point(scoregraph + 120, vertpos + 25), score)
            drawnscore.draw(win)
            #if it is the loop line, dont draw 
            if line == 0 :
                bar.undraw()
                name.undraw()
                drawnscore.undraw()
     #closes the graph
    Text(Point(100, 40), "Click twice to exit").draw(win)
    win.getMouse()
    win.getMouse()
    win.close()
    testscores.close()
    #close the file
    testscores.close()
main()

#Example of the file being scraped for data
#6/0
#Grimsley/20
#Lambert/99
#MoBamba/77
#Lenin/45
#SickoMode/6 
#Animey/89
