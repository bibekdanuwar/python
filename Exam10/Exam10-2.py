students_score = [
    ("田中", 85),
    ("佐藤", 78),
    ("鈴木", 92),
    ("山田", 67),
    ("高橋", 89)
]

good_students_score = []

for name, score in students_score:
    if score >= 80:
        good_students_score.append((name, score))

print("80点以上の学生だけの名前と得点を入れた新しいタプルのリスト:", good_students_score)