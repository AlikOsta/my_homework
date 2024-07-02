

# Задание 1
numbers = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
num = ([int(i) for i in numbers.split()]) #"минимальный и максимальный элементы"
num_pos_neg = ([i for i in num if i < 0])

print(" ".join([str(min(num)), str(max(num))]), "минимальный и максимальный элементы")
print(len(([i for i in num if i < 0])), "количество отрицательных элементов")
print(len(([i for i in num if i > 0])), "количество положительных элементов")
print(len(([i for i in num if i == 0])), "количество нулей")

# Задание 2
def uno(n):
    return sorted(list(set(n)))

print("Начальный список: [10, 20, 10, 20, 30, 40, 30, 50]")
print("После удаления дублей:", uno([10, 20, 10, 20, 30, 40, 30, 50]))