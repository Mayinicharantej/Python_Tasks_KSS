class Rectangle:
    # Set length and width via constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Compute and display area
    def calculate_area(self):
        area = self.length * self.width
        print(f"Area of Rectangle ({self.length}x{self.width}): {area}")

rect = Rectangle(10, 5)
rect.calculate_area()