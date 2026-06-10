"""
Задание 1.
В матрице найти среднее арифметическое положительных элементов."""

from itertools import chain


def mean_positive(matrix: list[list[float]]) -> float | None:
    """
    :param matrix: Двумерный список (матрица)
    :return: Среднее арифметическое или None, если положительных элементов нет
    """
    # Генератор, объединяющий все строки и фильтрующий положительные элементы
    positives = (element for element in chain.from_iterable(matrix) if element > 0)

    total = 0
    count = 0
    for value in positives:
        total += value
        count += 1

    return total / count if count != 0 else None


def display_matrix(matrix: list[list[float]]) -> None:
    """Вывод матрицы в консоль."""
    for row in matrix:
        print(' '.join(f'{elem:8.2f}' for elem in row))
    print()


def main() -> None:
    matrix = [
        [1.5, -2.3, 0.0, 4.1],
        [-3.0, 5.7, -1.2, 8.3],
        [0.0, 6.1, -4.5, 2.9],
        [-7.2, 3.4, 0.0, -9.0]
    ]

    print("Исходная матрица:")
    display_matrix(matrix)

    result = mean_positive(matrix)
    if result is not None:
        print(f"Среднее арифметическое положительных элементов: {result:.4f}")
    else:
        print("Положительные элементы отсутствуют.")


if __name__ == '__main__':
    main()