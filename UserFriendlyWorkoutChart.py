import workoutChartMPLOO
import json
import csv

class WorkoutUI(object):
    pass

class WorkoutDatabase(object):
    def __init__(self, folder):
        self.working_directory = folder
        print(self.working_directory)


if __name__ == "__main__":
    c = WorkoutDatabase("C:\\Users\\shotq\\Documents\\Personal Projects\\Workout chart\\git\\workoutchart")