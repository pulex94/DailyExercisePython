import pandas as pd

# Read the CSV with pandas
df = pd.read_csv("sales.csv")
# Print the first 5 rows
print(df.head())
# Print basic info
print(df.info())
# Add a new column "revenue" (quantity * price)
df["revenue"] = df.quantity * df.price
# Find the product with highest revenue
print(df.idxmax())
# Find the product with lowest revenue
print(df.idxmin())
# Calculate total revenue per category
print(df.groupby("category")["revenue"].sum())
