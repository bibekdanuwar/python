age = ""
while True:
    age = input("年齢を入力してください=>")
    if age.isdigit():
        if int(age) >= 0:
            break
    print("0以上の数値を入力してください")
print("入力を受け付けました : " + age)