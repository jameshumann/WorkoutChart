from dataclasses import dataclass
from enum import Enum, auto

class MonthName(Enum):
    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    FEBRUARY28 = "FEBRUARY(28)"
    FEBRUARY29 = "FEBRUARY(29)"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"

@dataclass
class WorkoutItem:
    name: str
    boxes: float
    days: float

@dataclass
class ChartInfo:
    goal_list: list[WorkoutItem]
    month: MonthName
    note: str

# class Ymlzer():
#     def YAML_to_dict():
#         pass
#     def dict_to_YAML():
#         pass
#     def item_to_YAML():
#         pass
#     def cha