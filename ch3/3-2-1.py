name = "FOM出版"
establish = 1981

print(name)
print(establish)
print(str(establish) + "年")

value = "3000" # strの3000
print(value + "円") #3000円と表示される
# strをintに型変換
print(int(value) + 300) # 3300と表示させたい
print(str(int(value) + 300) + "円") # 3300円と表示させたい


# わかりやすくする
value_str = "3000"
value_tax_total = int(value_str) + 300
value_tax_total_str = str(value_tax_total) + "円"
print(value_tax_total_str)

# キーボード入力
num = input("キーボード入力してEnter:")
print(num)