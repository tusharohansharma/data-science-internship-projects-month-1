# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create database
data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 65, 80, 90],
    "Attendance": [60, 65, 70, 80, 90]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Create correlation matrix
correlation_matrix = students_df.corr()

# Create heatmap
sns.heatmap(correlation_matrix, annot=True)

# Add chart title
plt.title("Correlation Heatmap")

# Display chart
plt.show()