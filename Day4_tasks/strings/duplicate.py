my_string = "hello"
result = ""
for char in my_string:
    if char not in result:
        result = result + char
print(result)