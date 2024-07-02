def discount(age):
    match age:
        case age if age < 3:
            return 10
        case age if 3 <= age < 6:
            return 20
        case age if 6 <= age < 10:
            return 30
        case age if 10 <= age < 14:
            return 40
        case _:
            return 50

def total():
    ages = [12, 4, 7, 11, 18, 2]
    discounts = []

    for age in ages:
        discount_age = discount(age)
        discounts.append(discount_age)
        print(f"Возраст: {age}, Скидка: {discount_age}%")

total()

##############################################

def top_category(total_score):
    match total_score:
        case total_score if total_score < 25:
            return "Новичок"
        case total_score if 25 <= total_score < 50:
            return "Любитель"
        case total_score if 50 <= total_score < 75:
            return "Профессионал"
        case _:
            return "Мастер"

def play() :
    scores_list = [
        [5, 2, 8, 1, 4],
        [7, 12, 9, 8, 11],
        [15, 10, 15, 12, 18],
        [19, 18, 15, 16, 17]
    ]
    i = 0
    for scores in scores_list :
        i += 1
        total_score = sum(scores)
        category = top_category(total_score)
        print(f"Игрок {i}: Очки = {total_score}, Категория = {category}")

play()

##############################################################

import random
import string


def generate_password(length, complexity=3) :
    result = ""

    if length < 1:
        return 'Ошибка! Укажите длину пароля'
    if  1 < complexity > 3 :
        return"Ошибка! Укажите верный уровень сложности"

    if complexity == 1 :
        password = string.ascii_letters
    elif complexity == 2 :
        password = string.ascii_letters + string.digits
    elif complexity == 3 :
        password = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length) :
        result += random.choice(password)
    return result

print(generate_password(int(input("Укажите длину пароля: ")), int(input("Укажите сложность пароля от 1 до 3: "))))