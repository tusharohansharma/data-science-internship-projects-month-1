# Import pandas library
import pandas as pd

# Create dataset with missing values
data = {
    "Name": ["Aman", "Riya", "Karan"],
    "Marks": [85, None, 78]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Remove rows with missing values
cleaned_data = students_df.dropna()

# Display cleaned dataset
print(cleaned_data)