from graphics import *
import math
import matplotlib.pyplot as plt
import numpy as np

class WorkoutChart():

    def __init__(self, month):
        self.pageWidth = 11 #inches
        self.pageHeight = 8.5

        self.leftMargin = 1
        self.rightMargin = 1
        self.topMargin = 1
        self.bottomMargin = 1

        self.labelWidth = 2.5 #width to right of margin and left of checkboxes for text labels
        self.noteHeight = 1
        self.interRowSpacing = 0.1 #vertical space between rows
        self.rowHeight = 0.25
        self.middleBuffer = 0.25 #space between top and bottom
        
        self.horizontalArea = self.pageWidth - self.leftMargin - self.rightMargin
        self.verticalArea = self.pageHeight - self.bottomMargin - self.topMargin
        self.dayWidth = (self.horizontalArea - self.labelWidth)/17 # 17 days are most possible in a row

        self.panelBottomLeft = (self.leftMargin + self.labelWidth, self.bottomMargin + self.noteHeight)
        self.panelWidth = self.pageWidth - self.rightMargin - self.panelBottomLeft[0]
        self.panelHeight = self.pageHeight - self.topMargin - self.panelBottomLeft[1]
        #print(self.panelBottomLeft)

        self.month = month


    # def init(self):
    #     pass

    def info(self):
        print("stuff")

    def main(self):
        print(self.daysInMonth("February (29)"))
        fig = plt.figure(2)
        fig.set_size_inches(11,8.5)
        #fig.clf()
        ax = fig.add_subplot(1,1,1)
        fig.subplots_adjust(left=0.1, right=.9, top=.9, bottom=0.1)
        #fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        ax.set_xlim([0,11])
        ax.set_ylim([0,8.5])
        #rectangle = plt.Rectangle((4,4), 2, 1, ec='black', fc='white')
        #ax.add_patch(rectangle)
        self.addLines(ax, self.month)

        workoutList = [['Pushups x5', 2, 7],
                       ['Pullups x10', 1, 1],
                       ['Make out w/ Rachel', 2, 1],
                       ['Cardio*', 8, 7],
                       ['Cheeseburger', 5, 31]]

        #self.addRow(ax, self.panelBottomLeft[1], 'January', workoutList[0][0], workoutList[0][1], workoutList[0][2])
        #self.addRow(ax, self.panelBottomLeft[1] + self.rowHeight + self.interRowSpacing, 'January', workoutList[1][0], workoutList[1][1], workoutList[1][2])
        #self.addRow(ax, self.panelBottomLeft[1] + self.rowHeight*2 + self.interRowSpacing*2, 'January', workoutList[2][0], workoutList[2][1], workoutList[2][2])
        #self.addRow(ax, self.panelBottomLeft[1], 'January', 'Pushups x5', 2, 7)
        y = 0
        for wo in workoutList:
            self.addRow(ax, self.panelBottomLeft[1] + y, self.month, wo[0], wo[1], wo[2])
            y += self.rowHeight + self.interRowSpacing

        plt.show()


    def daysInMonth(self,mo):
        dict = {'January':31,'February (28)':28,'February (29)':29,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
        return dict.get(mo)

    def addLines(self, axes, month):
        
        totalDays = self.daysInMonth(month)
        daysInTopRow = 14
        daysInBottomRow = totalDays - daysInTopRow

        for i in range(daysInBottomRow):
            x1 = self.panelBottomLeft[0] + (i+1)*self.dayWidth
            x2 = x1
            y1 = self.panelBottomLeft[1]
            y2 = y1 + self.panelHeight/2 - self.middleBuffer/2
            l = plt.Line2D( (x1,x2), (y1, y2), color = 'gray', linewidth=0.5, zorder = 0)
            axes.add_line(l)
            axes.text( x1 - (self.dayWidth)/2, y2 - (self.rowHeight/2), str(i + daysInTopRow), ha='center', va='center')

        for i in range(daysInTopRow):
            x1 = self.panelBottomLeft[0] + (i+1)*self.dayWidth
            x2 = x1
            y1 = self.panelBottomLeft[1] + self.panelHeight/2 + self.middleBuffer/2
            y2 = self.panelBottomLeft[1] + self.panelHeight
            l = plt.Line2D( (x1,x2), (y1, y2), color = 'gray', linewidth=0.5, zorder=0)
            axes.add_line(l)
            axes.text( x1 - (self.dayWidth)/2, y2 - (self.rowHeight/2), str(i + 1), ha='center', va='center')
        # x = self.leftMargin + self.labelWidth + 7*self.dayWidth
        # y = self.bottomMargin + self.noteHeight
        x1 = self.panelBottomLeft[0] + 7*self.dayWidth
        x2 = x1
        y1 = self.panelBottomLeft[1]
        y2 = y1 + self.panelHeight
        l = plt.Line2D( (x1,x2), (y1, y2), color = 'black', linewidth=1.5, zorder = 1)
        axes.add_line(l)
        # x = self.leftMargin + self.labelWidth + 14*self.dayWidth
        # y = self.bottomMargin + self.noteHeight
        # l = plt.Line2D( (x,x), (y, self.pageHeight-self.topMargin))
        # axes.add_line(l)
        x1 = self.panelBottomLeft[0] + 14*self.dayWidth
        x2 = x1
        y1 = self.panelBottomLeft[1]
        y2 = y1 + self.panelHeight
        l = plt.Line2D( (x1,x2), (y1, y2), color = 'black', linewidth=1.5, zorder = 1)
        axes.add_line(l)



    def addRow(self, axes, vertDistance, month, name, howMany, every):
        pd = howMany/every # boxes per day
        totalDays = self.daysInMonth(month)
        pm = pd*self.daysInMonth(month) # boxes per month
        print(pm)
        pm = np.round(pm)
        print(pm)
        pm = int(pm)
        print(pm)

        daysInTopRow = 14
        daysInBottomRow = totalDays - daysInTopRow
        
        dayWidth = (self.horizontalArea - self.labelWidth) / daysInBottomRow
        #boxWidth = dayWidth/pd
        boxWidth = (totalDays * self.dayWidth) / pm
        numBoxesInBottomRow = np.floor( (daysInBottomRow * dayWidth)/boxWidth )
        numBoxesInBottomRow = int(numBoxesInBottomRow)
        numBoxesInTopRow = pm - numBoxesInBottomRow
        
        y = vertDistance
        overlap = numBoxesInTopRow*boxWidth - self.dayWidth*daysInTopRow
        axes.text(self.leftMargin + (self.labelWidth/2), y + (self.rowHeight/2), name, ha='center', va='center')
        #axes.add_patch(t)
        for i in range(numBoxesInBottomRow):
            r = plt.Rectangle((i*boxWidth + self.rightMargin + self.labelWidth + overlap, y), boxWidth, self.rowHeight, ec='black', fc = 'lightgray', zorder = 2)
            axes.add_patch(r)

        y = vertDistance + self.panelHeight/2
        axes.text(self.leftMargin + (self.labelWidth/2), y + (self.rowHeight/2), name, ha='center', va='center')
        for i in range(numBoxesInTopRow):
            r = plt.Rectangle((i*boxWidth + self.rightMargin + self.labelWidth, y), boxWidth, self.rowHeight, ec='black', fc = 'lightgray', zorder = 2)
            axes.add_patch(r)

    
if __name__ == "__main__":
    c = WorkoutChart('January')
    c.main()



# t = np.arange(0, 2, 0.01)
# y = np.sin(4 * np.pi * t)

# # Imperative syntax
# plt.figure(1)
# plt.clf()
# plt.plot(t, y)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude (V)')
# plt.title('Sine Wave')
# plt.grid(True)

# Object oriented syntax





#fig.ylim(0,8.5)
#ax.plot(t, y)
#ax.set_xlabel('Time (s)')
#ax.set_ylabel('Amplitude (V)')
#ax.set_title('Sine Wave')
#ax.grid(True)

    
#     pd = numEx / 31.0 # per day
#     p17d = pd * 17  #per 17 days
#     exWidth = horizontalArea / p17d
#     inTopRow = math.ceil(pd*14)
#     inBottomRow = numEx - inTopRow
#     bottomOffset = inTopRow * exWidth - twoWeekWidth
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

#     for rect in range(inTopRow):
#         r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     for rect in range(inBottomRow):
#         r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     rowTop = rowBottom + interRowSpace
#     rowBottom = rowTop + rowHeight

print("Hellowortdl!")

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.


# def main():
#     docWidth = 1100 #pixels
#     docHeight = 850
#     margin = 50 # pixels, 1/2 inch
#     labelWidth = 160
#     rowHeight = 15
#     interRowSpace = 8
#     spaceBetweenRowGroups = 300
#     month = "March"
#     year = "2020"

#     rowBegin = margin + labelWidth
#     rowEnd = docWidth - margin
#     horizontalArea = rowEnd - rowBegin
#     twoWeekWidth = (horizontalArea/17) * 14
#     dayWidth = twoWeekWidth / 14
#     verticalSpace = docHeight - 2*margin

#     win = GraphWin("canvas", docWidth, docHeight)
#     win.setBackground("white")

#     rowTop = margin + 100
#     rowBottom = rowTop + rowHeight

    

#     """ Add days """
#     for day in range(31):
#         xpos = rowBegin + (day+1)*dayWidth
#         if(day > 13):
#             xpos = xpos - 14*dayWidth

#         ypos = rowTop if (day < 14) else rowTop + spaceBetweenRowGroups
        
#         l = Line(Point(xpos, ypos - margin*.333), Point(xpos, ypos))
#         l.setWidth(1)
#         l.setOutline("grey")
#         l.draw(win)

#         t = Text(Point(xpos - dayWidth*0.3, ypos - margin*0.2), day+1)
#         t.draw(win)

#     """ Add Vertical lines """
#     for line in [1,2,3,4]:
#         l = Line(Point(rowBegin + line*twoWeekWidth/2, margin),Point(rowBegin + line*twoWeekWidth/2, docHeight - margin))
#         l.setWidth(3)
#         l.draw(win)

#     """ Add rows for pushups """
#     nameEx = "Pushups x 10"
#     numPushups = 2*30 #per 30 days
#     numPushups = round(numPushups * (31/30)) # make 31 day month
#     pd = numPushups / 31.0 # per day
#     p17d = pd * 17  #per 17 days
#     pushupWidth = horizontalArea / p17d
#     inTopRow = math.ceil(pd*14)
#     inBottomRow = numPushups - inTopRow
#     bottomOffset = inTopRow * pushupWidth - twoWeekWidth
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

#     for rect in range(inTopRow):
#         r = Rectangle(Point(rowBegin + pushupWidth*rect, rowTop), Point(rowBegin + pushupWidth*(rect+1), rowBottom))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     for rect in range(inBottomRow):
#         r = Rectangle(Point(rowBegin + bottomOffset + pushupWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + pushupWidth*(rect+1), rowBottom + 300))
#         r.setFill("lightgrey")
#         r.draw(win)


#     rowTop = rowBottom + interRowSpace
#     rowBottom = rowTop + rowHeight
#     """ Add rows for Lunges """
#     nameEx = "Lunges x 10 (40 kg)"
#     numLunges =  20 #per 30-day month
#     numLunges = round(numLunges * (31/30)) # make 31 day month
#     pd = numLunges / 31.0 # per day
#     p17d = pd * 17  #per 17 days
#     lungesWidth = horizontalArea / p17d
#     inTopRow = math.ceil(pd*14)
#     inBottomRow = numLunges - inTopRow
#     bottomOffset = inTopRow * lungesWidth - twoWeekWidth
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

#     for rect in range(inTopRow):
#         r = Rectangle(Point(rowBegin + lungesWidth*rect, rowTop), Point(rowBegin + lungesWidth*(rect+1), rowBottom))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     for rect in range(inBottomRow):
#         r = Rectangle(Point(rowBegin + bottomOffset + lungesWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + lungesWidth*(rect+1), rowBottom + 300))
#         r.setFill("lightgrey")
#         r.draw(win)


#     rowTop = rowBottom + interRowSpace
#     rowBottom = rowTop + rowHeight
#     """ Add rows for PT """
#     nameEx = "PT Exercise"
#     numEx =  30*2 #per 30-day month
#     numEx = round(numEx * (31/30))
#     pd = numEx / 31.0 # per day
#     p17d = pd * 17  #per 17 days
#     exWidth = horizontalArea / p17d
#     inTopRow = math.ceil(pd*14)
#     inBottomRow = numEx - inTopRow
#     bottomOffset = inTopRow * exWidth - twoWeekWidth
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

#     for rect in range(inTopRow):
#         r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     for rect in range(inBottomRow):
#         r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     rowTop = rowBottom + interRowSpace
#     rowBottom = rowTop + rowHeight

#     """ Add rows for cardio """
#     nameEx = "Cardio"
#     numEx =  (8/7)*30 #per month
#     numEx = round(numEx * (31/30))
#     pd = numEx / 31.0 # per day
#     p17d = pd * 17  #per 17 days
#     exWidth = horizontalArea / p17d
#     inTopRow = math.ceil(pd*14)
#     inBottomRow = numEx - inTopRow
#     bottomOffset = inTopRow * exWidth - twoWeekWidth
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)

#     for rect in range(inTopRow):
#         r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     for rect in range(inBottomRow):
#         r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
#         r.setFill("lightgrey")
#         r.draw(win)

#     rowTop = rowBottom + interRowSpace
#     rowBottom = rowTop + rowHeight

#     """ Add rows for pullups """
#     nameEx = "Pullups x 5"
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8)),nameEx).draw(win)
#     Text(Point((margin + labelWidth/2),(rowTop + interRowSpace*.8 + spaceBetweenRowGroups)),nameEx).draw(win)
#     numEx =  (1.2)*30 #per month
#     numEx = round(numEx * (31/30))
#     pd = numEx / 31.0 # per day
#     p17d = pd * 17  #per 17 days
#     exWidth = horizontalArea / p17d
#     inTopRow = math.ceil(pd*14)
#     inBottomRow = numEx - inTopRow
#     bottomOffset = inTopRow * exWidth - twoWeekWidth

#     for rect in range(inTopRow):
#         r = Rectangle(Point(rowBegin + exWidth*rect, rowTop), Point(rowBegin + exWidth*(rect+1), rowBottom))
#         r.setFill("lightgrey")
#         r.draw(win)
    
#     for rect in range(inBottomRow):
#         r = Rectangle(Point(rowBegin + bottomOffset + exWidth*rect, rowTop + 300), Point(rowBegin + bottomOffset + exWidth*(rect+1), rowBottom + 300))
#         r.setFill("lightgrey")
#         r.draw(win)

#     rowTop = rowBottom + interRowSpace
#     rowBottom = rowTop + rowHeight

#     """ Add label at bottom """
#     labelx = margin + (7*dayWidth + labelWidth)/2
#     labely_t = rowTop + 300
#     labely_b = docHeight - margin
#     labely = (labely_t + labely_b)/2
#     # (rowTop + 300) + ((rowTop + 300) + (docHeight - margin)) / 2
#     bl = "Month: " + month + " " + year + "\n\n" + "Cardio = 0.25 mi jog, 1.5 volleyball game, 0.75 mi hike,\n2 mi bike ride, 1 Culver stairs, 2 city stairs"
#     t = Text(Point(labelx, labely), bl)
#     t.draw(win)

#     # saves the current TKinter object in postscript format
#     win.postscript(file="graphic.ps")
#     win.getMouse()
#     win.close()

# main()

