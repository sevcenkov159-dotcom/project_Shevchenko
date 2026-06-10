
class Person:
    def __init__(self, name: str, age: int, sex: str) -> None:
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if sex not in ("мужской", "женский"):
            raise ValueError("Пол должен быть 'мужской' или 'женский'.")
        self.name = name
        self.age = age
        self.sex = sex

    def display_sex(self) -> None:
        print(f"{self.name} имеет пол: {self.sex}")


class Man(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, "мужской")

    def display_sex(self) -> None:
        print(f"Объект Man: {self.name}, возраст {self.age}, является мужчиной.")


class Woman(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, "женский")

    def display_sex(self) -> None:
        print(f"Объект Woman: {self.name}, возраст {self.age}, является женщиной.")


if __name__ == "__main__":
    print("Тестирование классов Person, Man, Woman")
    print("-" * 40)

    person = Person("Алекс", 30, "мужской")
    person.display_sex()
    print()

    man = Man("Иван", 25)
    man.display_sex()
    print()

    woman = Woman("Мария", 28)
    woman.display_sex()
    print()

    print(f"Имя мужчины: {man.name}, Возраст: {man.age}, Пол: {man.sex}")
    print(f"Имя женщины: {woman.name}, Возраст: {woman.age}, Пол: {woman.sex}")
    print()

    try:
        bad_person = Person("Ошибка", -5, "женский")
    except ValueError as e:
        print(f"Ошибка создания Person (неверный возраст): {e}")

    try:
        bad_person2 = Person("Ошибка", 20, "неопределён")
    except ValueError as e:
        print(f"Ошибка создания Person (неверный пол): {e}")