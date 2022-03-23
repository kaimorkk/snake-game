class Employees:
    def __init__(self,name,age,salary):
        self.name='kelvin'
        self.age='25'
        self.salary='67500'
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
employees=Employees('name','age','salary')
print(employees.get_name())
print(employees.get_age())
print(employees.get_salary())
