

dictionary = {
    "cat": "кошка",
    "dog": "собака",
    "bird": "птица",
    "mouse": "мышь",
    "apple": "яблоко",
    "book": "книга",
    "home": "дом"
}

print(f"Исходный словарь (7 слов): {dictionary}\n")

new_words = {"elephant": "слон", "water": "вода"}

for eng, rus in new_words.items():
    if eng not in dictionary:
        dictionary[eng] = rus

print("Добавим 10-е слово в словарь вручную:")
user_eng = input("Введите слово на английском: ").strip().lower()
user_rus = input("Введите перевод на русский: ").strip().lower()

if user_eng not in dictionary:
    dictionary[user_eng] = user_rus
else:
    print(f"Слово '{user_eng}' уже есть в словаре!")

print("\n--- Финальные результаты работы со словарем ---")

print(f"Весь словарь целиком:\n{dictionary}\n")

print("Поэлементный вывод (ключ - значение):")
for eng_word, rus_word in dictionary.items():
    print(f"Английский: {eng_word:10} | Русский: {rus_word}")