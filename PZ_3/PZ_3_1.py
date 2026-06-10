'''Даны числа X,y. Проверить истинность высказывания: "Точка с координатами (x,y)"
#лежит в четвертой координатной четверти.'''

x = input("Введите первую координату x: ")
while type(x) != float:
    try:
        x = float(x)
    except TypeError:
        print("Вы ввели неправильное значение")
        x = input("Введите первую координату x: ")

y = input("Введите вторую координату y: ")
while type(y) != float:
    try:
        y = float(y)
    except TypeError:
        print("Вы ввели неправильное значение")
        y = input("Введите вторую координату y:")

in_fourth_quarter = (x > 0) and (y < 0)
print(in_fourth_quarter)