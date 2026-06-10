import os
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

    matches = pattern.findall(text)

    return set(matches)


def sort_variants(variants: Set[str]) -> List[str]:
    return sorted(variants)


def main(file_path: str) -> List[str]:
    content = read_file_content(file_path)

    variants = find_dostoevsky_variants(content)

    sorted_variants = sort_variants(variants)

    return sorted_variants


if __name__ == "__main__":
    os = r'D:/Этот компьютер/Локальный диск (D:)/Архив/Dostoevsky.txt'

    try:
        results = main(os)

        print("Найденные варианты фамилии Достоевского:")
        for variant in results:
            print(f"  • {variant}")

        print(f"Всего уникальных вариантов: {len(results)}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{os}' не найден.")
        print("Проверьте правильность пути к файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")