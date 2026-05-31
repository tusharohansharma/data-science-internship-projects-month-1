# Import matplotlib library
import matplotlib.pyplot as plt

# Create dataset
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 35, 31, 29]

# Create line plot
plt.plot(days, temperature)

# Add chart title
plt.title("Temperature Trend")

# Add axis labels
plt.xlabel("Days")
plt.ylabel("Temperature")

# Display plot
plt.show()