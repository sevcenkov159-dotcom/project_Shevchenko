"""2.Составить генератор (yield), который выводит из строки только буквы."""
def letter_generator(input_string: str):
    for char in input_string:
        if char.isalpha():
            yield char

def main_task_2():
    source_string = "Hello< world! Привет мир! 2026. #Python"
    print("Исходная строка: {source_stiring}")

    gen = letter_generator(source_string)

    result_string = "" .join(gen)
    print(f"Результат (только буквы): {result_string}")

    gen = letter_generator(source_string)
    result_string = "" .join(gen)
    print(f"Результат (только буквы): {result_string}")

if __name__ == "__main__":
    main_task_2()
