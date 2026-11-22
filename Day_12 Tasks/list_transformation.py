# Nested list dataset
data = [[1, 2, 3], [4, 5], [6]]

# Flatten the nested list using list comprehension
flattened = [item for sublist in data for item in sublist]

# Square only the even numbers from the flattened list
even_squares = [x ** 2 for x in flattened if x % 2 == 0]

print("Flattened list:", flattened)
print("Squares of even numbers:", even_squares)