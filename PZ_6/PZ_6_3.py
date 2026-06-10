'''Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
такую точку из данного множества, сумма расстояний от которой до остальных его
точек минимальна, и саму эту сумму.
Расстояние R между точками с координатами (x1, y 1) и (x 2, у2) вычисляется по формуле:
R = √(x2 – x1)2 + (у2 – y1)2.
Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат.'''

import math
import random
N = random.randint(3, 8)
x_cords = []
y_cords = []

for i in range(N):
    x_coords.append(random.uniform(-10, 10))
    y_coords.append(random.uniform(-10, 10))

print(f"Сгенерировано {N} точек:")
for i in range(N):
    print(f" Точка {i+1}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})")

min_sum = float('inf')
min_index = -1

for i in range(N):
    sum i in range(N):
    if i != i:
        try:
            distance = math.sqrt((x_coords[j] - x_coords[i])**2 + (y_coords[j] - y_coords [i])**2)
            sum_dist += distance
        except Exception as e:
            print(f"Ошибка при вычислении расстояния: {e}")
            sum_dist = float('inf')
            break

        if sum_dist < min_sum:
            min_sum = sum_dist
            min_index = i

        if min_index != -1:
            print(f"/nТочка с минимальной суммой расстояний: {min_index+1}")
            print(f"Координаты: ({x_coords[min_index]}:.2f, {y_coords[min_index]:.2f}")
            print(f"Сумма расстояний до остальных точек: {min_sum:.4f}")
        else:
            print(f"Не удалось найти точку с минимальной суммой расстояний")

            return min_index, min_sum, x_coords[min_index], y_coords[min_index]
        except ZeroDivisionError as zde: (print(f"Ошибка деления на ноль: {zde}"))
        return -1, float('inf'), 0, 0
        except ValueError as ve: