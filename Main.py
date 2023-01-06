# This is main project file.this run and manage windows.

from PyQt6.QtWidgets import QWidget, QApplication
from Forms.LoginForm import Ui_LoginForm
from Forms.UserForm import Ui_Form
from Forms.AdminForm import Ui_AdminForm
import sys


class Main(QWidget, Ui_LoginForm):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


class AdminForm(QWidget, Ui_AdminForm):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

    def OPEN(self):
        self.show()
        Login.hide()


class UserForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

    def OPEN(self):
        self.show()
        Login.hide()


def loginProcces():
    loginState = Login.loginFunc()
    if loginState == 'successful':
        user_form.lblID.setText(Login.txtLogin_UserID.text())
        user_form.firstInit()
        user_form.OPEN()
        Login.hide()
    elif loginState == 'admin_login':
        admin_form.OPEN()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login = Main()
    user_form = UserForm()
    admin_form = AdminForm()
    Login.show()
    Login.btnLogin.clicked.connect(loginProcces)
    sys.exit(app.exec())
