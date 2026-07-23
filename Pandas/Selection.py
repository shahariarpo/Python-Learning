from operator import index

import pandas as pd

df = pd.read_csv(r"D:\Dev\Python-Learning\Pandas\data.csv", index_col="Name")


# selection by column
print(df["Name"].to_string())
print(df[["Name", "Legendary"]].to_string())                   # multiple columns

# selection by rows
print(df.loc["Bulbasaur":"Pikachu", ["Height", "Legendary"]])       # search in range
