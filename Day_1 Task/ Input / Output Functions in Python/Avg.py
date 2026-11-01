# Get three numbers from the user
first_text = input("Enter the first number: ")
second_text = input("Enter the second number: ")
third_text = input("Enter the third number: ")

# Convert the text inputs into decimal numbers (floats)
num1 = float(first_text)
num2 = float(second_text)
num3 = float(third_text)

# Calculate the total sum of all three numbers
total_sum = num1 + num2 + num3

# Calculate the average by dividing the total sum by 3
average = total_sum / 3

# Display the final result
print("The average of the three numbers is:", average)