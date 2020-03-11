#workoutChart.p
from graphics import *
import math

print("Hellowortdl!")

def main():
    docWidth = 1100 #pixels
    docHeight = 850
    margin = 50 # pixels, 1/2 inch
    rowBegin = margin + 50
    rowEnd = docWidth - margin
    horizontalArea = rowEnd - rowBegin
    twoWeekWidth = (horizontalArea/17) * 14
    rowHeight = 15
    interRowSpace = 8

    win = GraphWin("canvas", docWidth, docHeight)

    rowTop = rowBegin + 50
    rowBottom = rowTop + rowHeight

    """ Add rows for pushups """
    numPushups = 2*31 #per month
    pd = numPushups / 31.0 # per day
    p17d = pd * 17  #per 17 days
    pushupWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numPushups - inTopRow
    bottomOffset = inTopRow * pushupWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + pushupWidth*rect, rowTop), Point(rowBegin + pushupWidth*(rect+1), rowBottom))
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + pushupWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + pushupWidth*(rect+1), rowBottom + 300))
        r.draw(win)


    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for Lunges """
    numLunges =  31/1.5 #per month
    numLunges = round(numLunges)
    pd = numLunges / 31.0 # per day
    p17d = pd * 17  #per 17 days
    lungesWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numLunges - inTopRow
    bottomOffset = inTopRow * lungesWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + lungesWidth*rect, rowTop), Point(rowBegin + lungesWidth*(rect+1), rowBottom))
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + lungesWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + lungesWidth*(rect+1), rowBottom + 300))
        r.draw(win)


    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for PT """
    nameEx = "PT Exercise"
    numEx =  31*2 #per month
    numEx = round(numEx)
    pd = numEx / 31.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
        r.draw(win)
    
    rowTop = rowBottom + interRowSpace
    rowBottom = rowTop + rowHeight
    """ Add rows for cardio """
    nameEx = "Cardio"
    numEx =  (8/7)*31 #per month
    numEx = round(numEx)
    pd = numEx / 31.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth

    for rect in range(inTopRow):
        r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
        r.draw(win)
    
    for rect in range(inBottomRow):
        r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
        r.draw(win)

    win.getMouse()
    win.close()

main()

