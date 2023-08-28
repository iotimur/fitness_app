import pandas as pd
import sqlite3
import os


def import_products(filepath: str):
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()

    try:
        conn.execute("SELECT count(*) FROM products")
        result = c.fetchall()
        print(result)

    except sqlite3.OperationalError:
        df_products = pd.read_excel(filepath)

        with open('imp_prod.sql', 'r') as file:
            sql_script = file.read()
        c.executescript(sql_script)

        # Преобразование колонок в списки
        products_data = df_products[
            ['Продукт', 'Жиры, г', 'Белки, г', 'Углеводы, г', 'Калорийность, Ккал']].values.tolist()

        # Вставка данных с помощью executemany()
        c.executemany('INSERT INTO products (product, fats, proteins, carbohydrates, calories) VALUES (?, ?, ?, ?, ?)',
                      products_data)
        conn.commit()

    c.close()

