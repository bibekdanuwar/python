import csv

with open("students.csv", "r", encoding="utf-8") as file:
    students = csv.reader(file)
    for student in students:
        print(student)