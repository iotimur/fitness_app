from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 212)
        Form.setStyleSheet("background-color:rgb(92, 92, 92)")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line.setStyleSheet("background-color: rgb(117, 117, 117)")
        self.login_line.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.login_line)
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setStyleSheet("background-color: rgb(117, 117, 117)")
        self.password_line.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.password_line)
        self.signIn_button = QtWidgets.QPushButton(self.centralwidget)
        self.signIn_button.setStyleSheet("background-color:rgb(255, 85, 127)")
        self.signIn_button.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.signIn_button)
        self.signUp_button = QtWidgets.QPushButton(self.centralwidget)
        self.signUp_button.setStyleSheet("background-color:rgb(255, 85, 127)")
        self.signUp_button.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.signUp_button)
        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_line.setPlaceholderText(_translate("MainWindow", "Login"))
        self.password_line.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signIn_button.setText(_translate("MainWindow", "Sign in"))
        self.signUp_button.setText(_translate("MainWindow", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
