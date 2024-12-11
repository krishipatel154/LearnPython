# Single inheritance
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(self.age)
        print(self.name)


class Employee(Human):
    def emp_details(self):
        print("child class")


e1 = Employee('abc', 34)
e1.show_data()
e1.emp_details()


# Multilevel inheritance
class Animal:
    def __init__(self, eyes, feet):
        self.eyes = eyes
        self.feet = feet
    def show_details(self):
        print("Eyes of animals: ",self.eyes)
        print("Feet of animals: ",self.feet)

class Dog(Animal):
    def dog_details(self):
        print("Details of dogs..")

class Cat(Animal):
    def cat_details(self):
        print("Details of cats..")

d1 = Dog(2,4)
d1.dog_details()
d1.show_details()

c1 = Cat(2,4)
c1.cat_details()
c1.show_details()

class Phone:
    def __init__(self, name, price, memory):
        self.name = name
        self.price = price
        self.memory = memory

    def show_details(self):
        print("Name is: ", self.name)
        print("Price is: ", self.price)
        print("Memory is: ", self.memory)

# multiple inheritance
class Subject:
    def __init__(self,fname):
        self.fname = fname
    def first_subject(self):
        print("First subject")

class Subject2:
    def __init__(self,sname):
        self.sname = sname
    def second_subject(self):
        print("Second subject")

class Student(Subject, Subject2):
    def __init__(self, fname, sname, name):
        super().__init__(fname)
        super().__init__(sname)
        self.name = name
    def student(self):
        print("student")

s1 = Student('php','java','savu')
s1.student()
s1.first_subject()
s1.second_subject()


# overwrite constructor
class Vivo(Phone):
    def __init__(self, dual_camera):
        super().__init__(name='abc' ,price=20,memory='64GB')
        self.dual_camera = dual_camera

    def vivo_details(self):
        print("Dual Camera: ", self.dual_camera)


p1 = Phone("vivo", 20000, '32GB')
p1.show_details()

v1 = Vivo(True)
v1.vivo_details()
v1.show_details()
