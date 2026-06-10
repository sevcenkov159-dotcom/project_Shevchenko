"""Задание2.
В матрице элементы первого столбца возвести в куб."""
def cube_first_column(matrix: list[list[float]]) -> list[list[float]]:
    return [
        [row[0] ** 3] + row[1:] if row else row
        for row in matrix
    ]


def display_matrix(matrix: list[list[float]]) -> None:
    for row in matrix:
        print(' '.join(f'{elem:10.2f}' for elem in row))
    print()


def main() -> None:
    matrix = [
        [1.0, -2.0,  3.0,  4.0],
        [2.0,  5.0, -1.0,  8.0],
        [3.0,  6.0,  4.0,  2.0],
        [4.0, -3.0,  0.0, -9.0]
    ]

    print("Исходная матрица:")
    display_matrix(matrix)

    transformed_matrix = cube_first_column(matrix)

    print("Матрица после возведения первого столбца в куб:")
    display_matrix(transformed_matrix)


if __name__ == '__main__':
    main()