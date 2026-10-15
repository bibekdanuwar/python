import csv


with open("students.csv", "a", newline="", encoding="utf8") as file:
    students = csv.writer(file)
    students.writerow([4,"富士通四郎", 27, "Fujitsu","python応用"])