Scenario:
The manager sends you a CSV file with customer data. The problem is that the data is dirty. Names have extra spaces, emails with mixed capitalization, phone numbers with hyphens and spaces.
The program must:

Read the CSV with DictReader
Name: remove extra spaces, capitalize the first letter
Email: all lowercase
Phone: remove spaces and hyphens — numbers only

Save the cleaned data in a new file: clienti_puliti.csv
Print how many records you cleaned