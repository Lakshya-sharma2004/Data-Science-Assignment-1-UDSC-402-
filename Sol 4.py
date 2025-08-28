import matplotlib.pyplot as plt
import pandas as pd

# Data
departments = ["CSE","ECE","ME","CE","EE","MBA"]
placements = [180,150,120,100,80,140]

# Create DataFrame for sorting
df = pd.DataFrame({"Department": departments, "Placements": placements})
df = df.sort_values(by="Placements", ascending=False)

# Plot
plt.figure(figsize=(8,6))
bars = plt.bar(df["Department"], df["Placements"], color="skyblue", edgecolor="black")

# Annotate values
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
             str(bar.get_height()), ha='center', va='bottom', fontsize=10)

plt.title("Placement Ranking by Department", fontsize=14)
plt.xlabel("Department")
plt.ylabel("No. of Students Placed")
plt.show()
