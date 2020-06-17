class Employee:
    #global no_of_employees
    no_of_employees=0
    salarylist = []
    def __init__(self, name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.salarylist.append(salary)
        self.department = department
        Employee.no_of_employees +=1

    def average(self):
        sum_num = 0
        for t in self.salarylist:
            sum_num = sum_num + t

        avg = sum_num / len(self.salarylist)
        return avg


class FullTimeEmployee(Employee):
    pass

p1 = FullTimeEmployee("Harun","Gente",121,"DevOps Engineer")
p2 = FullTimeEmployee("Deepak","Gente",131,"Cloud Engineer")
FullTimeEmployee("kumar","Gente",141,"software developer")
print(p1.average())
print(p1.name)
print(p1.salarylist)
print(p1.no_of_employees)