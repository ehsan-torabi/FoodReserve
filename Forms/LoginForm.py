# این کد صفحه ورود کاربر را طراحی و کنترل مقادیر آن را به عهده دارد
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Modules.UserModule import User


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(410, 260)
        LoginForm.setMinimumSize(QtCore.QSize(410, 260))
        LoginForm.setMaximumSize(QtCore.QSize(410, 260))
        font = QtGui.QFont()
        font.setFamily("IRANSans(FaNum)")
        LoginForm.setFont(font)
        LoginForm.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.frame = QtWidgets.QFrame(LoginForm)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 441, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btnRegister = QtWidgets.QPushButton(self.frame)
        self.btnRegister.setGeometry(QtCore.QRect(20, 220, 91, 31))
        self.btnRegister.setObjectName("btnRegister")
        self.btnLogin = QtWidgets.QPushButton(self.frame)
        self.btnLogin.setGeometry(QtCore.QRect(20, 80, 91, 31))
        self.btnLogin.setObjectName("btnLogin")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 110, 411, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.lblName = QtWidgets.QLabel(self.frame)
        self.lblName.setGeometry(QtCore.QRect(350, 140, 49, 16))
        self.lblName.setObjectName("lblName")
        self.lblFamily = QtWidgets.QLabel(self.frame)
        self.lblFamily.setGeometry(QtCore.QRect(330, 170, 71, 20))
        self.lblFamily.setObjectName("lblFamily")
        self.lblRegister_Password = QtWidgets.QLabel(self.frame)
        self.lblRegister_Password.setGeometry(QtCore.QRect(350, 200, 49, 16))
        self.lblRegister_Password.setObjectName("lblRegister_Password")
        self.lblLogin_Password = QtWidgets.QLabel(self.frame)
        self.lblLogin_Password.setGeometry(QtCore.QRect(350, 60, 49, 16))
        self.lblLogin_Password.setObjectName("lblLogin_Password")
        self.lblLogin_UserID = QtWidgets.QLabel(self.frame)
        self.lblLogin_UserID.setGeometry(QtCore.QRect(308, 30, 91, 20))
        self.lblLogin_UserID.setObjectName("lblLogin_UserID")
        self.lblRegister_UserID = QtWidgets.QLabel(self.frame)
        self.lblRegister_UserID.setGeometry(QtCore.QRect(350, 230, 49, 16))
        self.lblRegister_UserID.setObjectName("lblRegister_Password")
        self.txtRegister_Password = QtWidgets.QLineEdit(self.frame)
        self.txtRegister_Password.setGeometry(QtCore.QRect(130, 200, 171, 21))
        self.txtRegister_Password.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                               QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtRegister_Password.setObjectName("txtRegister_Password")
        self.txtRegister_UserID = QtWidgets.QLineEdit(self.frame)
        self.txtRegister_UserID.setGeometry(QtCore.QRect(130, 230, 171, 21))
        self.txtRegister_UserID.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                             QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtRegister_UserID.setObjectName("txtRegister_UserID")
        self.txtRegister_Family = QtWidgets.QLineEdit(self.frame)
        self.txtRegister_Family.setGeometry(QtCore.QRect(130, 170, 171, 21))
        self.txtRegister_Family.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                             QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtRegister_Family.setObjectName("txtRegister_Family")
        self.txtRegister_Name = QtWidgets.QLineEdit(self.frame)
        self.txtRegister_Name.setGeometry(QtCore.QRect(130, 140, 171, 21))
        self.txtRegister_Name.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtRegister_Name.setObjectName("txtRegister_Name")
        self.txtLogin_Password = QtWidgets.QLineEdit(self.frame)
        self.txtLogin_Password.setGeometry(QtCore.QRect(130, 60, 171, 21))
        self.txtLogin_Password.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                            QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtLogin_Password.setObjectName("txtLogin_Password")
        self.txtLogin_UserID = QtWidgets.QLineEdit(self.frame)
        self.txtLogin_UserID.setGeometry(QtCore.QRect(130, 30, 171, 21))
        self.txtLogin_UserID.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtLogin_UserID.setObjectName("txtLogin_UserID")
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
        self.btnRegister.clicked.connect(self.registerFunc)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowIcon(QtGui.QIcon('Files//login.png'))
        LoginForm.setWindowTitle(_translate("LoginForm", "سیستم رزرو غذا"))
        ############################ Register #################################
        self.lblName.setText(_translate("LoginForm", "نام:"))
        self.lblFamily.setText(_translate("LoginForm", "نام خانوادگی:"))
        self.lblRegister_Password.setText(_translate("LoginForm", "پسورد:"))
        self.lblRegister_UserID.setText(_translate("LoginForm", "کد ملی:"))
        self.btnRegister.setText(_translate("LoginForm", "ثبت نام"))
        self.txtRegister_UserID.setMaxLength(10)
        ############################ Login ####################################
        self.lblLogin_Password.setText(_translate("LoginForm", "پسورد:"))
        self.lblLogin_UserID.setText(_translate("LoginForm", "کد ملی:"))
        self.btnLogin.setText(_translate("LoginForm", "ورود"))
        self.txtLogin_UserID.setMaxLength(10)
        #######################################################################

    def showMsg(self, massage, title):
        msg = QMessageBox()
        msg.setText(massage)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('Files//msg.png'))
        msg.exec()

    def registerFunc(self):
        name = self.txtRegister_Name.text()
        family = self.txtRegister_Family.text()
        password = self.txtRegister_Password.text()
        id = self.txtRegister_UserID.text()
        if id != '' and name != '' and password != '' and family != '':
            registerState = User.register(name, family, password, id)
            if registerState == 'successful':
                self.showMsg('ثبت نام با موفقیت انجام شد',
                             'عملیات موفقیت آمیز')
            else:
                self.showMsg('این کد ملی قبلا ثبت نام شده است!',
                             'عملیات ناموفق')
        else:
            self.showMsg('لطفا همه فیلد ها را کامل کنید', 'خطا')

    def loginFunc(self):
        Uid = self.txtLogin_UserID.text()
        pasword = self.txtLogin_Password.text()
        if Uid != '' and pasword != '':
            Uid = self.txtLogin_UserID.text()
            pasword = self.txtLogin_Password.text()
            loginState = User.login(Uid, pasword)
            if loginState == 'successful':
                self.showMsg('ورود با موفقیت انجام شد', 'عملیات موفقیت آمیز')
            elif loginState == 'failed':
                self.showMsg('نام کاربری یا رمز عبور اشتباه است', 'خطا')
            return loginState
        elif Uid == '' and pasword == '':
            self.showMsg('لطفا همه فیلد ها را کامل کنید', 'خطا')

#############################################################
