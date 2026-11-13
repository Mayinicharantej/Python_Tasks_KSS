import math

def is_strong(num):
    # Sum of factorial of digits equals the number itself[cite: 1]
    temp = num
    sum_fact = 0
    while temp > 0:
        digit = temp % 10
        sum_fact += math.factorial(digit)
        temp //= 10
        
    if sum_fact == num:
        print(f"{num} is a Strong number")
    else:
        print(f"{num} is not a Strong number")

# Example usage[cite: 1, 2]:
is_strong(145)