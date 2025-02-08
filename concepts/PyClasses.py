

class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        self._base_salary = 0

class Designer (Employee):


    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, base_salary):
        self._base_salary = base_salary


d = Designer("des1",10,'designer')
d.base_salary = 10
print(d.base_salary)