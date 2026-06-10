'''Дано целое число N (> 1). Вывести наибольшее из целых чисел K
#для которых сумма 1 + 2 + ... + K будет меньше или равна N, и саму эту сумму'''

def invert_digits(k: int) -> int:
    if not isinstance(k, int):
        raise ValueError("Параметр k должен быть целым числом")
        if k <= 0:
            raise ValueError("Параметр k должен быть положительным числом (k > 0)")

            reversed_str = str(k)[::-1]
            reversed_number = int(reversed_str)

    return reversed_number

def process_numbers(numbers: list[int]) -> list[int]:

    result = []
    for num in numbers:
        reversed_num = invert_digits(num)
        result.append(reversed_num)

    return result

if __name__ == "__main__":
    try:
        original_numbers = [123, 4567, 89, 1000, 7]

        print("Исходные числа:")
        for i, num in enumerate(original_numbers, 1):
            print(f"{i}. {num}")

        inverted_numbers = process_numbers(original_numbers)

        print("\nЧисла с обратным порядком цифр:")
        for i, num in enumerate(inverted_numbers, 1):
            print(f"{i}. {num}")

    except ValueError as e:
        print(f"Ошибка: {e}")