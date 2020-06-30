from graphics import *
import math
import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill

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
        self.note = "*Cardio = 0.25 mi run, 30 min walk, 15 min hike, 1 Culver stairs, 2 Mar Vista stairs, 2 mi bike + blah + a a a a a a a a a a a blah + blah + blah+ blah adflasdfl;kj blah+ blah+ blah"

    # def init(self):
    #     pass

    def info(self):
        print("stuff")

    def main(self):
        #print(self.daysInMonth("February (29)"))
        fig = plt.figure(2)
        fig.set_size_inches(11,8.5)
        #fig.clf()
        ax = fig.add_subplot(1,1,1)
        #fig.subplots_adjust(left=0.1, right=.9, top=.9, bottom=0.1)
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        ax.set_xlim([0,11])
        ax.set_ylim([0,8.5])
        #rectangle = plt.Rectangle((4,4), 2, 1, ec='black', fc='white')
        #ax.add_patch(rectangle)
        self.addLines(ax, self.month)

        workoutList = [['Lunges x10', 2, 3],
                       ['Pushups x5', 2, 7],
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

        self.addTitle(ax, self.month)
        self.addNote(ax, self.note)

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
            axes.text( x1 - (self.dayWidth)/2, y2 - (self.rowHeight/2), str(i + daysInTopRow + 1), ha='center', va='center')

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
        
        #dayWidth = (self.horizontalArea - self.labelWidth) / daysInBottomRow
        dayWidth = (self.horizontalArea - self.labelWidth) / 17 #17 is maximum number of days in bottom row
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

    def addTitle(self,axes,mo):
        x = self.leftMargin + self.horizontalArea/2
        y = self.panelBottomLeft[1] - self.rowHeight
        axes.text( x, y, mo, ha='center', va='center', fontweight='bold')

    def addNote(self, axes, note):
        x = self.leftMargin
        y = self.panelBottomLeft[1] - 2*self.rowHeight
        axes.text(x, y, fill(note, width = round(self.horizontalArea*13.5)), ha='left', va='top') # ~11 characters per inch



if __name__ == "__main__":
    c = WorkoutChart('July')
    c.main()