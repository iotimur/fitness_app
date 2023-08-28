from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


class Enter_Products(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 638)
        MainWindow.setStyleSheet("background-color:rgb(170, 85, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.diary_tab = QtWidgets.QWidget()
        self.diary_tab.setObjectName("diary_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.diary_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.enter_product_label = QtWidgets.QLabel(self.diary_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.enter_product_label.setFont(font)
        self.enter_product_label.setTextFormat(QtCore.Qt.PlainText)
        self.enter_product_label.setObjectName("enter_product_label")
        self.horizontalLayout.addWidget(self.enter_product_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.SelectComboBox = QtWidgets.QComboBox(self.diary_tab)
        self.SelectComboBox.setMaximumSize(QtCore.QSize(521, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SelectComboBox.setFont(font)
        self.SelectComboBox.setStyleSheet("border: 2px solid dimgray;\n"
                                          "background-color: rgb(117, 117, 117)")
        self.SelectComboBox.setEditable(True)
        self.SelectComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.SelectComboBox.setObjectName("SelectComboBox")
        self.horizontalLayout.addWidget(self.SelectComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.weight_label = QtWidgets.QLabel(self.diary_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weight_label.setFont(font)
        self.weight_label.setObjectName("weight_label")
        self.horizontalLayout_2.addWidget(self.weight_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.spinWeight = QtWidgets.QSpinBox(self.diary_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinWeight.setFont(font)
        self.spinWeight.setStyleSheet("border: 2px solid dimgray;\n"
                                      "background-color: rgb(117, 117, 117)")
        self.spinWeight.setObjectName("spinWeight")

        # Устанавливаем минимальное и максимальное значение для spinWeight
        self.spinWeight.setRange(100, 1000)

        self.spinWeight.setSingleStep(100)

        self.spinWeight.setSuffix(" г")

        self.horizontalLayout_2.addWidget(self.spinWeight)

        self.horizontalLayout_2.addWidget(self.spinWeight)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.EnterButton = QtWidgets.QPushButton(self.diary_tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.EnterButton.setFont(font)
        self.EnterButton.setStyleSheet("border: 2px solid dimgray;\n"
                                       "background-color:rgb(255, 85, 127)")
        self.EnterButton.setObjectName("EnterButton")
        self.horizontalLayout_3.addWidget(self.EnterButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.diary_tab, "")
        self.progress_tab = QtWidgets.QWidget()
        self.progress_tab.setObjectName("progress_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.progress_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_1 = QtWidgets.QLabel(self.progress_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_4.addWidget(self.label_1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.progress_tab)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem9 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.widget = QtWidgets.QWidget(self.progress_tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4.addWidget(self.widget)
        spacerItem10 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.progress_tab)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_5.addWidget(self.calendarWidget)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem14)
        self.widget_2 = QtWidgets.QWidget(self.progress_tab)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3.addWidget(self.widget_2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem15)
        self.tabWidget.addTab(self.progress_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_product_label.setText(_translate("MainWindow", "Введите продукт"))
        self.EnterButton.setText(_translate("MainWindow", "Ввод"))
        self.weight_label.setText(_translate("MainWindow", "Вес "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diary_tab), _translate("MainWindow", "Дневник"))
        self.label_1.setText(_translate("MainWindow", "Калории за день:"))
        self.label_2.setText(_translate("MainWindow", "3000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.progress_tab), _translate("MainWindow", "Progress"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Products_Window = QtWidgets.QMainWindow()
    ui = Enter_Products()
    ui.setupUi(Products_Window)
    Products_Window.show()
    sys.exit(app.exec_())
