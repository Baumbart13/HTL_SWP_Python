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
    def __init__(self, dep: Department = Department.EconomicalEngineering, sex: Sex = Sex.Male):
        self.dep = dep
        self.sex = sex


class Mitarbeiter(Person):
    def __init__(self, dep: Department = Department.BiomedicalEngineering, sex: Sex = Sex.FeMale):
        super().__init__(dep, sex)


class Gruppenleiter(Mitarbeiter):
    def __init__(self, dep: Department = Department.MechanicalEngineering, sex: Sex = Sex.Male):
        super().__init__(dep, sex)