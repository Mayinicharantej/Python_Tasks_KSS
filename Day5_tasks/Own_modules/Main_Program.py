import calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(calculator.add(num1, num2))
elif op == '-':
    print(calculator.subtract(num1, num2))
elif op == '*':
    print(calculator.multiply(num1, num2))
elif op == '/':
    print(calculator.divide(num1, num2))
else:
    print("Invalid operator")