students = {"Alice": 85, "Bob": 95, "Charlie": 78}
best_student = max(students, key=students.get)
print(best_student)