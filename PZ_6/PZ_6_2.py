"""Дан целочисленный список A размера N (< 15). Переписать в новый целочисленный
список B все элементы с нечетными порядковыми номерами (1,3,...) и вывести
размер полученного списка B и его содержимое. Условный оператор не
использовать."""

import random
N = random.randint(1, 14)

A = []

for i in range(N):
    A.append(random.randint(-10, 10))

print(f"исходный список A Размера {N}: {A}")

B = A[0::2]
print(f"Размер полученого списка B: {len(B)}")
print(f"Содержимое списка B: {B}")

def result_len(B):
    return_len(B), B

    try:
        return_len(B), B
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
        return 0, []
    except IndexError as ie:
        print(f"Ошибка индекса: {ie}")
    return 0, []
    except Exception as e:
        print(f"Ошибка: {e}")
    return [], []