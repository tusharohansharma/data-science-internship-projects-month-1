# Import pandas library
import pandas as pd

# Create dataset
data = {
    "Name": ["Aman", "Riya", "Karan"],
    "Marks": [85, 90, 78]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Calculate average marks
average_marks = students_df["Marks"].mean()

# Display result
print("Average Marks:", average_marks)