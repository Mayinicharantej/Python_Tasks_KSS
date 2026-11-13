def is_armstrong(num):
    # Sum of the cubes of its digits equals the number itself[cite: 1]
    temp = num
    sum_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp //= 10
        
    if sum_cubes == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

# Example usage[cite: 1]:
is_armstrong(153)