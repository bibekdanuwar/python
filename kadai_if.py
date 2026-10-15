score = int(input("テストの点数を入力してください: "))

if score < 0 or score > 100:
    print("不正な値入力")
elif score < 60:
    print("不可")
elif score < 70:
    print("可")
elif score < 80:
    print("良")
elif score < 90:
    print("優")
else:
    print("秀")