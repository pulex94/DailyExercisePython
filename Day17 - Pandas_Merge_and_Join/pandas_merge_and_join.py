import pandas as pd

df_customer = pd.read_csv("customer.csv")
df_orders = pd.read_csv("orders.csv")
df_products = pd.read_csv("products.csv")

customer_id = pd.merge(df_customer, df_orders, on="customer_id")
product = pd.merge(customer_id, df_products, on="product")
product["revenue"] = product["quantity"] * product["price"]
total_revenue_per_customer = product.groupby("customer_id")["revenue"].sum()
total_revenue_per_city = product.groupby("city")["revenue"].sum()
best_customer = product.groupby("name")["revenue"].sum()
best_customer_name = best_customer.idxmax()
best_customer_revenue = best_customer.max()
print(
    f"Summary:\nBest Customer is: {best_customer_name} with: {best_customer_revenue}\nTotal revenue per customer id: \n{total_revenue_per_customer}\n Total revenue per city: \n{total_revenue_per_city}"
)
