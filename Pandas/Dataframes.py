import pandas as pd

data = {
    "Name": ["John", "Alex", "Jane"],
    "Age": [18, 21, 23]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
print(df)
print(df.loc["Employee 2"])


# add a new column
df["Job"] = ["Cook", "Waiter", "Manager"]
print(df)


# add a new rows
new_rows = pd.DataFrame([{"Name": "Tony", "Age": 26, "Job": "Cashier"},
                         {"Name": "Steve", "Age": 36, "Job": "Waiter"},
                         {"Name": "Peter", "Age": 21, "Job": "Delivery"}],
                       index=["Employee 4", "Employee 5", "Employee 6"])
df = pd.concat([df, new_rows])

print(df)