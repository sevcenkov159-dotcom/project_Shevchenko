"""1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Элементы первого файла, отсутствующие во втором:
Элементы второго файла, отсутствующие в первом:
Количество элементов:
Индекс первого минимального элемента:
Индекс последнего максимального элемента:"""

data_1 = ['15 -7 42 -3 8 42 -1 0 5']
with open('data_1.txt', 'w', encoding='utf-8') as f1:
    f1.writelines(data_1)

data_2 = ['8 -3 42 10 -7 5 20']
with open('data_2.txt', 'w', encoding='utf-8') as f2:
    f2.writelines(data_2)

try:
    with open('data_1.txt', 'r', encoding='utf-8') as f1:
        content1 = f1.read().split()
        list1 = [int(x) for x in content1]
except FileNotFoundError:
    print("Файл data_1.txt не найден")
    list1 = []
except ValueError:
    print("Ошибка преобразования данных в файле data_1.txt")
    list1 = []

try:
    with open('data_2.txt', 'r', encoding='utf-8') as f2:
        content2 = f2.read().split()
        list2 = [int(x) for x in content2]
except FileNotFoundError:
    print("Файл data_2.txt не найден")
    list2 = []
except ValueError:
    print("Ошибка преобразования данных в файле data_2.txt")
    list2 = []

unique_in_1 = []
for x in list1:
    if x not in list2 and x not in unique_in_1:
        unique_in_1.append(x)

unique_in_2 = []
for x in list2:
    if x not in list1 and x not in unique_in_2:
        unique_in_2.append(x)

total_elements = len(list1) + len(list2)

combined = list1 + list2
if combined:
    min_value = min(combined)
    first_min_index = combined.index(min_value)
else:
    first_min_index = -1

if combined:
    max_value = max(combined)
    # Ищем справа
    last_max_index = len(combined) - 1 - combined[::-1].index(max_value)
else:
    last_max_index = -1

with open('result.txt', 'w', encoding='utf-8') as res:
    res.write('Элементы первого и второго файлов:\n')
    res.write(f'Первый файл: {list1}\n')
    res.write(f'Второй файл: {list2}\n\n')

    res.write('Элементы первого файла, отсутствующие во втором:\n')
    res.write(f'{unique_in_1}\n\n')

    res.write('Элементы второго файла, отсутствующие в первом:\n')
    res.write(f'{unique_in_2}\n\n')

    res.write('Количество элементов:\n')
    res.write(f'{total_elements}\n\n')

    res.write('Индекс первого минимального элемента:\n')
    res.write(f'{first_min_index}\n\n')

    res.write('Индекс последнего максимального элемента:\n')
    res.write(f'{last_max_index}\n')

print("Обработка завершена. Результат сохранён в файл result.txt")