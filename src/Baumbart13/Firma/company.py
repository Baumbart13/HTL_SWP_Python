import companyAssets as cA


class Company:

    def __init__(self):
        self.persons = []
        self.department_counters = {}
        [self.department_counters.setdefault(i, 0) for i in cA.Department]

    def add_person(self, p: cA.Person):
        if not isinstance(p, cA.Person):
            raise Exception()
        self.persons.append(p)
        self.department_counters[p.dep] += 1

    def add_persons(self, l: list):
        for p in l:
            self.add_person(p)

    def get_all_persons(self):
        return self.persons

    def get_all_mitarbeiter(self):
        ms = [m for m in self.persons if isinstance(m, cA.Mitarbeiter)]
        return ms

    def get_all_gruppenleiter(self):
        gs = [g for g in self.persons if isinstance(g, cA.Gruppenleiter)]
        return gs

    def get_departments(self):
        return cA.Department

    def get_department_with_most_employees(self):
        return max(self.department_counters, key=self.department_counters.get)

    def get_gender_amount(self, s: cA.Sex):
        if not isinstance(s, cA.Sex):
            raise Exception()
        gs = [g for g in self.persons if g.sex == s]
        return gs

    def get_gender_percentage(self, s: cA.Sex):
        return 100 * len(self.get_gender_amount(s)) / len(self.persons)

    def get_persons_by_department(self, dep: cA.Department):
        if not isinstance(dep, cA.Department):
            raise Exception()
        es = [e for e in self.persons if e.dep == dep]
        return es


if __name__ == '__main__':
    employees = [cA.Person(), cA.Person(), cA.Person(), cA.Mitarbeiter(), cA.Mitarbeiter(), cA.Mitarbeiter(),
                 cA.Gruppenleiter(), cA.Gruppenleiter(), cA.Gruppenleiter()]
    c = Company()
    c.add_persons(employees)

    print(f'Number of all persons: {len(c.get_all_persons())}\n'
        f'Number of all Mitarbeiter: {len(c.get_all_mitarbeiter())}\n'
        f'Number of all Gruppenleiter {len(c.get_all_gruppenleiter())}')
    print(f'Number of all departments: {len(c.get_departments())}')
    print(f'Department with most employees: {c.get_department_with_most_employees()}')
    print(f'Percentage of females males: {c.get_gender_percentage(cA.Sex.FeMale):{3}.{6}}%')
