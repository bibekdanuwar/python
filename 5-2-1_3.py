with open("member.txt", "r", encoding="utf8") as file:
    for name in file:
        print(name,end="")
