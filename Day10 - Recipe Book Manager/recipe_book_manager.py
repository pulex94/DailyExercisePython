with open("recipes.txt", "r") as f:
    content = f.read()
    ricetta = content.split("---")
    recipes = []
    for element in ricetta:
        template = {}
        lines = element.split("\n")
        for element in lines:
            if element == "":
                continue
            key, value = element.split(":")
            value = value.strip()
            if key.strip() == "ingredients":
                value = value.split(", ")
            template[key] = value
        if template:
            recipes.append(template)

    categories = {}
    for recipe in recipes:
        if recipe["category"] not in categories:
            categories[recipe["category"]] = [recipe["name"]]
        else:
            categories[recipe["category"]].append(recipe["name"])

    most_recipe_category_name = ""
    most_recipe_category_quant = 0
    for category, recipe_list in categories.items():
        if len(recipe_list) > most_recipe_category_quant:
            most_recipe_category_name = category
            most_recipe_category_quant = len(recipe_list)
    print(f"{most_recipe_category_name}:{most_recipe_category_quant}")

    less_recipe_category_name = ""
    less_recipe_category_quant = 9999
    less_time_recipe_name = ""
    less_time_recipe_time = 9999
    high_calorie = []
    for recipe in recipes:
        if int(recipe["calories"]) < less_recipe_category_quant:
            less_recipe_category_name = recipe["name"]
            less_recipe_category_quant = int(recipe["calories"])
        if int(recipe["time_minutes"]) < less_time_recipe_time:
            less_time_recipe_name = recipe["name"]
            less_time_recipe_time = int(recipe["time_minutes"])
        if int(recipe["calories"]) >= 500:
            high_calorie.append(recipe)
    print(f"{less_recipe_category_name}: {less_recipe_category_quant}")
    print(f"{less_time_recipe_name}: {less_time_recipe_time}")

with open("high_calorie_recipes.txt", "w") as f:
    for recipe in high_calorie:
        f.write(
            f"{recipe["name"]} - Calories: {recipe["calories"]} - Time: {recipe["time_minutes"]} min\n"
        )

with open("category_report.txt", "w") as f:
    categories = sorted(categories.items(), key=lambda x: len(x[1]), reverse=True)
    for category, recipe_list in categories:
        f.write(f"Category: {category} Recipes -> {', '.join(recipe_list)}\n")
