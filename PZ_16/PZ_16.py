import math

class Circle:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def diameter(self) -> float:
        return 2 * self.radius


# Тестовые запуски для класса Circle
if __name__ == "__main__":
    print("Тестирование класса Circle")
    print("-" * 40)

    # Создание объекта с радиусом 5
    circle1 = Circle(5)
    print(f"Радиус: {circle1.radius}")
    print(f"Площадь: {circle1.area():.2f}")
    print(f"Длина окружности: {circle1.circumference():.2f}")
    print(f"Диаметр: {circle1.diameter():.2f}")
    print()

    # Тест с дробным радиусом
    circle2 = Circle(3.5)
    print(f"Радиус: {circle2.radius}")
    print(f"Площадь: {circle2.area():.2f}")
    print(f"Длина окружности: {circle2.circumference():.2f}")
    print(f"Диаметр: {circle2.diameter():.2f}")
    print()

    # Тест обработки некорректного значения
    try:
        circle3 = Circle(-2)
    except ValueError as e:
        print(f"Ожидаемая ошибка при отрицательном радиусе: {e}")