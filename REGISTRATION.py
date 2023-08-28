import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
from authentication import Ui_Form
from df_conf import CheckThread
from dataBaseModule.import_data_products import import_products
from enter_prod import Enter_Products
from main_module import select_products
from PyQt5.Qt import Qt
from DIARY import Diary


class Registration(QMainWindow):

    def __init__(self, app):
        super(Registration, self).__init__()
        self.AUTH = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.AUTH)
        self.setWindowTitle('Registration Window')
        self.start_Diary = None
        self.name_product = ''
        self.amount_product = 0
        self.AUTH.show()

        self.ui.signIn_button.setDefault(True)

        self.ui.signIn_button.clicked.connect(self.auth)
        self.ui.signUp_button.clicked.connect(self.reg)
        self.authlist = [self.ui.login_line, self.ui.password_line]
        self.authData = [self.ui.login_line.text(), self.ui.password_line.text()]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

        self.diary_window = None  # Экземпляр окна Diary

    # Проверка правильности ввода
    def check_input(funct):
        try:
            def wrapper(self):
                for line_edit in self.authlist:
                    if len(line_edit.text()) == 0:
                        return
                funct(self)
            return wrapper
        except Exception as e:
            print(f"check_input {e}")

    @check_input
    def auth(self):
        try:
            name = self.ui.login_line.text()
            password = self.ui.password_line.text()

            self.authData = [self.ui.login_line.text(), self.ui.password_line.text()]

            self.check_db.thr_login(name, password)
        except Exception as e:
            print(f"auth {e}")

    @check_input
    def reg(self):
        try:
            name = self.ui.login_line.text()
            passw = self.ui.password_line.text()
            self.check_db.thr_register(name, passw)
        except Exception as e:
            print(f"reg {e}")

    def goNextPage(self):
        try:
            print("Opening Diary window")
            self.start_Diary = Diary(self.authData)
            self.AUTH.close()
        except Exception as e:
            print(f"goNextPage {e}")

    # Обработчик сигналов
    def signal_handler(self, value):
        try:
            QtWidgets.QMessageBox.about(self, 'Оповещение', value)
            if value == 'Успешная авторизация!':
                print("Correct")
                self.goNextPage()
        except Exception as e:
            print(f"signal_handler {e}")

