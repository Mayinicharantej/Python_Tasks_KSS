def is_prime(num):
    # A Prime number has only two factors: 1 and itself[cite: 2]
    if num <= 1:
        print(f"{num} is not a Prime number")
        return
        
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            
    print(f"Factors = {factors}")
    if len(factors) == 2:
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is not a Prime number")

# Example usage[cite: 2]:
is_prime(7)