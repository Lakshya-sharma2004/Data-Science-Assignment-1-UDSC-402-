import matplotlib.pyplot as plt
import numpy as np

# Data
data = [0.5, 1, 1, 1.5, 2, 2, 2.5, 2.5, 3, 3, 3, 3.5, 3.5, 3.5, 4, 4, 4, 4, 
        4.5, 4.5, 4.5, 5, 5, 5, 5, 5.5, 5.5, 6, 6, 6, 6, 6.5, 6.5, 6.5, 
        7, 7, 7, 7, 7.5, 7.5, 7.5, 8, 8, 8, 8, 8.5, 8.5, 9, 9, 9]

# Plot Histogram
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.hist(data, bins=np.arange(0,10,0.5), edgecolor='black', color='skyblue')
plt.xlabel("Hours on Social Media (per day)")
plt.ylabel("Number of Students")
plt.title("Distribution of Social Media Usage")

# Plot Boxplot
plt.subplot(1,2,2)
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor="lightgreen"))
plt.xlabel("Hours on Social Media (per day)")
plt.title("Boxplot of Social Media Usage")

plt.tight_layout()
plt.show()
