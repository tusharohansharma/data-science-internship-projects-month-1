# Import matplotlib library
import matplotlib.pyplot as plt

# Create database
study_hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 80, 90]

# Create scatter plot
plt.scatter(study_hours, marks)

# Add chart title
plt.title("Study Hours vs Marks")

# Add axis labels
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Display chart
plt.show()