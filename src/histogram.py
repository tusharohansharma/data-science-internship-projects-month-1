# Import matplotlib library
import matplotlib.pyplot as plt

# Create dataset
marks = [40, 50, 60, 70, 80, 85, 90, 95]

# Create histogram
plt.hist(marks)

# Add chart title
plt.title("Marks Distribution")

# Add axis labels
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Display chart
plt.show()