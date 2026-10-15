one_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# one_listオブジェクトを使う場合
even_list2 = []
odd_list2 = []
for value in one_list:
    if value % 2 == 0:
        even_list2.append(value)
    else:
        odd_list2.append(value)
print("one_listを使った偶数リスト:", even_list2)
print("one_listを使った奇数リスト:", odd_list2)