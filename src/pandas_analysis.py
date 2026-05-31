# Import pandas library
import pandas as pd

# Create sample dataset
data = {
    "Name": ["Aman", "Riya", "Karan"],
    "Marks": [80, 90, 78]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Display dataset
print(students_df)