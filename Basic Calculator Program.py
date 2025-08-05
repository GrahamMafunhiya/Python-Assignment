# Get user input
A = float(input("Enter the first number: "))
B = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == "+":
    result = A + B
    print(f"{A} + {B} = {result}")
elif operation == "-":
    result = A - B
    print(f"{A} - {B} = {result}")
elif operation == "*":
    result = A * B
    print(f"{A} * {B} = {result}")
elif operation == "/":
    if B != 0:
        result = A / B
        print(f"{A} / {B} = {result}")
    else:
        print("Error: Cannot divide by 0")
else:
    print("Invalid operation. Please choose +, -, *, or /.")