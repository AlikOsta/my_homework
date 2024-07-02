# import matplotlib.pyplot as plt

# 1. Чтение данных:
def read_file(file_path) :
    with open(file_path, 'r', encoding='utf-8') as file :
        return file.readlines()

file_path = 'post.txt'
# print(f"{read_file(file_path)=}")

# 2. Обработка данных:
def process_data(data):
    sales_data = {}
    for line in data :
        period, sales = line.strip().split(':')
        sales_data[period] = int(sales)
    return sales_data

data_2 = eval(read_file(file_path)[0].split(' = ')[1])
# print(f"{process_data(data_2)=}")

#3. Фильтрация данных:
def filter_data(data, threshold) :
    return {date : profit for date, profit in data.items() if profit > threshold}

data_3 = process_data(data_2)
# print(f"{filter_data(data_3, 100000)=}")

# 4. Агрегация данных:
def aggregate_data(data) :
    total_sales = sum(data.values())
    return total_sales

data_4 = filter_data(data_3, 100000)
# print(f"{aggregate_data(data_4)=}")

# 5. Визуализация результатов:
# если можно, повторите еще раз как решить эту задачу.

# def visualize_data(data):
#     months = list(data.keys())
#     values = list(data.values())
#
#     plt.figure(figsize=(10, 6))  # Размер графика
#     plt.bar(months, values, color='skyblue')
#
#     plt.title('Продажи по месяцам')
#     plt.xlabel('Месяц')
#     plt.ylabel('Продажи')
#
#     for i, value in enumerate(values):
#         plt.text(i, value + max(values)*0.02, str(value), ha='center', va='bottom', fontsize=10)
#
#     plt.tight_layout()
#     plt.xticks(rotation=45)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.show()
#
# visualize_data(data_2)

# 6. Общий процесс:
# не до конца понял задачу, нужна функция которая ссылается на остальные функции и выводит данные всех задач?
# или нужна одна большая функция
def all_processed():
    read_file_answer = eval(read_file(file_path)[0].split(' = ')[1])
    process_data_answer = process_data(read_file_answer)
    filter_data_answer = filter_data(process_data_answer, 100000)
    aggregate_data_answer = aggregate_data(filter_data_answer)
    return (f"{read_file_answer=}\n{process_data_answer=}\n{filter_data_answer=}\n{aggregate_data_answer=}")

print(all_processed())
