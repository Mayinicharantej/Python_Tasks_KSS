# Base staff class
class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

class Professor(Staff):
    def __init__(self, name, staff_id, department):
        super().__init__(name, staff_id)
        self.department = department

    def display(self):
        print(f"Professor: {self.name} (ID: {self.staff_id}) - Dept: {self.department}")

class LabAssistant(Staff):
    def __init__(self, name, staff_id, lab_name):
        super().__init__(name, staff_id)
        self.lab_name = lab_name

    def display(self):
        print(f"Lab Assistant: {self.name} (ID: {self.staff_id}) - Lab: {self.lab_name}")

class Administrator(Staff):
    def __init__(self, name, staff_id, role):
        super().__init__(name, staff_id)
        self.role = role

    def display(self):
        print(f"Administrator: {self.name} (ID: {self.staff_id}) - Role: {self.role}")

prof = Professor("Dr. Sharma", "P101", "Computer Science")
lab = LabAssistant("Kiran", "L204", "Data Science Lab")
admin = Administrator("Meera", "A309", "Registrar")

for member in (prof, lab, admin):
    member.display()