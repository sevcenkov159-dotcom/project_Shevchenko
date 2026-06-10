'''Составить программу, в которой функцию построит изображение, в котором в первой строке 1 звездочка
во второй - 2, в третьей - 3, ..., в строке с номером m - m звездочек'''

def print_asterisk_pattern(m: int) -> None:
    if not isinstance(m, int):
        raise ValueError("Параметр m должен быть целым числом")
        if m <= 0:
            raise ValueError("Параметр m должен быть положительным числом (m > 0)")

    for i in range(1, m + 1): print("*" * i)

if __name__ == "__main__":
    try:
        print("\nУзор из 5 строк:")
        print_asterisk_pattern(5)

        print("\nУзор из 3 строк:")
        print_asterisk_pattern(3)

        print("\nПопытка вывести узор с m = -1:")
        print_asterisk_pattern(-1)

    except ValueError as e:
        print(f"Ошибка: {e} ")