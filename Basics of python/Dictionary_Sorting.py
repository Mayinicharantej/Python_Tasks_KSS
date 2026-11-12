students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
print(sorted_students[0])
print(sorted_students[1])