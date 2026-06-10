import os
    os = r'D:/Этот компьютер/Локальный диск (D:)/Архив/Dostoevsky.txt'
import re
from typing import Set, List


def read_file_content(file_path: str) -> str:

    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_dostoevsky_variants(text: str) -> Set[str]:
    pattern = re.compile(
        r'\bДостоевск(?:ий|ого|ому|им|ом|ая|ой|ие|их)\b',
        re.UNICODE
    )

    # Поиск всех совпадений
    matches = pattern.findall(text)

    # Возвращаем множество для уникальности
    return set(matches)


def sort_variants(variants: Set[str]) -> List[str]:
    return sorted(variants)


def main(file_path: str) -> List[str]:
    content = read_file_content(file_path)

    # Поиск вариантов фамилии
    variants = find_dostoevsky_variants(content)

    # Сортировка результатов
    sorted_variants = sort_variants(variants)

    return sorted_variants


if __name__ == "__main__":
    # Запуск программы
    file_path = "Dostoevsky.txt"

    try:
        results = main(file_path)

        print("Найденные варианты фамилии Достоевского:")
        print("-" * 40)
        for variant in results:
            print(f"  • {variant}")

        print("-" * 40)
        print(f"Всего уникальных вариантов: {len(results)}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")