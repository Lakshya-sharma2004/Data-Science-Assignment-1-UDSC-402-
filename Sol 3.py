import matplotlib.pyplot as plt

# Data
days = [1,2,3,4,5,6,7,8,9,10]
company_A = [120,125,123,128,130,132,131,135,140,138]
company_B = [80,82,81,84,88,90,87,89,91,92]

# Plot
plt.figure(figsize=(10,6))
plt.plot(days, company_A, marker='o', label="Company A", color="blue")
plt.plot(days, company_B, marker='s', label="Company B", color="green")

plt.title("Stock Prices of Company A & B Over 10 Days", fontsize=14)
plt.xlabel("Day")
plt.ylabel("Stock Price (₹)")
plt.xticks(days)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
