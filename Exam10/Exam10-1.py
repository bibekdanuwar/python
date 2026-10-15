students_score = [
    ("田中", 85),
    ("佐藤", 78),
    ("鈴木", 92),
    ("山田", 67),
    ("高橋", 89)
]

score_list = []

for student in students_score:
    score = student[1]
    score_list.append(score)

total = 0
for score in score_list:
    total = total + score

average = total / len(score_list)

print("各学生の得点だけを抽出したリスト:", score_list)
print("平均点:", average)