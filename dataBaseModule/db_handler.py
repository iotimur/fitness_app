import sqlite3
import os


def login(login, passw, signal):
    try:
        if os.path.exists('data.sqlite'):
            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()

            # Проверяем есть ли такой пользователь
            c.execute(f'SELECT * FROM clients WHERE login="{login}"')
            value = c.fetchall()

            if value != []:
                if value[0][2] == passw:
                    signal.emit('Успешная авторизация!')
            else:
                signal.emit('Проверьте правильность ввода данных!')

            c.close()
            c.close()
        else:
            signal.emit('Сначала зарегистрируйтесь!')
    except Exception as e:
        print(f"login {e}")


def register(login, passw, signal):
    try:
        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()
        with open('reg.sql', 'r') as file:
            sql_script = file.read()
        c.executescript(sql_script)

        c.execute(f'SELECT * FROM clients WHERE login="{login}"')
        value = c.fetchall()

        if value != []:
            signal.emit('Такой ник уже используется!')

        elif value == []:
            c.execute('INSERT INTO clients (login, password) VALUES (?, ?)',(login, passw))
            signal.emit('Вы успешно зарегистрированы!')
            conn.commit()

        c.close()

    except Exception as e:
        print(f"register {e}")