students_scores = [
    ("田中", [85, 78, 90]),
    ("佐藤", [78, 82, 88]),
    ("鈴木", [92, 90, 85]),
    ("山田", [67, 72, 80]),
    ("高橋", [89, 88, 91])
]

students_avg_score = []

for name, scores in students_scores:
    total = 0
    for score in scores:
        total = total + score
    average = total // len(scores)
    students_avg_score.append((name, average))

print("各生徒の名前と平均点が格納されたタプルのリスト:", students_avg_score)