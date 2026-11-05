one_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# range()クラスを使う場合
total = 0
for i in range(len(one_list)):
    total = total + one_list[i]
print("range()を使った合計:", total)

# one_listオブジェクトを使う場合
total2 = 0
for value in one_list:
    total2 = total2 + value
print("one_listを使った合計:", total2)