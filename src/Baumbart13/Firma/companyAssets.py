from enum import Enum


class Sex(Enum):
    Indeterminable = 0,
    Male = 1,
    FeMale = 2


class Department(Enum):
    NoDepartment = 0,
    EconomicalEngineering = 1,
    BiomedicalEngineering = 2,
    ElectricalEngineering = 3,
    MechanicalEngineering = 4


class Person:
    def __init__(self, dep: Department = Department.NoDepartment, sex: Sex = Sex.Indeterminable):
        self.dep = dep
        self.sex = sex


class Mitarbeiter(Person):
    def __init__(self, dep: Department = Department.NoDepartment, sex: Sex = Sex.Indeterminable):
        super().__init__(dep, sex)


class Gruppenleiter(Mitarbeiter):
    def __init__(self, dep: Department = Department.NoDepartment, sex: Sex = Sex.Indeterminable):
        super().__init__(dep, sex)