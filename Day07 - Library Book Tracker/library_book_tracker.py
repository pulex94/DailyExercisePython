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
            "returned" : persona["returned"],
            "totalPages" : 0
        }
        if name not in members:
            members[name] = [book_info]
        else:
            members[name].append(book_info)
    bestName = ""
    bestCount = 0
    genres = {}
    for name, books in members.items():
        counter = 0
        for book in books:
            if book["returned"] == "yes":
                counter += book["pages"]
            if counter > bestCount:
                bestCount = counter
                bestName = name
        print(f"{name} read a total of {counter} pages")
    print(f"Most pages in total by: {bestName} with {bestCount} pages!")
    for element in dates:
        if element["genre"] not in genres:
            genres[element["genre"]] = 1
        else:
            genres[element["genre"]] += 1
    genresOrdinato = sorted(genres.items(), key=lambda x: x[1], reverse=True)
    for element in genresOrdinato:
        print(f"{element[0]} - {element[1]}")

    noReturned = []
    for element in dates:
        if element["returned"] == "no":
            noReturned.append(element)
    print(f"Books on loan: {len(noReturned)}")

    with open("overdue_members.txt", "w") as file:
        overdueMembers = []
        for elements in dates:
            if elements["returned"] == "no":
                if elements["member_name"] not in overdueMembers:
                    overdueMembers.append(elements["member_name"])
        for name in overdueMembers:
            file.write(f"{name}\n")
    
    with open("top_readers.txt", "w") as file:
        topReaders = {}
        for name, books in members.items():
                counter = 0
                for book in books:
                        counter += book["pages"]
                topReaders[name] = counter
        Ordened = sorted(topReaders.items(), key=lambda x: x[1], reverse=True)
        for element in Ordened:
            file.write(f"{element[0]}: {element[1]}\n")

