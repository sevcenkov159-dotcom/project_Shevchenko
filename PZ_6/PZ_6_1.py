"""Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем
положительные и отрицательные числа. Если чередуются, то вывести 0, если нет, то
вывести порядковый номер первого элемента, нарушающего закономерность."""
import math
import random

N = random.randint(5, 10)

numbers = []

for i in range(N):
    num = random.randint(-10, 10)
    while num == 0:
        num = random.randint(-10, 10)
    numbers.append(num)

print(f"Список из {N} чисел: {numbers}")


result = 0
for i in range(1, N):
            if (numbers[i]) > 0 and numbers[i-1] > 0 or (numbers[i] < 0 and numbers[i-1] < 0):
                result = i + 1
                break

            else:

                print("Числа чередуются правильно")
print(f"Результат: {result}")

def main():
    return result
try:
    main()
except Exception as e:
    print(f"Ошибка: {e}")
    return -1
