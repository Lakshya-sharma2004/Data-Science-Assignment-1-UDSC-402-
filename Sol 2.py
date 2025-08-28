import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
actual = [12,18,25,45,75,160,210,190,120,80,40,15]
normal = [15,20,30,50,70,150,200,200,110,90,50,20]

# Calculate deviation
deviation = np.array(actual) - np.array(normal)

# Plot
plt.figure(figsize=(10,6))
bars = plt.bar(months, deviation, color=['skyblue' if d>=0 else 'salmon' for d in deviation])

# Highlight values
plt.axhline(0, color='black', linewidth=1)
plt.title("Deviation of Actual Rainfall from Normal Values", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Deviation (mm)")

# Annotate values on bars
for bar, dev in zip(bars, deviation):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (2 if dev>=0 else -6),
             str(dev), ha='center', va='bottom' if dev>=0 else 'top', fontsize=9)

plt.show()
