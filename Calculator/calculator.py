
# Enhanced Simple Calculator with Error Handling

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

print("Welcome to Simple Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Validate choice input
choice = input("Enter choice (1/2/3/4): ")
if choice not in ['1', '2', '3', '4']:
    print("Invalid choice! Please restart the program.")
else:
    try:
        # Validate numeric input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")

    except ValueError:
        print("Error! Please enter valid numbers.")
