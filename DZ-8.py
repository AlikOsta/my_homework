
num_tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15)
num_tuple_2 = (12, 23, 3, 4, 15, 10, 61, 71, 82, 93)
num_tuple_3 = (15, 16, 17, 18, 23, 24, 2, 5, 10, 4,)
# 1 - Пересечение
print(tuple(set(num_tuple_1) & set(num_tuple_2) & set(num_tuple_3)))
# 2 - Разность
print(tuple(set(num_tuple_1) - set(num_tuple_2) - set(num_tuple_3)))
print(tuple(set(num_tuple_2) - set(num_tuple_1) - set(num_tuple_3)))
print(tuple(set(num_tuple_3) - set(num_tuple_1) - set(num_tuple_2)))

#3
def print_info(name, **kwargs):
    print(f"Имя: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

print_info("Иван", возраст=30, профессия="инженер", город="Москва")

#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mapped_result = list(map(lambda x: x ** 2 if x % 2 != 0 else x ** 3, numbers))

print(mapped_result)