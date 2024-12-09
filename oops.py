# OOPs stand for Object Oriented Programming
# How to create a class
class Books:
    def gain_knowlage(self):
        print("Books are used to gain knowlage")

b1 = Books()
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
p1.get_color()
p1.get_price()