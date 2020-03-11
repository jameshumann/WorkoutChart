#workoutChart.p
from graphics import *
import math

print("Hellowortdl!")

def main():
    docWidth = 1100 #pixels
    docHeight = 850
    margin = 50 # pixels, 1/2 inch
    labelWidth = 160
    rowBegin = margin + labelWidth
    rowEnd = docWidth - margin
    horizontalArea = rowEnd - rowBegin
    twoWeekWidth = (horizontalArea/17) * 14
    rowHeight = 15
    interRowSpace = 8

    win = GraphWin("canvas", docWidth, docHeight)
    win.setBackground("white")

    rowTop = margin + 100
    rowBottom = rowTop + rowHeight

    """ Add Vertical lines """
    for line in [1,2,3,4]:
        l = Line(Point(rowBegin + line*twoWeekWidth/2, margin),Point(rowBegin + line*twoWeekWidth/2, docHeight - margin))
        l.setWidth(3)
        l.draw(win)

    """ Add rows for pushups """
    numPushups = 2*30 #per 30 days
    pd = numPushups / 30.0 # per day
    p17d = pd * 17  #per 17 days
    pushupWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numPushups - inTopRow
    bottomOffset = inTopRow * pushupWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + pushupWidth*rect, rowTop), Point(rowBegin + pushupWidth*(rect+1), rowBottom))
        r.setFill("lightgrey")
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + pushupWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + pushupWidth*(rect+1), rowBottom + 300))
        r.setFill("lightgrey")
        r.draw(win)


    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for Lunges """
    numLunges =  30/1.5 #per month
    numLunges = round(numLunges)
    pd = numLunges / 30.0 # per day
    p17d = pd * 17  #per 17 days
    lungesWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numLunges - inTopRow
    bottomOffset = inTopRow * lungesWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + lungesWidth*rect, rowTop), Point(rowBegin + lungesWidth*(rect+1), rowBottom))
        r.setFill("lightgrey")
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + lungesWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + lungesWidth*(rect+1), rowBottom + 300))
        r.setFill("lightgrey")
        r.draw(win)


    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for PT """
    nameEx = "PT Exercise"
    numEx =  30*2 #per month
    numEx = round(numEx)
    pd = numEx / 30.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
        r.setFill("lightgrey")
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
        r.setFill("lightgrey")
        r.draw(win)
    
    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for cardio """
    nameEx = "Cardio"
    numEx =  (8/7)*30 #per month
    numEx = round(numEx)
    pd = numEx / 30.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
        r.setFill("lightgrey")
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
        r.setFill("lightgrey")
        r.draw(win)

    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for pullups """
    nameEx = "Pullups x 5"
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
    numEx =  (1.2)*30 #per month
    numEx = round(numEx)
    pd = numEx / 30.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
        r.setFill("lightgrey")
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
        r.setFill("lightgrey")
        r.draw(win)

    

    win.getMouse()
    win.close()

main()

