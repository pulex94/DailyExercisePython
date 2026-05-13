import csv

with open("bookings.csv", "r") as f:
    reader = csv.DictReader(f)
    table = []

    for lines in reader:
        table.append(lines)
    print(table)
    hotels = {}
    for element in table:  # {nome_hotel : [{hotel1}, {hotel2}]}
        name = element["hotel"]
        prenotations = {
            "guest": element["guest"],
            "nights": element["nights"],
            "price_per_night": element["price_per_night"],
            "paid": element["paid"],
        }
        if name not in hotels:
            hotels[name] = [prenotations]
        else:
            hotels[name].append(prenotations)

    guests = {}
    for key, value in hotels.items():
        for prenotation in value:
            if prenotation["guest"] not in guests:
                guests[prenotation["guest"]] = int(prenotation["nights"])
            else:
                guests[prenotation["guest"]] += int(prenotation["nights"])

    sorted_guest = sorted(guests.items(), key=lambda x: x[1], reverse=True)
    best_guest_name, best_guest_nights = sorted_guest[0]
    print(f"{best_guest_name} - {best_guest_nights}")

    unpaid_bookkings = []
    for key, value in hotels.items():
        for prenotation in value:
            if prenotation["paid"] == "no":
                unpaid_bookkings.append({key: prenotation})
    for prenotation in unpaid_bookkings:
        for hotel_name, info in prenotation.items():
            print(
                f"To pay in {hotel_name} from {info["guest"]} a price per night of {info["price_per_night"]} for a total of {info["nights"]} nights"
            )

    with open("unpadid_bookings.txt", "w") as file:
        for prenotation in unpaid_bookkings:
            for hotel_name, info in prenotation.items():
                total = int(info["nights"]) * int(info["price_per_night"])
                file.write(f"{info["guest"]} - {hotel_name} - Total:{total}€\n")

    with open("top_hotels.txt", "w") as file:
        top_hotels = {}
        for key, value in hotels.items():
            counter = 0
            for prenotation in value:
                total = int(prenotation["price_per_night"] * int(prenotation["nights"]))
                counter += total
            top_hotels[key] = counter
        ordened = sorted(top_hotels.items(), key=lambda x: x[1], reverse=True)
        for element in ordened:
            file.write(f"{element[0]}: {element[1]}€\n")
