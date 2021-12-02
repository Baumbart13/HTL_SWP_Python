import companyAssets


class Firma:
    smolPenis = ""

    def __init__(self):
        self.persons = [companyAssets.Person]

    def add_person(self, p: companyAssets.Person):
        pass

    def add_mitarbeiter(self, m: companyAssets.Mitarbeiter):
        pass

    def add_gruppenleiter(self, g: companyAssets.Gruppenleiter):
        pass

    def get_all_persons(self):
        return self.persons

    def get_all_mitarbeiter(self):
        ms = []
        for m in self.persons:
            if m is isinstance(m, companyAssets.Mitarbeiter):
                ms.append(m)
        return ms

    def get_all_gruppenleiter(self):
        gs = []
        for g in self.persons:
            if g is isinstance(g, companyAssets.Gruppenleiter):
                gs.append(g)
        return gs

    def get_departments(self):
        return companyAssets.Department
