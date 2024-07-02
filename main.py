# Пользователь вводит с клавиатуры три числа. В за-
# висимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

a, b, c = int(input("Введите число: ")), int(input("Введите число: ")), input("Укажите '*' или '+': ")
if c == "*":
    print(a, "*", b, '=', (a * b))
elif c == "+":
    print(a, "+", b, '=', (a + b))

# Пользователь вводит с клавиатуры три числа. В за-
# висимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или сред-
# неарифметическое трёх чисел.
#
# chislo_1, chislo_2, chislo_3 = int(input("Введите число_1: ")), int(input("Введите число_2: ")),int(input("Введите число_3: "))
# res = input("Какое число вы хотите вывести на экран (макс, мин, сред): ")
#
# if res == "сред":
#     print("Среднеарифметическое трёх чисел = ", (chislo_1 + chislo_2 +chislo_3) / 3)
# elif res == "макс":
#     max = 0
#     if chislo_1 > chislo_2 and chislo_1 > chislo_3:
#         max = chislo_1
#     elif chislo_2 > chislo_3 and chislo_2 > chislo_1:
#         max = chislo_2
#     elif chislo_3 > chislo_1 and chislo_3 > chislo_2:
#         max = chislo_3
#     print("Максимум из трёх чисел- ",max)
# elif res == "мин":
#     min = 0
#     if chislo_1 < chislo_2 and chislo_1 < chislo_3:
#         min = chislo_1
#     elif chislo_2 < chislo_3 and chislo_2 < chislo_1:
#         min = chislo_2
#     elif chislo_3 < chislo_1 and chislo_3 < chislo_2:
#         min = chislo_3
#     print("Минимум из трёх чисел- ", min)

# Пользователь вводит с клавиатуры количество ме-
# тров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.
#
# metrov = int(input("Укажите количество метров: "))
# var = input("Укажите желаемую величину измерения (мили, дюймы или ярды): ")
#
# if var == "мили":
#     print(metrov * 0.00062)
# elif var == "дюймы":
#     print(metrov * 39.37)
# elif var == "ярды":
#     print(metrov * 1.0936)
