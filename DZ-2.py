# Задание 1
# Пользователь вводит с клавиатуры два числа.
# Нужно посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.

start, stop = int(input("Enter a number: ")), int(input("Enter a number: "))

if start > stop:
    start, stop = stop, start

sum_chet = 0    #сумма четных чисел
sum_nechet = 0   #сумма нечетных чисел
krat_9 = 0       #сумма кратных 9

x = 0
y = 0
z = 0

for i in range(start, stop + 1):
    if i % 2 == 0:
        x += 1
        sum_chet = sum_chet + i
    elif i % 2 != 0:
        y += 1
        sum_nechet = sum_nechet + i

for i in range(start, stop + 1):
    if i % 9 == 0:
        z += 1
        krat_9 = krat_9 + i

if z > 0:
    print("Сумма всех чисел, кратных 9 =", krat_9)
    print("Среднеарифметическое чисел, кратных 9 =", krat_9 / z)
else:
    print("Чисел, кратных 9, нет")

if x > 0:
    print("Сумма всех четных чисел в диапазоне от", start, "до", stop, "=", sum_chet)
    print("Среднеарифметическое четных чисел =", sum_chet / x)
else:
    print("Четных чисел нет")

if y > 0:
    print("Сумма всех нечетных чисел в диапазоне от", start, "до", stop, "=", sum_nechet)
    print("Среднеарифметическое нечетных чисел =", sum_nechet / y)
else:
    print("Нечетных чисел нет")

# # Задание 2
# # Пользователь вводит любое целое число.
# # Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.
# # Будет плюсом если вы используете управляющие операторы continue, break и else.
#
# # chislo_2 = int(input('Chislo: '))
# chislo_2 = 169353465693
# rezerv = ["3", "6"]
#
# str_chislo_2 = str(chislo_2)
# result = list(str_chislo_2)
#
# new_chislo_2 = ""
#
# for i in result:
#     if i in rezerv:
#         result.remove(i)
#         new_chislo_2 = int(''.join(result))
#
# print(new_chislo_2)
#
#








