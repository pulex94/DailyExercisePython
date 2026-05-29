import pandas as pd

df = pd.read_csv("store_sales.csv")
df["revenue"] = df["quantity"] * df["price"]
revenue_store = df.groupby("store")["revenue"].sum()
print(revenue_store)
revenue_category = df.groupby("category").sum()
print(revenue_category["revenue"])
total_value = df.groupby(["store", "category"])["revenue"].sum()
print(total_value)
best_performing_store = df.groupby("store")["revenue"].sum()
best_performing_store_name = best_performing_store.idxmax()
best_performing_store_value = round(best_performing_store.max())
print(
    f"Best selling store is: {best_performing_store_name} with: {best_performing_store_value}€ revenue!"
)
best_performing_city = df.groupby("city")["revenue"].sum()
best_performing_name = best_performing_city.idxmax()
best_performing_value = best_performing_city.max()
print(best_performing_name, best_performing_value)
df["date"] = pd.to_datetime(df["date"])
monthly_date = df["date"].dt.month
monthly_revenue = df.groupby(df["date"].dt.month)["revenue"].sum()
print(monthly_revenue)
print(
    f"Final Summary:\nMost revenue store is: {best_performing_store_name}\nMost performing city: {best_performing_name}"
)
