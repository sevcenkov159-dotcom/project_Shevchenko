""" Даны строки S и S0. Удалить из строки S все подстроки, совпадающие с S 0. Если
совпадающих подстрок нет, то вывести строку S без изменений.
"""
import random
def check_alternating_signs(numbers: list[int]) -> int:

    if not numbers:
        raise ValueError("Список не должен быть пустым")

    for num in numbers:
        if num == 0:
            raise ValueError("Все числа в списке должны быть ненулевыми")

    if len(numbers) == 1:
        return 0

    for i in range(1, len(numbers)):
        current_sign = numbers[i] > 0
        previous_sign = numbers[i - 1] > 0

        if current_sign == previous_sign:
            return i + 1

    return 0



