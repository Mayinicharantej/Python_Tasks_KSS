# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Derived class inheriting from Employee
class Manager(Employee):
    def display_details(self):
        print(f"Manager Name: {self.name}, Salary: ₹{self.salary}")

mgr = Manager("Vikram", 95000)
mgr.display_details()