"""2. Из предложенного текстового файла (text18-26.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно заменив все знаки пунктуации на знак «/»"""
t = 0
d = 0

try:
    f_in = open('text18-26.txt', 'r', encoding='UTF-8')
    for line in f_in:
        print(line, end='')
        t += 1
        for char in line:
            if char == 'ж':
                d += 1
    f_in.close()
except FileNotFoundError:
    print("Файл text18-26.txt не найден")
    t, d = 0, 0

print(end='\n')
print('Количество строк: ', t, end='\n')
print('Количество букв "ж": ', d, end='\n')

try:
    f1 = open('text18-26.txt', 'r', encoding='UTF-8')
    lines = f1.readlines()
    f1.close()

    if len(lines) >= 4:
        lines[0], lines[3] = lines[3], lines[0]
    else:
        print("В файле менее 4 строк, перестановка невозможна")

    f2 = open('text18-2.txt', 'w', encoding='UTF-8')
    f2.writelines(lines)
    f2.close()
    print("Новый файл text18-26.txt успешно создан")
except FileNotFoundError:
    print("Не удалось открыть файл text18-26.txt для перестановки строк")