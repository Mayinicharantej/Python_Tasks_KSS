class Student:
    # Initialize student attributes
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    # Print student details
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_number}, Marks: {self.marks}")

# Create three student objects
s1 = Student("Aarav", 101, 88)
s2 = Student("Diya", 102, 94)
s3 = Student("Rohan", 103, 79)

# Display each student's details
for student in (s1, s2, s3):
    student.display()