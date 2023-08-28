import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dataBaseModule.import_data_products import import_products
from REGISTRATION import Registration


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Загружаем данные из Excel перед созданием и отображением первого окна
    # import_products("excel.xlsx")

    # Создаем и отображаем первое окно (startReg)
    startReg = Registration(app)
    # startReg.show()

    # Запускаем цикл обработки событий приложения
    sys.exit(app.exec_())


