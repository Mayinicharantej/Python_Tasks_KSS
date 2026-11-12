import random
import math

secret_number = random.randint(1, 50)
attempts = 5

for i in range(attempts):
    guess = int(input("Enter your guess (1-50): "))
    if guess == secret_number:
        print("Correct! You won!")
        break
    else:
        diff = math.fabs(secret_number - guess)
        print("Wrong! You are", diff, "away from the number.")
else:
    print("Game Over! The correct number was", secret_number)