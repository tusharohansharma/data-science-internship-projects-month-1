# Sum of Squares Program

# Define function to calculate sum of squares
def sum_of_squares(numbers):
    total = 0

    for number in numbers:
        total = total + number ** 2
        
    return total

# Input data
numbers_list = [1, 2, 3, 4]

# Function call
result = sum_of_squares(numbers_list)

# Display result
print("Sum of Squares:", result)