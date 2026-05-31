# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 65, 80, 90]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Create dashboard layout
fig, axes = plt.subplots(2, 3, figsize=(10, 8))

# Line Plot
axes[0, 0].plot(students_df["Study_Hours"], students_df["Marks"])
axes[0, 0].set_title("Line Plot")

# Bar Chart
axes[0, 1].bar(students_df["Study_Hours"], students_df["Marks"])
axes[0, 1].set_title("Bar Chart")

# Scatter Plot
axes[1, 0].scatter(students_df["Study_Hours"], students_df["Marks"])
axes[1, 0].set_title("Scatter Plot")

# Histogram
axes[1, 1].hist(students_df["Marks"])
axes[1, 1].set_title("Histogram")

# Pie Chart
axes[0, 2].pie(students_df["Marks"], labels=students_df["Study_Hours"], autopct="%1.1f%%")
axes[0, 2].set_title("Pie Chart")

# Heatmap
correlation_matrix = students_df.corr()

sns.heatmap(correlation_matrix, annot=True, ax=axes[1, 2])
axes[1, 2].set_title("Heatmap")

# Adjust layout
plt.tight_layout()

# Show dashboard
plt.show()