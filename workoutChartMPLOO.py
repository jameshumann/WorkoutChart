from graphics import *
from DataClasses import MonthName, WorkoutItem, ChartInfo
import math
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import asdict, dataclass
from textwrap import fill
import json
import csv
import yaml
from pathlib import Path
import argparse
# from workout_GUI import MyWidget

class WorkoutChart():
    # def __init__(self, month = "January", file_folder = "saved_configs", file_name = "demo.yaml", absolute_file_path = "err", load_from_file = True, info:ChartInfo = None, load_from_info = True):
    def __init__(self, info:ChartInfo = None):
        # load_from_info = True
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

        # self.month = month
        # self.note = "*Cardio = 0.25 mi run, 30 min walk, 15 min hike, 15 min bike   Core = 30 s prone plank, 15 s side plank, 10 bench situp, 30 crunch   Chest = 10 pushups, 5x 20kg RL dumbell press"

        self.file_info:ChartInfo = None
        self.loaded_workout_list: list[WorkoutItem]
        self.month_name: MonthName
        # self.using_file = load_from_file
        self.file_info:ChartInfo
        self.file_info = info
        self.using_file = True

    def make_graphics(self, preview = True) -> plt.Figure:
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
        self.addLines(ax, self.file_info.month.value)

        y = 0
        for wo in self.file_info.goal_list:
            self.addRow(ax, self.panelBottomLeft[1] + y,
                        self.file_info.month,
                        wo.name, wo.boxes, wo.days)
            y += self.rowHeight + self.interRowSpacing

        self.addTitle(ax, self.file_info.month.value)
        self.addNote(ax, self.file_info.note)

        plt.margins(0,0)
        # plt.savefig(save_path)
        if preview:
            plt.show()

        return fig

    def make_PDF(self, save_path:str, preview = False):
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
        self.addLines(ax, self.file_info.month.value) #self.month)

        y = 0
        for wo in self.file_info.goal_list:
            self.addRow(ax, self.panelBottomLeft[1] + y,
                        self.file_info.month,
                        wo.name, wo.boxes, wo.days)
            y += self.rowHeight + self.interRowSpacing

        self.addTitle(ax, self.file_info.month.value)
        self.addNote(ax, self.file_info.note)

        plt.margins(0,0)
        print("Saving PDF to:")
        print(save_path)
        plt.savefig(save_path)

        if preview:
            plt.show()


    def daysInMonth(self,mo):
        dict = {'January':31,'February (28)':28,'February (29)':29,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
        return dict.get(mo)
    
    def daysInEnumMonth(self,mo:MonthName):
        dict = {MonthName.JANUARY:31,
                MonthName.FEBRUARY:28,
                MonthName.FEBRUARY28:28,
                MonthName.FEBRUARY29:29,
                MonthName.MARCH:31,
                MonthName.APRIL:30,
                MonthName.MAY:31,
                MonthName.JUNE:30,
                MonthName.JULY:31,
                MonthName.AUGUST:31,
                MonthName.SEPTEMBER:30,
                MonthName.OCTOBER:31,
                MonthName.NOVEMBER:30,
                MonthName.DECEMBER:31}
        return dict.get(mo)

    def addLines(self, axes, month):
        if self.using_file:
            totalDays = self.daysInEnumMonth(self.file_info.month)
        else:
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
        if self.using_file:
            totalDays = self.daysInEnumMonth(self.file_info.month)
        else:
            totalDays = self.daysInMonth(month)
        pm = pd*totalDays # boxes per month
        # print(pm)
        pm = np.round(pm)
        # print(pm)
        pm = int(pm)
        # print(pm)

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

class Ymlzer():
    @staticmethod
    def save_chart(info:ChartInfo, file_path:str):
        dic = asdict(info)
        # print(dic)
        dic["month"] = dic["month"].value
        # print(dic)
        # tex = yaml.safe_dump(dic)
        print("Saving chart to:")
        print(file_path)
        with open(file_path, "w") as f:
            yaml.safe_dump(dic, f, sort_keys=False, indent = 2)
    
    @staticmethod
    def load_file(file_path):
        ans:ChartInfo
        with open(file_path, "r") as file:
            loaded_dict = yaml.safe_load(file)
            # print(file)
            print("Loading from file:")
            print(file_path)
            print(loaded_dict) 
            # print(loaded_dict)
            gl = []
            for a in loaded_dict["goal_list"]:
                n = WorkoutItem(name  = a["name"],
                                boxes = a["boxes"],
                                days  = a["days"])
                gl.append(n)

            ans = ChartInfo(goal_list = gl,
                            month     = MonthName(loaded_dict["month"]),
                            note      = loaded_dict["note"])
        # print(loaded_dict)
        return ans


def run_hardcoded():
    ## Inputs ##
    month = MonthName.JANUARY # Use Enum
    workoutList = [['Lunges x5(RL) 45kg', 2.25, 7],
                    ['Squats x5 45kg', 2.25, 7],
                    ['Shoulder x5(RL) 5kg(RL)', 3, 7],
                    ['Chest', 1.85, 1],
                    ['Curl x5(RL) 15kg(RL)', 1.00, 1],
                    ['Cardio*', 9, 7],
                    ['PT/back exercise', 1.8, 1],
                    ['Core', 1.5*1.1, 2]]
    note = "*Cardio = 0.25 mi run, 30 min walk, 15 min hike, 15 min bike   Core = 30 s prone plank, 15 s side plank, 10 bench situp, 30 crunch   Chest = 10 pushups, 5x 20kg RL dumbell press"
    output_name = "HC_chart.pdf" # Include .pdf extension
    #############

    ## Leave the rest of the function alone ##
    items = []
    for e in workoutList:
        items.append( WorkoutItem(e[0], e[1], e[2]) )
    info = ChartInfo(goal_list = items,
                     month     = month,
                     note      = note)
    chart = WorkoutChart(info=info) #, load_from_info=True)
    chart.make_graphics(preview = True)
    chart.make_PDF("saved_charts/" + output_name)

if __name__ == "__main__":
    ## Can be by hardcoding parameters in run_hardcoded function ##
    RUN_HARDCODED = False
    if RUN_HARDCODED:
        print("Running hardcoded...")
        run_hardcoded()
        sys.exit(0)

    ## Typical (better) way to run using YAML files, GUI, and/or CLI ##
    parser = argparse.ArgumentParser(description="Start up the workout chart editor, or run fully from CLI.")
    # , help="Run without any arguments to generate demo file."
    parser.add_argument("--input_file", type=Path, help="Input YAML file, including .yaml extension, from default folder")
    parser.add_argument("--output_file", type=Path, help="Output PDF file, including .pdf extension, saved in default folder")
    parser.add_argument("--demo", action="store_true", help="Run demo and save to default output folder.")
    args = parser.parse_args()

    if args.demo:
        print("Running demo, using demo.yaml...")
        a = Ymlzer.load_file("saved_configs/demo.yaml")
        c = WorkoutChart(info=a)
        c.make_PDF("saved_charts/demo_output.pdf", preview=True)
        sys.exit(0)
    elif (args.input_file == None) ^ (args.output_file == None):
        print("Invalid, must have input and output, or neither.")
        sys.exit(0)
    elif (args.input_file != None) and (args.output_file != None):
        print("Running headless with user-specified YAML file...")
        # path_to_input = Path("saved_configs/")
        a = Ymlzer.load_file(args.input_file)
        b = WorkoutChart(info=a)
        b.make_PDF(args.output_file)
        sys.exit(0)
    else:
        import workout_GUI
        print("Running GUI...")
        app, widget = workout_GUI.get_main_window()
        app.exec()
        sys.exit(0)
