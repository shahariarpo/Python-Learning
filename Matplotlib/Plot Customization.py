import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026, 2027])
y1 = np.array([10, 8, 18, 25, 20])
y2 = np.array([5, 8, 43, 22, 18])
y3 = np.array([32, 33, 22, 19, 13])

plt.xticks(x)           # only shows the values of the given list as the tick
plt.tick_params(axis="both",
                colors="#0000ff")

# grid lines

plt.grid(axis="both",
         linestyle="dashed",
         linewidth=1)

# pass in a dictionary of styles

line_style = dict(marker=".",
                  markersize=15,
                  markerfacecolor="#1dd3fc",
                  markeredgecolor="#0000ff",
                  linestyle="solid",
                  linewidth=2)


plt.title("Unemployment Chart",
          fontsize=20,
          family="Arial",
          fontweight="bold")

plt.xlabel("Year")
plt.ylabel("Unemployment Rate")

plt.plot(x, y1, color="#ff0000", **line_style)
plt.plot(x, y2, color="#00ff00", **line_style)
plt.plot(x, y3, color="#0000ff", **line_style)

plt.show()