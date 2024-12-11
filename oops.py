# OOPs stand for Object Oriented Programming
# How to create a class
class Books:
    def gain_knowlage(self):
        print("Books are used to gain knowlage")

# how to create object of class
b1 = Books()
# how to access the method of class
b1.gain_knowlage()

# getter and setter
class Phone:
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def set_price(self,price):
        self.price = price
    def get_price(self):
        return self.price
p1 = Phone()
p1.set_color("blue")
p1.set_price(20000)
print(p1.get_color())
print(p1.get_price())

class Vehicle:
    def can_drive(self,speed):
        self.speed = speed
        print(speed)

v1 = Vehicle()
v1.can_drive(60)