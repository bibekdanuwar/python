user_dict_list = [
    {"name": "yamada taro", "age": "10", "height": "140", "weight": "40", "email": "taro@example.com"},
    {"name": "suzuki keiko", "age": "15", "height": "150", "weight": "50", "email": "keiko@example.com"},
    {"name": "sato hanako", "age": "20", "height": "160", "weight": "60", "email": "hanako@example.com"},
    {"name": "yoshida yoshio", "age": "25", "height": "170", "weight": "70", "email": "yoshio@example.com"}
]

bmi_score_list = []

for user in user_dict_list:
    height = int(user["height"])
    weight = int(user["weight"])

    bmi = weight / ((height / 100) ** 2)

    bmi_score_list.append((user["name"], round(bmi, 2)))

print(bmi_score_list)

for user in user_dict_list:
    height = int(user["height"])
    weight = int(user["weight"])

    bmi = weight / ((height / 100) ** 2)

    if bmi < 16:
        result = "痩せすぎ"
    elif bmi < 17:
        result = "痩せ"
    elif bmi < 18.5:
        result = "痩せぎみ"
    elif bmi < 25:
        result = "普通体重"
    elif bmi < 30:
        result = "前肥満"
    elif bmi < 35:
        result = "肥満(1度)"
    elif bmi < 40:
        result = "肥満(2度)"
    else:
        result = "肥満(3度)"

    print(user["name"], round(bmi, 2), result)