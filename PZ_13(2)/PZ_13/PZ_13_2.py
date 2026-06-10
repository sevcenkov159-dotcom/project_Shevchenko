import string

def task_2():
    input_filename = "text18-26.txt"
    output_filename = "text18-26_processed.txt"

    with open(input_filename, "w", encoding="utf-8") as f:
        f.write(sample_text)

    # Набор знаков препинания (добавляем тире '—', так как стандартный string.punctuation его не содержит)
    punctuation_marks = set(string.punctuation + "—")

    punctuation_count = 0
    processed_lines = []

    try:
        print("Содержимое исходного файла:")
        print("-" * 30)

        with open(input_filename, "r", encoding="utf-8") as f_in:
            for line in f_in:
                print(line, end="")

                for char in line:
                    if char in punctuation_marks:
                        punctuation_count += 1

                new_line = "".join(
                    ["/" if char in punctuation_marks else char for char in line]
                )
                processed_lines.append(new_line)

        print("\n" + "-" * 30)
        print(f"Количество знаков препинания в файле: {punctuation_count}\n")

        # 3. Записываем обработанный текст в новый файл
        with open(output_filename, "w", encoding="utf-8") as f_out:
            f_out.writelines(processed_lines)

        # Выводим измененный текст на экран для проверки
        print("Содержимое нового измененного файла:")
        print("-" * 30)
        with open(output_filename, "r", encoding="utf-8") as f_check:
            print(f_check.read())

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_filename} не найден.")


if __name__ == "__main__":
    task_2()