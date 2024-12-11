# Constructor is a special type of method, through which we can assign values to the variable when object created
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def emp_deatils(self):
        print(self.name)
        print(self.age)
        print(self.salary)

e1 = Employee('abc',20,20000)
e1.emp_deatils()