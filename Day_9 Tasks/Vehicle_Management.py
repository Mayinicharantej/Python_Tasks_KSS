# Parent class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

# Child class for cars
class Car(Vehicle):
    def display(self):
        print(f"Car -> Brand: {self.brand}, Top Speed: {self.speed} km/h")

# Child class for bikes
class Bike(Vehicle):
    def display(self):
        print(f"Bike -> Brand: {self.brand}, Top Speed: {self.speed} km/h")

car = Car("Toyota", 180)
bike = Bike("Yamaha", 150)

car.display()
bike.display()