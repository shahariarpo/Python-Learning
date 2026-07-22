import pandas as pd

data = [10, 20, 30, 40]
dictionary = {"A": 120,
              "B": 230,
              "C": 150,
              "D": 434,}

series_col = pd.Series(data, index=['a', 'b', 'c', 'd'])
series_dict = pd.Series(dictionary)

series_col.loc['b'] = 200

print(series_col.loc['b'])
print(series_col.iloc[0])
print(series_col[series_col > 15])
print(series_dict[series_dict <= 150])
