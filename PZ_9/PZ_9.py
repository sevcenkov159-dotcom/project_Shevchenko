magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
buk_market = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

print(f"Магистр:   {magistr}")
print(f"ДомКниги:  {dom_knigi}")
print(f"БукМаркет: {buk_market}")
print(f"Галерея:   {galereya}")
print("-" * 50)

all_books = magistr | dom_knigi | buk_market | galereya
print(f"1. Полный набор книг в городе:\n   {all_books}\n")

common_books = magistr & dom_knigi & buk_market & galereya
print(f"2. Книги, которые есть во всех магазинах:\n   {common_books}\n")

not_in_all_shops = all_books - common_books

if not_in_all_shops:
    single_book = list(not_in_all_shops)[0]
    print(f"3. Пример книги, которой НЕТ в некоторых магазинах:\n   '{single_book}'")
    print(f"   (Всего таких книг {len(not_in_all_shops)} шт: {not_in_all_shops})")
else:
    print("3. Таких книг нет, ассортимент всех магазинов абсолютно идентичен.")