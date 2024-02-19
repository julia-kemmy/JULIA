

import math

class Square:
    def __init__(self,side_length):
        self.side_length = side_length
    def calculate_area(self):
        return self.side_length ** 2
    
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height

square = Square(6)
print("Area of a square:", square.calculate_area())

rectangle = Rectangle(4, 5)
print("Area of  rectangle:", rectangle.calculate_area())

circle =Circle(7)
print("Area of a circle:", circle.calculate_area())

triangle = Triangle(3, 6)
print("Area of a triangle:",triangle.calculate_area())