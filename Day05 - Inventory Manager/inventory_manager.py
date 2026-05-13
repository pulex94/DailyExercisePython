# 1. Read the TXT file and parse each line
with open("inventory.txt", "r") as f:
    dates = f.readlines()
# 2. Create a list of dictionaries with product data
    inventory = []
    for riga in dates:
        riga = riga.strip()
        parti = riga.split(": ")
        prodotto = {
            "product":parti[0].strip(),
            "quantity":parti[1].strip(),
            "min_stock":parti[2].strip(),
            "price":parti[3].strip()
        }
        inventory.append(prodotto)
    del inventory[0]
# 3. Identify products below minimum stock (quantity < min_stock)
    belowStock = []
    for element in inventory:
        if int(element["quantity"]) < int(element["min_stock"]):
            belowStock.append(element["product"])
            print(f"Below minimum stock: {element["product"]}")
# 4. Calculate how many units need to be ordered (min_stock - quantity)
    toOrder = int(element["min_stock"]) - int(element["quantity"])
    for element in inventory:
        if toOrder > 0 :
            print(f"{element["product"]} - To order: {toOrder}")     
# 5. Calculate the reorder cost for each product (units_to_order * price)
    totalCost = 0
    for element in inventory:
        toOrder = int(element["min_stock"]) - int(element["quantity"])
        reorderCost = int(toOrder) * float(element["price"])
        if toOrder > 0:
            print(f"Reorder cost for {element["product"]} is: {round(reorderCost)}")
# 6. Calculate the total reorder cost
            totalCost = totalCost + reorderCost
    print(f"Total Reorder cost: {totalCost}")
# 7. Print a clean reorder report
    print(f"While looking at this dates we can see that:\nWe have some articles below minimum stock:")
    [print(x) for x in belowStock]
    print(f"The total cost for reorder everything is: {totalCost}")
# The file has 4 fields separated by ": "
# Use split(": ") to parse each line
# Skip the first line (header)
