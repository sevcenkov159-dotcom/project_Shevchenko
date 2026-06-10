'''даны целые числа a, b, c. Проверить истинность высказывания: "Существует треугольник
#со сторонами a, b, c.'''
a = input("Введите сторону a: ")
while type(a) != int:
    try:
        a = int(a)
    except TypeError:
        print("Вы ввели неправильное значение")
        a = int(a)

b = input("Введите сторону b: ")
while type(b) != int:
    try:
        b = int(b)
    except TypeError:
        print("Вы ввели неправильное значене")
        b = int(b)

c = input("Введите сторону c: ")
while type(c) != int:
    try:
        c = int(c)
    except TypeError:
        print("Вы ввели неправильное значение")
        c = int(c)

triangle_exists = (a + b > c) and (a + c > b) and (b + c > a)
print(triangle_exists)