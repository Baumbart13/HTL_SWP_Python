from enum import Enum


class Sex(Enum):
    Indeterminable = 0,
    Male=1,
    FeMale=2


class Department(Enum):
    NoDepartment = 0,
    EconomicalEngineering = 1,
    BiomedicalEngineering = 2,
    ElectricalEngineering = 3,
    MechanicalEngineering = 4


class Person:
    def __init__(self):
        self.dep = Department.NoDepartment
        self.sex = Sex.Indeterminable


class Mitarbeiter(Person):
    def __init__(self):
        super().__init__()


class Gruppenleiter(Mitarbeiter):
    def __init__(self):
        super().__init__()