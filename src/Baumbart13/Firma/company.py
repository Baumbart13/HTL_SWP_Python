import src.Baumbart13.Firma.companyAssets as cA


class Company:

    def __init__(self):
        self.persons = [cA.Person()]
        self.persons.clear()

    def add_person(self, p: cA.Person):
        if not isinstance(p, cA.Person):
            raise Exception()
        self.persons.append(p)

    def get_all_persons(self):
        return self.persons

    def get_all_mitarbeiter(self):
        ms = []
        for m in self.persons:
            if isinstance(m, cA.Mitarbeiter):
                ms.append(m)
        return ms

    def get_all_gruppenleiter(self):
        gs = []
        for g in self.persons:
            if g is isinstance(g, cA.Gruppenleiter):
                gs.append(g)
        return gs

    def get_departments(self):
        return cA.Department

    def get_number_departments(self):
        return len(self.get_departments())

    def get_gender_amount(self, s: cA.Sex):
        if isinstance(s, cA.Sex):
            raise Exception()
        gs = []
        for g in self.persons:
            if g.sex == s:
                gs.append(g)
        return gs

    def get_gender_percentage(self, s: cA.Sex):
        return len(self.get_gender_amount(s)) / len(self.persons)

    def get_persons_by_department(self, dep: cA.Department):
        if isinstance(dep, cA.Department):
            raise Exception()
        es = []
        for e in self.persons:
            if e.dep == dep:
                es.append(e)
        return es
