import pandas as pd

# Read the CSV with pandas
df = pd.read_csv("sales.csv")
# Print the first 5 rows
print(df.head())
# # Print basic info
print(df.info())
# Add a new column "revenue" (quantity * price)
df["revenue"] = df.quantity * df.price
# Find the product with highest revenue
highest_revenue = df["revenue"].idxmax()
highest_revenue_name = df.loc[highest_revenue, "product"]
print(highest_revenue_name)
# Find the product with lowest revenue
lowest_revenue = df["revenue"].idxmin()
lowest_revenue_name = df.loc[lowest_revenue, "product"]
print(lowest_revenue_name)
# Calculate total revenue per category
category_revenue = df.groupby("category")["revenue"].sum()
print(category_revenue)
# Print a clean summary report
print(f"Summary:\nProduct with most sell: {highest_revenue_name}\nProduct with lowest sells: {lowest_revenue_name}")