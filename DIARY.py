import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from authentication import Ui_Form
from df_conf import CheckThread
from dataBaseModule.import_data_products import import_products
from enter_prod import Enter_Products
from main_module import select_products_thr
from graphics import Hystogram_classic, Circle_hystogram
from PyQt5.Qt import Qt
from dateutil.relativedelta import relativedelta
import sqlite3
import numpy as np
import datetime
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure


class Diary(QWidget):
    def __init__(self, authData):
        try:
            super(Diary, self).__init__()
            self.Products_Window = QtWidgets.QMainWindow()
            self.gui = Enter_Products()
            self.gui.setupUi(self.Products_Window)
            self.setWindowTitle('Diary Window')

            self.authData = authData
            self.name_product = ''
            self.amount_product = 0
            self.colories = 0
            self.user_id = None
            products_list = select_products_thr()
            self.gui.SelectComboBox.addItems(products_list)
            self.gui.SelectComboBox.setEditable(True)
            self.gui.SelectComboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

            # change completion mode of the default completer from InlineCompletion to PopupCompletion
            self.gui.SelectComboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

            self.gui.EnterButton.clicked.connect(self.input_data)

            self.gui.tabWidget.currentChanged.connect(self.tab_changed)
            self.set_user_id()

            self.init_widgets()

            self.gui.calendarWidget.selectionChanged.connect(self.calendarDateChanged)

            self.Products_Window.show()
        except Exception as e:
            print(f"Init :{e}")

    def changeGraphicBar(self):
        try:
            # получаем информацию о бжу выбранного дня
            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()

            # потом обновляем информацию о колориях за данный день
            # далее обновляем информацию и гистограмме
            def read_curr_colories(date):
                c.execute("SELECT * FROM nutrition WHERE user_id = ? AND date_meal = ?", (self.user_id, date))
                result_strings = c.fetchall()
                colories = 0
                proteins = 0
                fats = 0
                carbohydrates = 0

                if result_strings:
                    for value in result_strings:
                        product_name = value[2]
                        amount_prod = value[3]
                        c.execute("SELECT * FROM products WHERE product = ?", (product_name,))
                        prod_strings = c.fetchall()[0]
                        colories += (prod_strings[5] * amount_prod)/100
                        proteins += (prod_strings[3] * amount_prod)/100
                        fats += (prod_strings[2] * amount_prod)/100
                        carbohydrates += (prod_strings[4] * amount_prod)/100
                else:
                    return 0

                return colories

            self.date_before_7 = (self.dataSelected - relativedelta(days=6)).date()
            current_date = self.dataSelected.date()

            date_list = []
            cal_list = []

            while self.date_before_7 <= current_date:
                date_list.append(self.date_before_7.strftime('%d.%m.%Y'))
                self.date_before_7 += datetime.timedelta(days=1)

            i = 0
            for date in date_list:
                count_colories = read_curr_colories(date)
                cal_list.append(count_colories)
                i += 1

            new_date_list = []

            for date_string in date_list:
                date_object = datetime.datetime.strptime(date_string, '%d.%m.%Y')
                new_date_string = date_object.strftime('%d.%m')
                new_date_list.append(new_date_string)

            return cal_list, new_date_list

        except Exception as e:
            print(f'changeGraphicBar: {e}')

    def changeGraphicPie(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()

            # Получаем текущее время
            current_time = self.dataSelected

            # Преобразуем время в строку в формате "день.месяц.год"
            formatted_time = current_time.strftime('%d.%m.%Y')

            c.execute("SELECT * FROM nutrition WHERE user_id = ? AND date_meal = ?", (self.user_id, formatted_time))

            result_strings = c.fetchall()
            colories = 0
            proteins = 0
            fats = 0
            carbohydrates = 0

            if result_strings:
                for value in result_strings:
                    product_name = value[2]
                    amount_prod = value[3]
                    c.execute("SELECT * FROM products WHERE product = ?", (product_name,))
                    prod_strings = c.fetchall()[0]
                    colories += (prod_strings[5] * amount_prod) / 100
                    proteins += (prod_strings[3] * amount_prod) / 100
                    fats += (prod_strings[2] * amount_prod) / 100
                    carbohydrates += (prod_strings[4] * amount_prod) / 100

            print(self.colories)

            self.gui.label_2.setText(str(colories).split('.')[0])
            # Закрываем соединение с базой данных
            conn.close()
            return colories, proteins, fats, carbohydrates
        except Exception as e:
            print(f'changeGraphicPie: {e}')

    def calendarDateChanged(self):
        try:
            print("The calendar date was changed")
            self.dataSelected = self.gui.calendarWidget.selectedDate().toPyDate()
            # Преобразуем объект date в объект datetime, добавляя время 00:00:00
            self.dataSelected = datetime.datetime.combine(self.dataSelected, datetime.time())

            colories, date_list = self.changeGraphicBar()

            self.matplotlibwidget_downer.axis.clear()

            self.matplotlibwidget_downer.axis.bar(date_list, colories)
            self.matplotlibwidget_downer.canvas.draw()
            # ставим данные значения в гистограмму
            colories, proteins, fats, carbohydrates = self.changeGraphicPie()

            self.matplotlibwidget_upper.axis.clear()
            data_circle = [proteins, fats, carbohydrates]  # Data values for each slice
            labels = ["Белки", "Жиры", "Углеводы"]  # Labels for each slice
            self.matplotlibwidget_upper.axis.pie(data_circle, labels=labels, autopct='%1.1f%%', startangle=90)
            self.matplotlibwidget_upper.canvas.draw()

            print(self.dataSelected)
        except Exception as e:
            print(f'calendarDateChanged: {e}')

    def set_user_id(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()
            c.execute("SELECT id FROM clients WHERE login = ? AND password = ?", (self.authData[0], self.authData[1]))
            result_id = c.fetchone()
            self.user_id = result_id[0]
            print(self.user_id)

            # # создадим таблицу с колориями за день
            # with open('calories.sql', 'r') as file:
            #     sql_script = file.read()
            # c.executescript(sql_script)
            #
            # # Получаем текущее время
            # current_time = datetime.datetime.now()
            #
            # # Преобразуем время в строку в формате "день.месяц.год"
            # formatted_time = current_time.strftime('%d.%m.%Y')
            #
            # c.execute('INSERT INTO calories (user_id, calories, date_meal) VALUES (?, ?, ?)',
            #           (self.user_id, self.colories, formatted_time))
            # conn.commit()

        except Exception as e:
            print(f"set_user_id: {e}")

    def calc_colories(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()

            # Получаем текущее время
            current_time = datetime.datetime.now()

            # Преобразуем время в строку в формате "день.месяц.год"
            formatted_time = current_time.strftime('%d.%m.%Y')

            c.execute("SELECT * FROM nutrition WHERE user_id = ? AND date_meal = ?", (self.user_id, formatted_time))

            result_strings = c.fetchall()
            self.colories = 0
            self.proteins = 0
            self.fats = 0
            self.carbohydrates = 0

            if result_strings:
                for value in result_strings:
                    product_name = value[2]
                    amount_prod = value[3]
                    c.execute("SELECT * FROM products WHERE product = ?", (product_name,))
                    prod_strings = c.fetchall()[0]
                    self.colories += (prod_strings[5] * amount_prod)/100
                    self.proteins += (prod_strings[3] * amount_prod)/100
                    self.fats += (prod_strings[2] * amount_prod)/100
                    self.carbohydrates += (prod_strings[4] * amount_prod)/100

            print(self.colories)

            self.gui.label_2.setText(str(self.colories).split('.')[0])
            # Закрываем соединение с базой данных
            conn.close()

            # В переменной result теперь хранится список кортежей, каждый из которых представляет строку с данными
            print(result_strings)
        except Exception as e:
            print(f"calc_colories: {e}")

    def set_values_bar(self):
        try:
            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()

            def read_curr_colories(curr_date):
                c.execute("SELECT * FROM nutrition WHERE user_id = ? AND date_meal = ?", (self.user_id, curr_date))
                result_strings = c.fetchall()
                colories = 0
                proteins = 0
                fats = 0
                carbohydrates = 0

                if result_strings:
                    for value in result_strings:
                        product_name = value[2]
                        amount_prod = value[3]
                        c.execute("SELECT * FROM products WHERE product = ?", (product_name,))
                        prod_strings = c.fetchall()[0]
                        colories += (prod_strings[5] * amount_prod)/100
                        proteins += (prod_strings[3] * amount_prod)/100
                        fats += (prod_strings[2] * amount_prod)/100
                        carbohydrates += (prod_strings[4] * amount_prod)/100
                else:
                    return 0

                return colories

            self.date_before_7 = (datetime.datetime.now() - relativedelta(days=6)).date()
            current_date = datetime.datetime.now().date()

            date_list = []
            cal_list = []

            while self.date_before_7 <= current_date:
                date_list.append(self.date_before_7.strftime('%d.%m.%Y'))
                self.date_before_7 += datetime.timedelta(days=1)

            i = 0
            for date in date_list:
                count_colories = read_curr_colories(date)
                cal_list.append(count_colories)
                i += 1

            new_date_list = []

            for date_string in date_list:
                date_object = datetime.datetime.strptime(date_string, '%d.%m.%Y')
                new_date_string = date_object.strftime('%d.%m')
                new_date_list.append(new_date_string)

            return cal_list, new_date_list
        except Exception as e:
            print(f'set_values_bar: {e}')

    def plot_widget(self):
        try:
            self.matplotlibwidget_downer.axis.clear()

            self.date_before_7 = (datetime.datetime.now() - relativedelta(days=6)).strftime('%d.%m.%Y')

            data, date_list = self.set_values_bar()  # Your data values here
            categories = date_list

            self.matplotlibwidget_downer.axis.bar(categories, data)
            self.matplotlibwidget_downer.canvas.draw()

            self.matplotlibwidget_upper.axis.clear()
            data_circle = [self.proteins, self.fats, self.carbohydrates]  # Data values for each slice
            labels = ["Белки", "Жиры", "Углеводы"]  # Labels for each slice
            self.matplotlibwidget_upper.axis.pie(data_circle, labels=labels, autopct='%1.1f%%', startangle=90)
            self.matplotlibwidget_upper.canvas.draw()
        except Exception as e:
            print(f"plot_widget: {e}")

    def init_widgets(self):
        try:
            self.matplotlibwidget_upper = Circle_hystogram()
            self.layoutvertical_upper = QVBoxLayout(self.gui.widget)
            self.layoutvertical_upper.addWidget(self.matplotlibwidget_upper)

            self.matplotlibwidget_downer = Hystogram_classic()
            self.layoutvertical_down = QVBoxLayout(self.gui.widget_2)
            self.layoutvertical_down.addWidget(self.matplotlibwidget_downer)
        except Exception as e:
            print(e)

    def input_data(self):
        try:
            self.name_product = self.gui.SelectComboBox.currentText()
            self.amount_product = self.gui.spinWeight.text().split()[0]

            conn = sqlite3.connect('data.sqlite')
            c = conn.cursor()
            with open('nutrition.sql', 'r') as file:
                sql_script = file.read()
            c.executescript(sql_script)

            # Получаем текущее время
            current_time = datetime.datetime.now()

            # Преобразуем время в строку в формате "день.месяц.год"
            formatted_time = current_time.strftime('%d.%m.%Y')

            c.execute('INSERT INTO nutrition (user_id, meal_type, weight, date_meal) VALUES (?, ?, ?, ?)', (self.user_id, self.name_product, self.amount_product, formatted_time))
            conn.commit()
            print("ID пользователя:", self.user_id)

            c.close()
        except Exception as e:
            print(e)

    def tab_changed(self, index):
        try:
            if index == self.gui.tabWidget.indexOf(self.gui.progress_tab):
                # Выполняйте действие только при переключении на вкладку self.progress_tab
                print("Switched to progress_tab")
                self.calc_colories()
                self.plot_widget()

        except Exception as e:
            print(e)


