#ES shapes

#import what you need
import math

#make a class for cirlce 
class Circle:
    #defing init with self and radius 
    def __init__(self, radius):
        self.radius = radius
    #make are be self and make py times the radius squared 
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    #make a funtionf for perimeter and calculate it using times and math
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
    #return the output 
    def __str__(self):
        return f"Circle (r={self.radius}) | Area: {self.area()} | Perimeter: {self.perimeter()}"

#make a class for rectangles 
class Rectangle:
    #make the init thing with self lenght width and make those thing equals themselfs
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #make a funtion for area and make the math for it 
    def area(self):
        return round(self.length * self.width, 2)
    #make a funtion for perimeter and make the math for it 
    def perimeter(self):
        return round(2 * (self.length + self.width), 2)
    #make a 
    def __str__(self):
        return f"Rectangle ({self.length}x{self.width}) | Area: {self.area()} | Perimeter: {self.perimeter()}"

#make a class for squares
class Square:
    #make the init thing and make side be side 
    def __init__(self, side):
        self.side = side
    #make a funtion area and make the math for it 
    def area(self):
        return round(self.side ** 2, 2)
    #make a funtion for perimeter and make the math for it 
    def perimeter(self):
        return round(4 * self.side, 2)
    #make a pritn option
    def __str__(self):
        return f"Square (s={self.side}) | Area: {self.area()} | Perimeter: {self.perimeter()}"

#make a class for triangle 
class Triangle:
    #make init with the base height side 1 side 2 and make themselfes equal each other
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    #make a funtion for area 
    def area(self):
        #return the math equation
        return round(0.5 * self.base * self.height, 2)
    #make a funtion for perimeter 
    def perimeter(self):
        #return the math eqution
        return round(self.base + self.side1 + self.side2, 2)
    #print the outputs
    def __str__(self):
        return f"Triangle | Area: {self.area()} | Perimeter: {self.perimeter()}"