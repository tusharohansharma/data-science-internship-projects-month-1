# Filter Even Numbers from List

# Original data
numbers = [10, 15, 20, 25, 30, 35, 40]

# Filter even numbers
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# Display filtered data
print("Even Numbers:", even_numbers)