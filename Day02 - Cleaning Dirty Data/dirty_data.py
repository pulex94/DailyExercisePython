
# Read the CSV with DictReader
import csv
counter = 0
with open("client.csv") as file:
    reader = csv.DictReader(file)
    with open("file_cleaned.csv", "w", newline="") as file_cleaned:
        fields = ["name", "email", "phone"]
        writer = csv.DictWriter(file_cleaned, fieldnames=fields)
        writer.writeheader()
                
# Name: remove extra spaces, capitalize the first letter
        for person in reader:
          person["name"] = person["name"].title().strip().replace("  ", " ")
# Email: all lowercase
          person["email"] = person["email"].lower().strip()
# Phone: remove spaces and hyphens — numbers only
          person["phone"] = person["phone"].replace("-", "").replace(" ", "").strip()
# Save the cleaned data in a new file: file_cleaned.csv
          writer.writerow(person)
# Print how many records you cleaned
          counter += 1

print(f"Record puliti: {counter}")