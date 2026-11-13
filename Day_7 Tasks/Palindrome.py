def is_palindrome(num):
    # Reads the same forward and backward[cite: 2]
    original = str(num)
    reversed_str = original[::-1]
    
    if original == reversed_str:
        print(f"{num} is a Palindrome number")
    else:
        print(f"{num} is not a Palindrome number")

# Example usage[cite: 2]:
is_palindrome(121)