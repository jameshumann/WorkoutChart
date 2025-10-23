from graphics import *
import math
import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill
import json
import csv
from pathlib import Path



class WorkoutChart():

    def __init__(self, month, file_name = "jamesJan.csv"):
        self.pageWidth = 11 #inches
        self.pageHeight = 8.5

        self.leftMargin = 1
        self.rightMargin = 1
        self.topMargin = 1
        self.bottomMargin = 1

        self.labelWidth = 2.5 #width to right of margin and left of checkboxes for text labels
        self.noteHeight = 1
        self.interRowSpacing = 0.1 #vertical space between rows
        self.rowHeight = 0.20
        self.middleBuffer = 0.25 #space between top and bottom
        
        self.horizontalArea = self.pageWidth - self.leftMargin - self.rightMargin
        self.verticalArea = self.pageHeight - self.bottomMargin - self.topMargin
        self.dayWidth = (self.horizontalArea - self.labelWidth)/17 # 17 days are most possible in a row

        self.panelBottomLeft = (self.leftMargin + self.labelWidth, self.bottomMargin + self.noteHeight)
        self.panelWidth = self.pageWidth - self.rightMargin - self.panelBottomLeft[0]
        self.panelHeight = self.pageHeight - self.topMargin - self.panelBottomLeft[1]
        #print(self.panelBottomLeft)

        self.month = month
        self.note = "*Cardio = 0.25 mi run, 30 min walk, 15 min hike, 15 min bike   Core = 30 s prone plank, 15 s side plank, 10 bench situp, 30 crunch   Chest = 10 pushups, 5x 20kg RL dumbell press"

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
        ax.set_xlim([0,self.pageWidth])
        ax.set_ylim([0,self.pageHeight])
        #rectangle = plt.Rectangle((4,4), 2, 1, ec='black', fc='white')
        #ax.add_patch(rectangle)
        ax.patch.set_visible(False)
        ax.axis('off')
        self.addLines(ax, self.month)

        workoutList = [['Lunges x5(RL) 45kg', 2.25, 7],
                       ['Squats x5 45kg', 2.25, 7], #bumped up weight JUL 24
                    #    ['Pushups x10', 1.85, 1],
                       ['Shoulder x5(RL) 5kg(RL)', 3, 7],
                       ['Chest', 1.85, 1],
                       ['Curl x5(RL) 15kg(RL)', 1.00, 1],
                       ['Cardio*', 9, 7],
                       ['PT/back exercise', 1.8, 1],
                       ['Core', 1.5*1.1, 2]]

        # path = Path(__file__).parent / "jamesJan.csv"
        # with path.open() as f:
        #     test = list(csv.reader(f))
        #     print(test)
        #     print(workoutList)

        #     # workoutList = test[1:]
        #     used = test[1:len(test)]
        #     print(used)
        #     newList = []
        #     for line in used:
        #         entry = [str(line[0]), float(line[1]), float(line[2])]
        #         newList.append(entry)
            

        #     workoutList = newList
        #     print(workoutList)


        y = 0
        for wo in workoutList:
            self.addRow(ax, self.panelBottomLeft[1] + y, self.month, wo[0], wo[1], wo[2])
            y += self.rowHeight + self.interRowSpacing

        self.addTitle(ax, self.month)
        self.addNote(ax, self.note)

        plt.margins(0,0)
        plt.savefig(self.month + ".pdf")

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
    c = WorkoutChart('December')
    c.main()