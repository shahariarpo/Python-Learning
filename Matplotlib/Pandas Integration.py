import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Dev\Python-Learning\Matplotlib\data.csv")

type_count = df["Type1"].value_counts(ascending= True)

plt.barh(type_count.index, type_count.values,
         color= "#ff0000",
         edgecolor= "black")

plt.title("Number of Pokemon by type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()