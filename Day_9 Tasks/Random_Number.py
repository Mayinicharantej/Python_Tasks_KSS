# Yield numbers lazily from 1 to n
def number_generator(n):
    for i in range(1, n + 1):
        yield i

# Iterate and print one number at a time
for num in number_generator(5):
    print(num)