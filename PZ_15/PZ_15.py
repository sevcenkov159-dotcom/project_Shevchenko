
import sqlite3
import sys
from typing import List, Tuple, Optional, Dict, Any

DATABASE_NAME = 'jewelry_workshop.db'
TABLE_NAME = 'Изделие'
TABLE_STRUCTURE = """
    CREATE TABLE IF NOT EXISTS Изделие (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_full_name TEXT NOT NULL,
        master_full_name TEXT NOT NULL,
        product_type TEXT NOT NULL,
        material TEXT NOT NULL,
        work_cost REAL NOT NULL CHECK(work_cost > 0)
    )
"""

INITIAL_DATA = [
    ('Иванов Иван Иванович', 'Петров Петр Петрович', 'Кольцо', 'Золото', 15000.00),
    ('Смирнова Анна Сергеевна', 'Сидоров Алексей Викторович', 'Серьги', 'Серебро', 8500.00),
    ('Кузнецов Дмитрий Андреевич', 'Петров Петр Петрович', 'Цепочка', 'Золото', 22000.00),
    ('Попова Елена Владимировна', 'Козлова Мария Игоревна', 'Браслет', 'Платина', 35000.00),
    ('Васильев Сергей Николаевич', 'Сидоров Алексей Викторович', 'Подвеска', 'Золото', 12000.00),
    ('Новикова Ольга Александровна', 'Козлова Мария Игоревна', 'Кольцо', 'Серебро', 7500.00),
    ('Морозов Андрей Павлович', 'Петров Петр Петрович', 'Брошь', 'Золото', 18000.00),
    ('Волкова Татьяна Игоревна', 'Сидоров Алексей Викторович', 'Колье', 'Платина', 45000.00),
    ('Зайцев Роман Викторович', 'Козлова Мария Игоревна', 'Запонки', 'Золото', 16000.00),
    ('Соловьева Мария Дмитриевна', 'Петров Петр Петрович', 'Диадема', 'Серебро с позолотой', 28000.00)
]


def create_connection() -> sqlite3.Connection:
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        sys.exit(1)


def initialize_database(connection: sqlite3.Connection) -> None:
    try:
        cursor = connection.cursor()
        cursor.execute(TABLE_STRUCTURE)
        connection.commit()
        print("База данных инициализирована успешно.")
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации базы данных: {e}")
        raise


def fill_initial_data(connection: sqlite3.Connection) -> None:
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.executemany(
                f"INSERT INTO {TABLE_NAME} (client_full_name, master_full_name, product_type, material, work_cost) "
                f"VALUES (?, ?, ?, ?, ?)",
                INITIAL_DATA
            )
            connection.commit()
            print(f"Добавлено {len(INITIAL_DATA)} начальных записей.")
        else:
            print(f"В таблице уже есть данные ({count} записей).")
    except sqlite3.Error as e:
        print(f"Ошибка при заполнении начальными данными: {e}")
        connection.rollback()
        raise


def add_record(connection: sqlite3.Connection, client_fio: str, master_fio: str,
               product_type: str, material: str, work_cost: float) -> None:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (client_full_name, master_full_name, product_type, material, work_cost) "
            f"VALUES (?, ?, ?, ?, ?)",
            (client_fio, master_fio, product_type, material, work_cost)
        )
        connection.commit()
        print(f"Запись успешно добавлена. ID: {cursor.lastrowid}")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении записи: {e}")
        connection.rollback()
        raise


def search_by_client(connection: sqlite3.Connection, client_fio: str) -> List[Dict[str, Any]]:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM {TABLE_NAME} WHERE client_full_name LIKE ?",
            (f"%{client_fio}%",)
        )
        return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Ошибка при поиске по клиенту: {e}")
        return []


def search_by_master(connection: sqlite3.Connection, master_fio: str) -> List[Dict[str, Any]]:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM {TABLE_NAME} WHERE master_full_name LIKE ?",
            (f"%{master_fio}%",)
        )
        return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Ошибка при поиске по мастеру: {e}")
        return []


def search_by_product_and_material(connection: sqlite3.Connection, product_type: str, material: str) -> List[
    Dict[str, Any]]:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM {TABLE_NAME} WHERE product_type LIKE ? AND material LIKE ?",
            (f"%{product_type}%", f"%{material}%")
        )
        return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Ошибка при поиске по изделию и материалу: {e}")
        return []


def delete_by_id(connection: sqlite3.Connection, record_id: int) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (record_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Запись с ID {record_id} успешно удалена.")
            return True
        else:
            print(f"Запись с ID {record_id} не найдена.")
            return False
    except sqlite3.Error as e:
        print(f"Ошибка при удалении записи: {e}")
        connection.rollback()
        return False


def delete_by_master(connection: sqlite3.Connection, master_fio: str) -> int:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM {TABLE_NAME} WHERE master_full_name LIKE ?",
            (f"%{master_fio}%",)
        )
        connection.commit()
        deleted_count = cursor.rowcount
        print(f"Удалено записей: {deleted_count}")
        return deleted_count
    except sqlite3.Error as e:
        print(f"Ошибка при удалении записей: {e}")
        connection.rollback()
        return 0


def delete_expensive_products(connection: sqlite3.Connection, min_cost: float) -> int:
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE work_cost > ?", (min_cost,))
        connection.commit()
        deleted_count = cursor.rowcount
        print(f"Удалено записей со стоимостью более {min_cost}: {deleted_count}")
        return deleted_count
    except sqlite3.Error as e:
        print(f"Ошибка при удалении дорогих записей: {e}")
        connection.rollback()
        return 0


def update_by_id(connection: sqlite3.Connection, record_id: int,
                 updates: Dict[str, Any]) -> bool:

    try:
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [record_id]

        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET {set_clause} WHERE id = ?",
            values
        )
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Запись с ID {record_id} успешно обновлена.")
            return True
        else:
            print(f"Запись с ID {record_id} не найдена.")
            return False
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении записи: {e}")
        connection.rollback()
        return False


def update_master_cost(connection: sqlite3.Connection, master_fio: str,
                       cost_increase_percent: float) -> int:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET work_cost = work_cost * (1 + ? / 100) "
            f"WHERE master_full_name LIKE ?",
            (cost_increase_percent, f"%{master_fio}%")
        )
        connection.commit()
        updated_count = cursor.rowcount
        print(f"Обновлено записей для мастера {master_fio}: {updated_count}")
        return updated_count
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении стоимости: {e}")
        connection.rollback()
        return 0


def update_material_for_product(connection: sqlite3.Connection, product_type: str,
                                old_material: str, new_material: str) -> int:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET material = ? "
            f"WHERE product_type LIKE ? AND material LIKE ?",
            (new_material, f"%{product_type}%", f"%{old_material}%")
        )
        connection.commit()
        updated_count = cursor.rowcount
        print(f"Обновлено записей: {updated_count}")
        return updated_count
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении материала: {e}")
        connection.rollback()
        return 0


def display_records(records: List[Dict[str, Any]]) -> None:

    if not records:
        print("Записи не найдены.")
        return

    print("\n" + "=" * 100)
    print(f"{'ID':<5} {'Клиент':<30} {'Мастер':<30} {'Изделие':<15} {'Материал':<15} {'Стоимость':>10}")
    print("=" * 100)

    for record in records:
        print(f"{record['id']:<5} {record['client_full_name']:<30} {record['master_full_name']:<30} "
              f"{record['product_type']:<15} {record['material']:<15} {record['work_cost']:>10.2f}")

    print("=" * 100)
    print(f"Всего записей: {len(records)}")


def get_all_records(connection: sqlite3.Connection) -> List[Dict[str, Any]]:

    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Ошибка при получении записей: {e}")
        return []


def demonstrate_search(connection: sqlite3.Connection) -> None:
    print("\n=== Демонстрация поиска ===")

    print("\n1. Поиск по клиенту 'Иванов':")
    results = search_by_client(connection, "Иванов")
    display_records(results)

    print("\n2. Поиск по мастеру 'Петров':")
    results = search_by_master(connection, "Петров")
    display_records(results)

    print("\n3. Поиск колец из золота:")
    results = search_by_product_and_material(connection, "Кольцо", "Золото")
    display_records(results)


def demonstrate_delete(connection: sqlite3.Connection) -> None:

    print("\n=== Демонстрация удаления ===")

    print("\nТекущие записи в БД:")
    display_records(get_all_records(connection))

    print("\n1. Удаление записи с ID 1:")
    delete_by_id(connection, 1)

    print("\n2. Удаление записей мастера 'Сидоров':")
    delete_by_master(connection, "Сидоров")

    print("\n3. Удаление изделий стоимостью более 40000:")
    delete_expensive_products(connection, 40000)


def demonstrate_update(connection: sqlite3.Connection) -> None:
    print("\n=== Демонстрация обновления ===")

    print("\n1. Обновление записи с ID 2 (изменение стоимости):")
    update_by_id(connection, 2, {"work_cost": 30000.00})

    print("\n2. Увеличение стоимости на 10% для мастера 'Петров':")
    update_master_cost(connection, "Петров", 10.0)

    print("\n3. Замена материала 'Золото' на 'Белое золото' для колец:")
    update_material_for_product(connection, "Кольцо", "Золото", "Белое золото")


def add_demonstration_record(connection: sqlite3.Connection) -> None:
    """
    Добавление демонстрационной записи.
    """
    print("\n=== Добавление новой записи ===")
    add_record(
        connection,
        "Демонстрационный Клиент И.О.",
        "Демонстрационный Мастер И.О.",
        "Кулон",
        "Платина",
        42000.00
    )


def main() -> None:
    """
    Главная функция программы.
    """
    print("Программа 'Ювелирная мастерская'")
    print("-" * 50)

    connection = create_connection()

    try:
        initialize_database(connection)

        fill_initial_data(connection)

        print("\nНачальные данные в БД:")
        display_records(get_all_records(connection))

        add_demonstration_record(connection)

        print("\nДанные после добавления:")
        display_records(get_all_records(connection))

        demonstrate_search(connection)

        demonstrate_update(connection)

        print("\nДанные после обновлений:")
        display_records(get_all_records(connection))

        demonstrate_delete(connection)

        print("\nИтоговые данные в БД:")
        display_records(get_all_records(connection))

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        connection.rollback()
    finally:
        connection.close()
        print("\nСоединение с базой данных закрыто.")


if __name__ == "__main__":
    main()