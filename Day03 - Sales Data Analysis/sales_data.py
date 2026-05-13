# 1. Read the CSV file
import csv
with open("sales.csv") as file:
    reader = csv.DictReader(file)
    dates = []
    for line in reader:
        dates.append(line)  
# 2. Calculate total revenue per product (quantity * price)
    print("Calculate total revenue per product (quantity * price)")
    productTotalRevenue = {}
    for element in dates:
        price = float(element["price"])
        quantity = int(element["quantity"])
        totalRevenue = round(price * quantity, 2)
        productTotalRevenue[element["product"]] = totalRevenue
        print(f" {element["product"]} - {totalRevenue}")
# 3. Calculate total revenue per category
    print("Calculate total revenue per category")
    categoryRevenue = {}
    for element in dates:
        category = element["category"]
        price = float(element["price"])        
        if category not in categoryRevenue:
            categoryRevenue[category] = 0
        categoryRevenue[category] += price
    for category, revenue in categoryRevenue.items():
        print(f" {category}: {revenue}")
# 4. Find the best selling product (highest revenue)
    print("Find the best selling product (highest revenue)")
    bestSellingproduct = ""
    counter = 0
    for key, value in productTotalRevenue.items():
        if value > counter:
            counter = value
            bestSellingproduct = key
    print(f" {bestSellingproduct}")
# 5. Find the worst selling product (lowest revenue)
    print("Find the worst selling product (lowest revenue)")
    worstSellingproduct = ""
    counter = 999999999
    for key, value in productTotalRevenue.items():
        if value < counter:
            counter = value
            worstSellingproduct = key
    print(f" {worstSellingproduct}")
# 6. Print a clean summary report
    print(f"Summary:\n Best Selling Product = {bestSellingproduct}\n Worst Selling Product = {worstSellingproduct}")