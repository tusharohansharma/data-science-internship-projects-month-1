# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 65, 80, 90],
    "Attendance": [60, 65, 70, 80, 90]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Create pairplot
sns.pairplot(students_df)

# Add display
plt.show()