import matplotlib.pyplot as plt
import numpy as np

# Data
advertising = [5, 8, 10, 12, 15, 18]   # in lakhs
sales = [50, 65, 80, 85, 100, 120]     # in crores

# Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(advertising, sales, color="blue", s=80, label="Companies")

# Fit regression line (to show trend)
z = np.polyfit(advertising, sales, 1)   # linear fit
p = np.poly1d(z)
plt.plot(advertising, p(advertising), "r--", label="Trend line")

# Labels & title
plt.title("Correlation between Advertising Expenditure and Sales", fontsize=14)
plt.xlabel("Advertising Expenditure (₹ lakhs)")
plt.ylabel("Sales Revenue (₹ crores)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
