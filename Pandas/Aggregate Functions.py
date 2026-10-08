import pandas as pd

df = pd.read_csv(r"D:\Dev\Python-Learning\Pandas\data.csv")


# whole dataframe
print(df.sum(numeric_only= True))
print(df.mean(numeric_only= True))
print(df.min(numeric_only= True))
print(df.max(numeric_only= True))
print(df.count())

# specific row
print(df["Height"].sum(numeric_only= True))
print(df["Weight"].mean(numeric_only= True))


# group object

group = df.groupby("Type1")
print(group["Height"].max())
print(group["Height"].min())
print(group["Height"].count())