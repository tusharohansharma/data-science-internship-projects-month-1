# Import matplotlib library
import matplotlib.pyplot as plt

# Create database
students = ["Aman", "Riya", "Karan"]
marks = [85, 90, 78]

# Add bar chart
plt.bar(students, marks)

# Add chart title
plt.title("Students Marks Comparison")

# Add axis labels
plt.xlabel("Students")
plt.ylabel("Marks")

# Display chart
plt.show()