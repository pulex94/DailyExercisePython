# 1. Read the CSV file
import csv
dati = []
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        dati.append(line)
# 2. Calculate the average grade for each student
    print("AVERAGE GRADES:")
    for person in dati:
        name = person["student"]
        math = int(person["math"])
        science = int(person["science"])
        english = int(person["english"])
        history = int(person["history"])
        averageDates = (math + science + english + history) / 4
        person["averageDates"] = averageDates
        print(f" {name}- {averageDates}")
    # 3. Assign a grade label:
    #    - average >= 90: "Excellent"
        if averageDates >= 90:
            person["label"] = "Excellent"
    #    - average >= 70: "Good"
        elif averageDates >= 70:
            person["label"] = "Good"
    #    - average >= 50: "Sufficient"
        elif averageDates >= 50:
            person["label"] = "Sufficient"
    #    - average < 50: "Insufficient — needs support"
        else:
            person["label"] = "Insufficient — needs support"
    # 4. Find the top student (highest average)
    print("TOP STUDENT GRADES:")
    topStudentGrades = 0
    topStudentName = ""
    for element in dati:
        if element["averageDates"] > topStudentGrades:
            topStudentGrades = element["averageDates"]
            topStudentName = element["student"]
    print(f" {topStudentName} - {topStudentGrades}")
# 5. Find the students who need support (average < 50)
    print("WORST STUDENTS GRADES:")
    for element in dati:
        if element["label"] == "Insufficient — needs support":
            print(f" {element["student"]} - {element["label"]}")
# 6. Print a clean summaryx report
    print(f"SUMMARY REPORT:\n TOP STUDENT:\n  {topStudentName} with {topStudentGrades}")
    print(f" WORST STUDENTS:")
    for element in dati:
        if element["label"] == "Insufficient — needs support":
            print(f"  {element["student"]} - {element["label"]}")
