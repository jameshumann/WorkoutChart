import sys
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFileDialog, QLineEdit, QSizePolicy, QComboBox
from PySide6.QtGui import QDoubleValidator

from workoutChartMPLOO import WorkoutChart, Ymlzer
from DataClasses import ChartInfo, MonthName, WorkoutItem
from dataclasses import asdict

DEFAULT_SIZE = (400,400)
                                                     
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.new_file_window:FileEditWidget = None
        # self.load_file_window:

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # self.click_button = QtWidgets.QPushButton("Click me!")
        self.load_file_button = QtWidgets.QPushButton("Load File")
        self.create_new_file_button = QtWidgets.QPushButton("Create New File")
        # self.text = QtWidgets.QLabel("Hello World",
                                    #  alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.click_button)
        self.layout.addWidget(self.load_file_button)
        self.layout.addWidget(self.create_new_file_button)

        # self.click_button.clicked.connect(self.magic)
        self.load_file_button.clicked.connect(self.pick_file_to_load)
        self.create_new_file_button.clicked.connect(self.create_new_file)

    # @QtCore.Slot()
    # def magic(self):
        # self.text.setText(random.choice(self.hello))

    @QtCore.Slot()
    def create_new_file(self):
        # self.text.setText(random.choice(self.hello))
        print("File editor clicked")
        few = FileEditWidget()
        self.new_file_window = few
        self.new_file_window.resize(*DEFAULT_SIZE)
        self.new_file_window.show() 


    @QtCore.Slot()
    def pick_file_to_load(self):
        base_directory="saved_configs"
        print("File button clicked")
        path = os.getcwd() + "/" + base_directory
        file_picker = QFileDialog(self)
        file_picker.setDirectory(path)
        file_picker.setFileMode(QFileDialog.ExistingFiles)
        # file_picker.setNameFilter("Images (*.png *.jpg)")
        file_picker.setViewMode(QFileDialog.List)
        # file_picker.exec()
        file_to_load = file_picker.getOpenFileName()[0]
        # print (file_picker.getOpenFileName())
        print(file_to_load)
        # woc = WorkoutChart(absolute_file_path=file_to_load)
        # woc.main()
        initial_chart = Ymlzer.load_file(file_to_load)
        self.new_file_window = FileEditWidget(initial_chart)
        self.new_file_window.resize(*DEFAULT_SIZE)
        self.new_file_window.show() 

class FileEditWidget(QtWidgets.QWidget):
    def __init__(self, initial_chart:WorkoutChart = None):
        super().__init__()
        self.setWindowTitle("Create or edit a workout plan.")

        self.expanding_space = QtWidgets.QVBoxLayout()
        self.note_box = QtWidgets.QTextEdit()
        self.save_button = QtWidgets.QPushButton("💾 Save Workout")
        self.preview_button = QtWidgets.QPushButton("🧐 Preview")
        self.pdf_button = QtWidgets.QPushButton("📃 Make PDF")
        self.month_combo = QComboBox(placeholderText="Select Month")

        self.month_combo.addItems([m.value for m in MonthName])

        # for m in MonthName:
        #     print(m)
        #     self.month_combo.addItem(m)

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.entry_list = []
        self.new_goal_button = QtWidgets.QPushButton("➕ Add New Goal")
        lbg = QtWidgets.QLabel("Workout Name", alignment=QtCore.Qt.AlignCenter)
        lbg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        lbb = QtWidgets.QLabel("# of boxes", alignment=QtCore.Qt.AlignCenter)
        lbb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        lbd = QtWidgets.QLabel("per # of days", alignment=QtCore.Qt.AlignCenter)
        lbd.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        gdb = QtWidgets.QHBoxLayout()
        gdb.addWidget(lbg, 0)
        gdb.addWidget(lbb, 0)
        gdb.addWidget(lbd, 0)
        # self.load_file_button = QtWidgets.QPushButton("Load File")
        # self.text = QtWidgets.QLabel("Hello World",
        #                              alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(QtWidgets.QLabel("Month"))
        self.layout.addWidget(self.month_combo)
        # self.layout.setSpacing(4)
        # self.layout.setContentsMargins(10, 10, 10, 10)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.new_goal_button)
        self.layout.addLayout(gdb, 0)
        self.layout.addLayout(self.expanding_space)
        self.layout.addWidget(self.new_goal_button)
        self.layout.addWidget(QtWidgets.QLabel("Optional Note:"))
        self.layout.addWidget(self.note_box)
        self.layout.addStretch(1)
        botom_button_layout = QtWidgets.QHBoxLayout()
        botom_button_layout.addWidget(self.preview_button)
        botom_button_layout.addWidget(self.save_button)
        botom_button_layout.addWidget(self.pdf_button)
        # self.layout.addWidget(self.save_button)
        self.layout.addLayout(botom_button_layout)
        
        self.new_goal_button.clicked.connect(self.add_new_row)
        self.preview_button.clicked.connect(self.show_preview)
        self.save_button.clicked.connect(self.save_file)
        self.pdf_button.clicked.connect(self.save_PDF)

        if initial_chart == None:
            pass
        else:
            self.month_combo.setCurrentText(initial_chart.month.value)
            for i in initial_chart.goal_list:
                lll = self.add_new_row()
                lll[0].setText(i.name)
                lll[1].setText(str(i.boxes))
                lll[2].setText(str(i.days))
            self.note_box.setText(initial_chart.note)

    @QtCore.Slot()
    def add_new_row(self):
        # row_of_three = QtWidgets.QWidget()
        # row_of_three.layout = 
        row_of_three = QtWidgets.QHBoxLayout()
        self.expanding_space.addLayout(row_of_three)
        text_name = "name of workout"
        name_box = QtWidgets.QLineEdit()  #text=text_name)
        text_boxes = "number of boxes"
        boxes_box = QtWidgets.QLineEdit()  #text=text_boxes)
        boxes_box.setValidator(QDoubleValidator()) 
        text_days = "per number of days"
        days_box = QtWidgets.QLineEdit()  #text=text_days)
        days_box.setValidator(QDoubleValidator()) 
        row_of_three.addWidget(name_box)
        row_of_three.addWidget(boxes_box)
        row_of_three.addWidget(days_box)

        curr_list = [name_box, boxes_box, days_box]

        self.entry_list.append( curr_list )
        return curr_list

        # self.layout.addStretch(1)
        
        # self.layout.addWidget(self.load_file_button)

        # self.click_button.clicked.connect(self.magic)
        # self.load_file_button.clicked.connect(self.pick_file_to_load)

    def entries_to_ChartInfo(self) -> ChartInfo:
        items = []
        for e in self.entry_list:
            items.append( WorkoutItem(e[0].text(), float(e[1].text()), float(e[2].text())) )
            # print(e[0].text(), float(e[1].text()), float(e[2].text()))
        info = ChartInfo(goal_list = items,
                         month     = MonthName[self.month_combo.currentText()],
                         note      = self.note_box.toPlainText())
        return info

    @QtCore.Slot()
    def save_file(self):
        base_directory="saved_configs"
        print("File saver clicked")
        path = os.getcwd() + "/" + base_directory
        # file_picker = QFileDialog(self)
        # file_picker.setDirectory(path)
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",              # Dialog title
            path,                       # Default path
            "YAML Files (*.yaml)"  # File filters
        )

        items = []
        to_save = self.entries_to_ChartInfo()
        # for e in self.entry_list:
        #     items.append( WorkoutItem(e[0].text(), float(e[1].text()), float(e[2].text())) )
        #     # print(e[0].text(), float(e[1].text()), float(e[2].text()))
        # to_save = ChartInfo(goal_list = items,
        #                     month     = self.month_combo.currentText(),
        #                     note      = "")
        print(to_save)

        ym = Ymlzer()
        ym.save_chart(to_save, file_path)
            # print()

    def create_new_blank_entry(self):
        nl = QLineEdit(self)

    @QtCore.Slot()
    def show_preview(self):
        # base_directory="saved_charts"
        # print("PDF saver clicked")
        print("Preview clicked")
        info = self.entries_to_ChartInfo()
        chart = WorkoutChart(info = info, load_from_info=True)
        # chart.main()
        chart.make_graphics()
        # path = os.getcwd() + "/" + base_directory
        # file_picker = QFileDialog(self)
        # file_picker.setDirectory(path)
        # save_path, _ = QFileDialog.getSaveFileName(
        #     self,
        #     "Save a PDF",              # Dialog title
        #     path,                       # Default path
        #     "PDF Files (*.pdf)"  # File filters
        # )

    @QtCore.Slot()
    def save_PDF(self):
        base_directory="saved_charts"
        print("PDF saver clicked")
        path = os.getcwd() + "/" + base_directory
        # file_picker = QFileDialog(self)
        # file_picker.setDirectory(path)
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save a PDF",              # Dialog title
            path,                       # Default path
            "PDF Files (*.pdf)"  # File filters
        )

        info = self.entries_to_ChartInfo()
        chart = WorkoutChart(info = info, load_from_info=True)
        # chart.main()
        chart.make_PDF(save_path)


        # items = []
        # for e in self.entry_list:
        #     items.append( WorkoutItem(e[0].text(), float(e[1].text()), float(e[2].text())) )
        #     # print(e[0].text(), float(e[1].text()), float(e[2].text()))
        # to_save = ChartInfo(goal_list = items,
        #                     month     = self.month_combo.currentText(),
        #                     note      = "")
        # print(to_save)

        # ym = Ymlzer()
        # ym.save_chart(to_save, file_path)
            # print()

def get_main_window():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(*DEFAULT_SIZE)
    widget.show()
    return app, widget



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(*DEFAULT_SIZE)
    widget.show()

    sys.exit(app.exec())