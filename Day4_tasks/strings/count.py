my_string = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in my_string:
    if char in vowels:
        count = count + 1
print(count)