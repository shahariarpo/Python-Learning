import pandas as pd

df = pd.read_csv(r"D:\Dev\Python-Learning\Pandas\data.csv")

# drop irrelevant columns

df = df.drop(columns=["Legendary", "No"])
print(df)

# drop missing data

df = df.dropna(subset=["Type2"])
df = df.fillna({"Type2": "None"})
print(df.to_string())

# fix inconsistent data

df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE"})
print(df.to_string())


# standardize text

df["Name"] = df["Name"].str.upper()
print(df)

# fix datatype

df["Legendary"] = df["Legendary"].astype(bool)
print(df.to_string())


# remove duplicate values

df = df.drop_duplicates()
print(df)