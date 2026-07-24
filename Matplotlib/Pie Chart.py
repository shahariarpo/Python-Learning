import numpy as np
import matplotlib.pyplot as plt

categories = ["Shower", "Toilet", "Sink", "Drinking", "Other"]
values = np.array([5, 2, 3, 4, 1])
colors = ["red", "green", "blue", "yellow", "skyblue"]

plt.title("Water Consumption")
plt.pie(values,
        labels = categories,
        colors = colors,
        autopct="%1.2f%%",
        explode= [0.1, 0, 0, 0, 0],
        shadow= True,
        startangle= 90)
plt.show()