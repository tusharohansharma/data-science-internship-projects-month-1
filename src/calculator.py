# Simple Calculator Program

# Display operation menu
print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user choice
choice = int(input("Enter your choice: "))

# Get input numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform addition
if choice == 1:
    result = num1 + num2
    print("Result:", result)

# Perform subtraction
elif choice == 2:
    result = num1 - num2
    print("Result:", result)

# Perform multiplication
elif choice == 3:
    result = num1 * num2
    print("Result:", result)

# Perform division
elif choice == 4:
    result = num1 / num2
    print("Result:", result)

# Handle invalid input
else:
    print("Invalid Choice")