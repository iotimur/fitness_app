import sqlite3
from threading import Thread


def select_products_thr() -> list:
    result_list = []
    t1 = Thread(target=select_products, args=(result_list,))
    t1.start()
    t1.join()
    return result_list


def select_products(result_list: list) -> list:
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()

    # Выполнение SQL-запроса для выборки значения столбца "product"
    c.execute("SELECT product FROM products")

    # Получение всех результатов запроса в виде списка
    products_list = [row[0] for row in c.fetchall()]

    result_list.extend(products_list)

    # Закрытие соединения с базой данных
    conn.close()
