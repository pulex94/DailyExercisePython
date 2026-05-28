import pandas as pd

df = pd.read_csv("dirty_data.csv")
rows_prima = len(df)
# print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df.dropna(subset=["name"], inplace = True)
average = df["salary"].mean()
df["salary"] = df["salary"].fillna(average)
df["department"] = df["department"].str.title()
df["email"] = df["email"].str.lower()
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df.loc[df["age"] > 100, "age"] = pd.NA
df.dropna(subset=["age"], inplace = True)
df.to_csv("cleared_dirty_data", index=False)
rows_dopo = len(df)
print(f"Prima erano presenti: {rows_prima}\nDopo la pulizia: {rows_dopo}")