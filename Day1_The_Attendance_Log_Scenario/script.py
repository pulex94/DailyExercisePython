# open file
# -Read the file
with open("registro.txt", "r") as file:

# -Create a dictionary {name: hours}   
    lines = file.readlines()
    dates = {}
    for line in lines:
        line = line.strip()
        name, hours = line.split(":")
        hours = int(hours)
        dates[name] = hours

# -Print all employees with their hours
    print("**Print all employees with their hours**")
    for name, hours in dates.items():
        print(f"{name} - {hours}")

# -Find who worked the most hours
    print("**Who worked the most hours**")
    workerTopName = ""      
    workerTopHours = 0
    for name, hours in dates.items():
        if hours > workerTopHours:
            workerTopName = name
            workerTopHours = hours
    print(f"{workerTopName} - {workerTopHours}")
# -Find who worked the fewest hours
    print("**Who worked the fewest hours**")
    workerLessName = ""
    workerLessHours = 999
    for name, hours in dates.items():
        if hours < workerLessHours:
            workerLessName = name
            workerLessHours = hours
    print(f"{workerLessName} - {workerLessHours}")
#-Calculate the average hours for the entire company
    print("Calculate the average hours for the entire company")
    totalHours = 0
    peoples = len(lines)
    for hours in dates.values():
        totalHours += hours
    average = totalHours / peoples
    print(round(average, 2))
#-Print who worked overtime — more than 40 hours
    print("Who worked overtime — more than 40 hours")
    for names, hours in dates.items():
        if hours > 40:
            print(f"{names} - {hours}")