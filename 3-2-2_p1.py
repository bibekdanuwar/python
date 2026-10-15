current_year = 2026

name = "ビベク"
age = 21

birthday = input("今年の誕生日は過ぎましたか？(y/n)：")

if birthday == "y":
    birth_year = current_year - age
else:
    birth_year = current_year - age - 1

print(name, "さんは", birth_year, "年生まれです。")