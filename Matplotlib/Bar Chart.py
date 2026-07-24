import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 6, 4, 1])

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.bar(categories, values, color="#0000ff")

plt.show()