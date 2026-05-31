# Temperature Converter Program

# Display conversion menu
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Get user choice
choice = int(input("Enter you choice: "))

# Celsius to Fahrenheit conversion
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

# Fahrenheit to Celsius conversion
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit-32)*5/9
    print("Temperature in Celsius:", celsius)

# Handle invalid input
else:
    print("Invalid Choice")