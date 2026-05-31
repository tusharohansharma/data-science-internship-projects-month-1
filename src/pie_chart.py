# Import matplotlib library
import matplotlib.pyplot as plt

# Create dataset
products = ["Laptop", "Mobile", "Tablet", "Accessories"]
sales = [40, 30, 20, 10]

# Create pie chart
plt.pie(sales, labels=products, autopct="%1.1f%%")

# Add chart title
plt.title("Product Sales Distribution")

# Display chart
plt.show()