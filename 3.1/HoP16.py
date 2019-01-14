#HoP15.py
#Jackson Lambert 1-14-19
#Archery scorer
from graphics import *
import math
def main() :
    loop = 1
    totalscorestr = "0"
    totalscore = 0
    win = GraphWin("Archery",400,400)
    win.setCoords(0,0, 15,15)
    topText = Text(Point(7.5,14), "Click somewhere on the target").draw(win)
    scoreText = Text(Point(7.5,13),"Your current score is " + totalscorestr).draw(win)
    #White Ring
    wCircle = Circle(Point(7.5,7.5), 5)
    wCircle.setFill("white")
    wCircle.draw(win)
    #Black Ring
    blaCircle = Circle(Point(7.5,7.5), 4)
    blaCircle.setFill("black")
    blaCircle.draw(win)
    #Blue Ring
    bluCircle = Circle(Point(7.5,7.5),3)
    bluCircle.setFill("blue")
    bluCircle.draw(win)
    #Red Ring
    rCircle = Circle(Point(7.5,7.5), 2)
    rCircle.setFill("red")
    rCircle.draw(win)
    #Yellow Circle
    yCircle = Circle(Point(7.5,7.5), 1)
    yCircle.setFill("yellow")
    yCircle.draw(win)
    center = 7.5
    exitbox = Rectangle(Point(10, 2), Point(14, 1)).draw(win)
    exittext = Text(Point(12, 1.5), "Exit").draw(win)
    
    while loop == 1 :
        scoreadd = 0
        score = win.getMouse()
        #distance formula
        dist = math.sqrt((score.getX() - 7.5)**2 + (score.getY() - 7.5)**2)
        #if the distance is a certain amount of way, do this
        if dist <= 1 :
            topText.setText("You scored 9 points")
            scoreadd = 9
        elif dist <= 2 and dist > 1 :
            topText.setText("You scored 7 points")
            scoreadd = 7
        elif dist <=3 and dist > 2 :
            topText.setText("You scored 5 points")
            scoreadd = 5
        elif dist <=4 and dist > 3 :
            topText.setText("You scored 3 points")
            scoreadd = 3
        elif dist <=5 and dist > 4 :
            topText.setText("You scored 1 point")
            scoreadd = 1
        elif dist >= 6.2 and dist <= 9 :
            win.close()
        elif dist > 5 :
            topText.setText("You missed")
        totalscore = totalscore + scoreadd
        totalscorestr = str(totalscore)
        scoreText.setText("Your total current score is " + totalscorestr)

       
    
    
main()

