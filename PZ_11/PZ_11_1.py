"""1.В последовательности их N чисел (N –четное) во второй ее половине найти сумму
элементов больших 10."""
import random

def generate_sequence(n: int, min_val: int = 0, max_val: int = 20) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(n)]


def sum_second_half_greater_than_10(sequence: list[int]) -> int:
    mid_index = len(sequence) // 2
    second_half = sequence[mid_index:]

    return sum(element for element in second_half if element > 10)


def main_task_1():
    n = 10
    source_sequence = generate_sequence(n)
    print(f"Исходная последовательность: (N={n}): {source_sequence}")
    print(f"Первая половина: {source_sequence[:n // 2]}")
    print(f"Вторая половина:  {source_sequence[n // 2:]}")

    result_sum = sum_second_half_greater_than_10(source_sequence)
    print(f"Сумма элементов больше 10 во второй половине:  {result_sum}\n")


if __name__ == "__main__":
    main_task_1()