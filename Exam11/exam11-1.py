

def bmi_checker(user):


    height = int(user['height'])
    weight = int(user['weight'])

    bmi = weight / (height / 100) ** 2



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




    print("名前:", user["name"])
    print("BMI:", round(bmi, 2))
    print("判定:", result)

# bmi_checker(user_dict)



# spiderman = {
#     'name'   : "spiderman",
#    'age'    : "26",
#    'height' : "125",
#    'weight' : "100",
#    'email'  : "spiderman@example.com"
# }


# bmi_checker(spiderman)


manche = {}


name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")
email = input("Enter your email: ")

manche = {
    'name': name,
    'age': age,
    'height': height,
    'weight': weight,
    'email': email
}


bmi_checker(manche)