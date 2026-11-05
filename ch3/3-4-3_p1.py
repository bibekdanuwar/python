score1 = int(input("テスト1の得点を入力="))
score2 = int(input("テスト2の得点を入力="))
score3 = int(input("テスト3の得点を入力="))

scores = [score1, score2, score3]
total = 0

for score in scores:
    total += score

print("合計点：" + str(total))