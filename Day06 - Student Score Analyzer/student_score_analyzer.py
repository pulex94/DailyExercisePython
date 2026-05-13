
with open("students.txt", "r") as f:
    content = f.readlines()
    lines = [line.strip() for line in content]
    nameValue = [line.split(",") for line in lines]

    listaDizionari = [{"name": n, "score": v} for n, v in nameValue]
    totalScore = 0
    for student in listaDizionari:
        totalScore += int(student["score"])
    averageScore = totalScore / len(listaDizionari)
    print(f"Average score between students: {round(averageScore)}")

    bestStudentName = "" 
    bestStudentScore = 0
    for student in listaDizionari:
        if int(student["score"]) > int(bestStudentScore):
            bestStudentScore = student["score"]
            bestStudentName = student["name"]
    print(f"Best student is: {bestStudentName} with score of: {bestStudentScore} ")

with open("passed_students.txt", "w") as file:
    passedStudent = []
    for student in listaDizionari:
        if int(student["score"]) > 70:
            file.write(f"{student["name"]}:{student["score"]}\n")

with open("sorted_scores.txt", "w") as file:
    nameValue = sorted(nameValue, key=lambda x: x[1], reverse=True) 
    for element in nameValue:
        file.write(f"{element[0]}:{element[1]}\n")