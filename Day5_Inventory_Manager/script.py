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
    for element in inventory:
        if int(element["quantity"]) > int(element["min_stock"]):
            print(f"{element["product"]}")
# 4. Calculate how many units need to be ordered (min_stock - quantity)

# 4. Calculate how many units need to be ordered (min_stock - quantity)
# 5. Calculate the reorder cost for each product (units_to_order * price)
# 6. Calculate the total reorder cost
# 7. Print a clean reorder report
# The file has 4 fields separated by ": "
# Use split(": ") to parse each line
# Skip the first line (header)
