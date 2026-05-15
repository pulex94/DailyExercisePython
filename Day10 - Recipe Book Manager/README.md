Objective:
Practice reading data from external TXT files, building and navigating nested dictionaries and lists, aggregating data across multiple keys, and writing filtered results to output TXT files.

Instructions:

Create a file called recipes.txt by copying the data below.
Read the TXT file and parse each recipe into a dictionary with: name, category, ingredients (as a list), calories, time_minutes.
Store all recipes in a list called recipes.
Build a dictionary called categories where each key is a category name and the value is a list of recipe names in that category.
Display the category with the most recipes. 
Find and display the recipe with the lowest calories.
Find and display the recipe with the shortest preparation time.
Filter all recipes with calories greater than 500 and store them in a list called high_calorie.
Save a file called high_calorie_recipes.txt containing one line per recipe formatted as: Name - Calories: X - Time: Y min.
Save a file called category_report.txt with categories sorted by number of recipes (highest first), formatted as: Category: X recipes → recipe1, recipe2, ....