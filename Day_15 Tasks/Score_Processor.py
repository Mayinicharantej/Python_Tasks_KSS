import math

records = [("Asha", 75), ("Ravi", 45), ("Meena", 88), ("Kiran", 50), ("Neha", 92)]

# Convert list of tuples into a dictionary
scores_dict = dict(records)

# Filter students scoring strictly above 50
above_50 = {}
for name, score in scores_dict.items():
    if score > 50:
        above_50[name] = score

# Compute class average using math.fsum for precision
average_score = math.fsum(scores_dict.values()) / len(scores_dict)

# Save output to a text file
with open("student_results.txt", "w") as f:
    f.write("Students scoring above 50:\n")
    for name, score in above_50.items():
        f.write(f"{name}: {score}\n")
    f.write(f"\nAverage score: {average_score:.2f}\n")

print("Above 50:", above_50)
print("Average:", average_score)