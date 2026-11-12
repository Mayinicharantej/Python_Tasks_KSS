# Create a list of dictionaries where each dictionary represents an employee's details
employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# Find the employee with the highest salary using the max() function and a lambda function
highest_paid = max(employees, key=lambda x: x["salary"])
print(highest_paid)

# Use a list comprehension to filter out employees whose salary is greater than 35,000
filtered_employees = [emp for emp in employees if emp["salary"] > 35000]
print(filtered_employees)

# Calculate the total salary by adding up all employee salaries using a generator expression
total_salary = sum(emp["salary"] for emp in employees)
# Divide the total salary by the total number of employees to get the average salary
avg_salary = total_salary / len(employees)
print(avg_salary)

# Use a list comprehension to extract only the "name" values from each dictionary into a new list
names = [emp["name"] for emp in employees]
print(names)