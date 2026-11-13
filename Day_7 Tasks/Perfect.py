def is_perfect(num):
    # Sum of proper divisors equals the number[cite: 3]
    if num <= 0:
        print(f"{num} is not a Perfect number")
        return
        
    divisors = [i for i in range(1, num) if num % i == 0]
    
    if sum(divisors) == num:
        print(f"Divisors: {', '.join(map(str, divisors))}")
        print(f"Sum {'+'.join(map(str, divisors))}={num}")
        print(f"{num} is a Perfect number")
    else:
        print(f"{num} is not a Perfect number")

# Example usage[cite: 3]:
is_perfect(6)