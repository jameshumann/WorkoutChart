#workoutChart.p
from graphics import *
import math

print("Hellowortdl!")

def main():
    docWidth = 1100 #pixels
    docHeight = 850
    margin = 50 # pixels, 1/2 inch
    labelWidth = 160
    rowHeight = 15
    interRowSpace = 8
    spaceBetweenRowGroups = 300
    month = "March 2020"

    rowBegin = margin + labelWidth
    rowEnd = docWidth - margin
    horizontalArea = rowEnd - rowBegin
    twoWeekWidth = (horizontalArea/17) * 14
    dayWidth = twoWeekWidth / 14
    verticalSpace = docHeight - 2*margin

    win = GraphWin("canvas", docWidth, docHeight)
    win.setBackground("white")

    rowTop = margin + 100
    rowBottom = rowTop + rowHeight

    

    """ Add days """
    for day in range(31):
        xpos = rowBegin + (day+1)*dayWidth
        if(day > 13):
            xpos = xpos - 14*dayWidth

        ypos = rowTop if (day < 14) else rowTop + spaceBetweenRowGroups
        
        l = Line(Point(xpos, ypos - margin*.333), Point(xpos, ypos))
        l.setWidth(1)
        l.setOutline("grey")
        l.draw(win)

        t = Text(Point(xpos - dayWidth*0.3, ypos - margin*0.2), day+1)
        t.draw(win)

    """ Add Vertical lines """
    for line in [1,2,3,4]:
        l = Line(Point(rowBegin + line*twoWeekWidth/2, margin),Point(rowBegin + line*twoWeekWidth/2, docHeight - margin))
        l.setWidth(3)
        l.draw(win)

    """ Add rows for pushups """
    nameEx = "Pushups x 10"
    numPushups = 2*30 #per 30 days
    numPushups = round(numPushups * (31/30)) # make 31 day month
    pd = numPushups / 31.0 # per day
    p17d = pd * 17  #per 17 days
    pushupWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numPushups - inTopRow
    bottomOffset = inTopRow * pushupWidth - twoWeekWidth
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

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
    nameEx = "Lunges x 10 (40 kg)"
    numLunges =  20 #per 30-day month
    numLunges = round(numLunges * (31/30)) # make 31 day month
    pd = numLunges / 31.0 # per day
    p17d = pd * 17  #per 17 days
    lungesWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numLunges - inTopRow
    bottomOffset = inTopRow * lungesWidth - twoWeekWidth
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

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
    numEx =  30*2 #per 30-day month
    numEx = round(numEx * (31/30))
    pd = numEx / 31.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

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
    numEx = round(numEx * (31/30))
    pd = numEx / 31.0 # per day
    p17d = pd * 17  #per 17 days
    exWidth = horizontalArea / p17d
    inTopRow = math.ceil(pd*14)
    inBottomRow = numEx - inTopRow
    bottomOffset = inTopRow * exWidth - twoWeekWidth
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

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
    Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)
    numEx =  (1.2)*30 #per month
    numEx = round(numEx * (31/30))
    pd = numEx / 31.0 # per day
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

    """ Add label at bottom """
    labelx = margin + (7*dayWidth + labelWidth)/2
    labely_t = rowTop + 300
    labely_b = docHeight - margin
    labely = (labely_t + labely_b)/2
    # (rowTop + 300) + ((rowTop + 300) + (docHeight - margin)) / 2
    bl = "Month: " + month + "\n\n" + "Cardio = 0.25 mi jog, 1.5 volleyball game, 1 mi hike,\n2 mi bike ride, 1 Culver stairs, 2 city stairs"
    t = Text(Point(labelx, labely), bl)
    t.draw(win)

    

    win.getMouse()
    win.close()

main()

