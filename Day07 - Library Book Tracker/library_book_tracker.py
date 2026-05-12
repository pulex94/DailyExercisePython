import csv

with open("library.csv", "r") as file:
    table = csv.DictReader(file)
    dates = []
    for persona in table:
        dates.append(persona)

    members = {}
    for persona in dates:
        name = persona["member_name"]
        book_info = {
            "title" : persona["book_title"],
            "pages" : int(persona["pages"]),
            "returned" : persona["returned"]
        }
        if name not in members:
            members[name] = [book_info]
        else:
            members[name].append(book_info)
    print(members)
