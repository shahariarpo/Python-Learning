import pandas as pd

df = pd.read_csv(r"D:\Dev\Python-Learning\Pandas\data.csv")

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] >= 100]
legendary_pokemon = df[df["Legendary"] == 1]
water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"] == "Water")]

print(tall_pokemon)
print()
print(heavy_pokemon)
print()
print(legendary_pokemon)
print()
print(water_pokemon)