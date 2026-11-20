import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Circle area formula
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Rectangle area formula
    def area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # Triangle area formula
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(7), Rectangle(4, 6), Triangle(10, 5)]

# Call the same area() method across different shape types
for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()}")