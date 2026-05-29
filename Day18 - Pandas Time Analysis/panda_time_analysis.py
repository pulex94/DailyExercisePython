import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")

df1 = pd.merge(customers, orders, on="customer_id")
df2 = pd.merge(df1, products, on="product")
df2["order_date"] = pd.to_datetime(df2["order_date"])
df2["revenue"] = df2["quantity"] * df2["price"]
df2["montly"] = df2["order_date"].dt.month_name()
df2["day"] = df2["order_date"].dt.day_name()
df2["year"] = df2["order_date"].dt.year
montly_revenue = df2.groupby(df2["montly"])["revenue"].sum()
city_revenue = df2.groupby(df2["city"])["revenue"].sum()
best_customer_name = df2.groupby(df2["name"])["revenue"].sum().idxmax()
best_customer_value = df2.groupby(df2["name"])["revenue"].sum().max()
best_day_name = df2.groupby(df2["day"])["revenue"].sum().idxmax()
best_day_value = df2.groupby(df2["day"])["revenue"].sum().max()
total_revenue = df2["revenue"].sum()
orders_len = len(df2["order_id"])
average_order_revenue = total_revenue / orders_len
filtered_date = df2[(df2["montly"] == "February") & (df2["year"] == 2025)]
top_products = df2.groupby("product")["revenue"].sum().sort_values(ascending=False)
top_products.index.name = None
print(
    f"Summary:\n"
    f"The best customer is: {best_customer_name} with: {best_customer_value}€\n"
    f"The best revenue day is: {best_day_name} with: {best_day_value}\n"
    f"Our most sold products are:\n{top_products.head(3)}"
)
