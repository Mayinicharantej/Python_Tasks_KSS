class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        return {"id": self.emp_id, "name": self.name, "salary": self.salary}


employees = {}

# Collect employee details and validate numeric salary input
for _ in range(2):
    emp_id = input("Enter Employee ID: ").strip()
    name = input("Enter Employee Name: ").strip()
    try:
        salary = float(input("Enter Salary: ").strip())
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        employees[emp_id] = Employee(emp_id, name, salary)
    except ValueError as e:
        print("Invalid salary input:", e)

# Persist employee records to a file
with open("employees.txt", "w") as f:
    for emp_id, emp in employees.items():
        f.write(f"{emp.emp_id},{emp.name},{emp.salary}\n")

# Display all stored employees
for emp_id, emp in employees.items():
    print(f"ID: {emp.emp_id} | Name: {emp.name} | Salary: {emp.salary}")