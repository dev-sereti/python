#Addition
def addition(a,b):
    return a+b

#Subtraction
def subraction(a,b):
    return a-b

#Multiplication
def multiplication(a,b):
    return a*b

# Division
def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Error, number has to be greater than 0"

print("Welcome to Simple Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = ("Enter choice (1/2/3/4): ")

if choice not in ['1', '2', '3', '4']:
    print("Invalid choice! Please restart the program.")

