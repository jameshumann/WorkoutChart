import workoutChartMPLOO
import json
import csv

class WorkoutUI(object):
    pass

class WorkoutDatabase(object):
    def __init__(self, folder):
        self.working_directory = folder
        print(self.working_directory)

        # read file
        with open(folder+"\\"+'jamesJan.json', 'r') as myfile:
            data=myfile.read()

        # parse file
        obj = json.loads(data)
        print(obj)
        print(obj["note"])
        obj["note"] = obj["note"] + "NEWNEWNEW"

        with open(folder+"\\"+'jamesJan2.json', 'w') as json_file:
            json.dump(obj, json_file)


if __name__ == "__main__":
    c = WorkoutDatabase("C:\\Users\\shotq\\Documents\\Personal Projects\\Workout chart\\git\\workoutchart\\chart_json_databases")