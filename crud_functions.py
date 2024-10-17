
import sqlite3

import sqlite3
def initiate_db():
    # Инициализация базы данных и создание таблицы
    connection = sqlite3.connect('Products.db')  # Убедитесь, что имя базы данных совпадает
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    )
    ''')

    # Загрузка тестовых данных только при первой инициализации базы данных
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:  # Проверяем, пустая ли таблица
        for i in range(1, 5):
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                           (f'Продукт{i}', f'Описание{i}', f'{i * 100}'))

    connection.commit()
    connection.close()


# Вызов функции при запуске скрипта
if __name__ == "__main__":
    initiate_db()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()  # Закрываем соединение после выполнения запроса
    return products

    