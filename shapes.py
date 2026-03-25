import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def display(self):
        print(f"Circle (r={self.radius}) | Area: {self.area()} | Perimeter: {self.perimeter()}")

    def formula(self):
        print("Circle → Area = πr² | Perimeter = 2πr")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return round(self.length * self.width, 2)

    def perimeter(self):
        return round(2 * (self.length + self.width), 2)

    def display(self):
        print(f"Rectangle ({self.length}x{self.width}) | Area: {self.area()} | Perimeter: {self.perimeter()}")

    def formula(self):
        print("Rectangle → Area = L×W | Perimeter = 2(L+W)")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side ** 2, 2)

    def perimeter(self):
        return round(4 * self.side, 2)

    def display(self):
        print(f"Square (s={self.side}) | Area: {self.area()} | Perimeter: {self.perimeter()}")

    def formula(self):
        print("Square → Area = s² | Perimeter = 4s")


class Triangle:
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return round(0.5 * self.base * self.height, 2)

    def perimeter(self):
        return round(self.base + self.side1 + self.side2, 2)

    def display(self):
        print(f"Triangle | Area: {self.area()} | Perimeter: {self.perimeter()}")

    def formula(self):
        print("Triangle → Area = ½bh | Perimeter = sum of sides")