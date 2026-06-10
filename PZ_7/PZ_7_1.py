"""Даны целые положительные числа N1 и N2 и строки S1 и S2. Получить из этих строк
новую строку, содержащую первые N1 символов строки S1 и последние N2
символов строки S2 (в указанном порядке)."""

def remove_substring(s: str, s0: str) -> str:

    if not isinstance(s, str):
        raise ValueError("Аргумент s должен быть строкой")
    if not isinstance(s0, str):
        raise ValueError("Аргумент s0 должен быть строкой")

    if len(s0) == 0:
        raise ValueError("Подстрока s0 не может быть пустой")

    if len(s0) > len(s):
        return s

    result = ""
    i = 0

    for i in range(len(s)):

        if i <= len(s) - len(s0) and s[i:i + len(s0)] == s0:
            continue
        else:
            result += s[i]

    return result

if __name__ == "__main__":
    try:
        S = "Привет, мир! Мир прекрасен!"
        S0 = "мир"

        result = remove_substring(S, S0)
        print(f"Исходная строка: '{S}'")
        print(f"Подстрока для удаления: '{S0}'")
        print(f"Результат: '{result}'")

        S2 = "Hello, World!"
        S0_2 = "xyz"
        result2 = remove_substring(S2, S0_2)
        print(f"\nИсходная строка: '{S2}'")
        print(f"Подстрока для удаления: '{S0_2}'")
        print(f"Результат: '{result2}'")

    except ValueError as e:
        print(f"Ошибка: {e}")