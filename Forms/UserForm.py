from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QInputDialog, QMessageBox
from Modules.FoodModule import Food
from Modules.UserModule import User
import Modules.pdModel as pdModel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        Form.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setFamily("IRANSans(FaNum)")
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)

        self.btnFoodReserve = QtWidgets.QPushButton(Form)
        self.btnFoodReserve.setGeometry(QtCore.QRect(250, 240, 141, 61))
        self.btnFoodReserve.setObjectName("btnFoodReserve")
        self.btnChargeBalance = QtWidgets.QPushButton(Form)
        self.btnChargeBalance.setGeometry(QtCore.QRect(250, 150, 141, 61))
        self.btnChargeBalance.setObjectName("btnChargeBalance")
        self.foodListVeiw = QtWidgets.QTableView(Form)
        self.foodListVeiw.setGeometry(QtCore.QRect(20, 120, 211, 261))
        self.foodListVeiw.setLayoutDirection(
            QtCore.Qt.LayoutDirection.RightToLeft)
        self.foodListVeiw.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.foodListVeiw.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.foodListVeiw.setObjectName("foodListVeiw")
        self.lblMenu = QtWidgets.QLabel(Form)
        self.lblMenu.setGeometry(QtCore.QRect(230, 110, 61, 20))
        self.lblMenu.setObjectName("lblMenu")
        self.lblBalancePerfix = QtWidgets.QLabel(Form)
        self.lblBalancePerfix.setGeometry(QtCore.QRect(298, 310, 81, 20))
        self.lblBalancePerfix.setObjectName("lblBalancePerfix")
        self.lblBalance = QtWidgets.QLabel(Form)
        self.lblBalance.setGeometry(QtCore.QRect(290, 340, 200, 20))
        self.lblBalance.setObjectName("lblBalance")
        self.lblMoneyUnit = QtWidgets.QLabel(Form)
        self.lblMoneyUnit.setGeometry(QtCore.QRect(248, 340, 31, 20))
        self.lblMoneyUnit.setObjectName("lblMoneyUnit")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 371, 80))
        palette = QtGui.QPalette()

        self.frame.setPalette(palette)
        self.frame.setStyleSheet("background-color: #1E1E24;\n"
                                 "border-radius:5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblWelcome = QtWidgets.QLabel(self.frame)
        self.lblWelcome.setGeometry(QtCore.QRect(200, 30, 161, 20))
        self.lblWelcome.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblWelcome.setObjectName("lblWelcome")

        self.lblUserIDPerfix = QtWidgets.QLabel(self.frame)
        self.lblUserIDPerfix.setGeometry(QtCore.QRect(310, 10, 50, 20))
        self.lblUserIDPerfix.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblUserIDPerfix.setObjectName("lblUserIDPerfix")
        self.lblID = QtWidgets.QLabel(self.frame)
        self.lblID.setGeometry(QtCore.QRect(230, 10, 80, 25))
        self.lblID.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblID.setObjectName("lblID")

        self.lblNamePerfix = QtWidgets.QLabel(self.frame)
        self.lblNamePerfix.setGeometry(QtCore.QRect(100, 10, 80, 25))
        self.lblNamePerfix.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblNamePerfix.setObjectName("lblNamePerfix")

        self.lblName_Family = QtWidgets.QLabel(self.frame)
        self.lblName_Family.setGeometry(QtCore.QRect(60, 10, 80, 25))
        self.lblName_Family.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblName_Family.setObjectName("lblName_Family")
#########################################################################
        self.lblFoodReservePerfix = QtWidgets.QLabel(self.frame)
        self.lblFoodReservePerfix.setGeometry(QtCore.QRect(200, 50, 161, 20))
        self.lblFoodReservePerfix.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblFoodReservePerfix.setObjectName("lblFoodReservePerfix")
        self.lblFoodReserve = QtWidgets.QLabel(self.frame)
        self.lblFoodReserve.setGeometry(QtCore.QRect(100, 50, 161, 20))
        self.lblFoodReserve.setStyleSheet("color:rgb(255, 255, 255)")
        self.lblFoodReserve.setObjectName("lblFoodReservePerfix")
        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setFamily("IRANSans(FaNum)")
        self.lblID.setFont(myFont)
        self.lblFoodReserve.setFont(myFont)
        self.lblName_Family.setFont(myFont)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnChargeBalance.clicked.connect(self.chargeBalance)
        self.btnFoodReserve.clicked.connect(self.reserveFood)
        self.foodListVeiw.setShowGrid(True)
        self.lblWelcome.setFont(font)
        self.lblUserIDPerfix.setFont(font)
        self.lblNamePerfix.setFont(font)
        self.lblFoodReservePerfix.setFont(font)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('Files//logo.png'))
        Form.setWindowTitle(_translate("Form", "سیستم رزرو غذا"))
        self.btnFoodReserve.setText(_translate("Form", "رزرو غذا"))
        self.btnChargeBalance.setText(_translate("Form", "افزایش موجودی"))
        self.lblMenu.setText(_translate("Form", "منو غذا ها:"))
        self.lblBalancePerfix.setText(_translate("Form", "موجودی فعلی:"))
        self.lblBalance.setText(_translate("Form", ''))
        self.lblMoneyUnit.setText(_translate("Form", "تومان"))
        self.lblWelcome.setText(_translate(
            "Form", "به سیستم رزرو غذاخوش آمدید!"))
        self.lblID.setText(_translate("Form", ''))
        self.lblUserIDPerfix.setText(_translate("Form", 'کد ملی:'))
        self.lblFoodReservePerfix.setText(
            _translate("Form", 'غذای  رزرو شده من:'))
        self.lblFoodReserve.setText(_translate("Form", ''))
        self.lblNamePerfix.setText(_translate('Form', 'نام:'))
        self.lblName_Family.setText(_translate('Form', ""))
        self.firstInit()


######## funcs########


    def firstInit(self):
        # First init function
        foodModel = pdModel.pandasModel(Food.listFaHeader())
        self.lblBalance.setText(str(User.getBalance(self.lblID.text())))
        if str(User.getFoodReserve_by_ID(self.lblID.text())) == 'nan':
            self.lblFoodReserve.setText('هنوز غذایی رزرو نکرده اید')
        else:
            self.lblFoodReserve.setText(
                str(User.getFoodReserve_by_ID(self.lblID.text())))

            #############################################################
        self.lblName_Family.setText(
            User.getNameAndFamily_by_ID(self.lblID.text()))
        self.foodListVeiw.setModel(foodModel)
        self.foodListVeiw.setColumnWidth(0, 50)
        self.foodListVeiw.setColumnWidth(1, 80)
        self.foodListVeiw.setColumnWidth(2, 70)

        return self.lblID.text()

    def foodNameList(self) -> list:
        return Food.foodNameList()

    def showMsg(self, massage, title):
        msg = QMessageBox()
        msg.setText(massage)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('Files//msg.png'))
        msg.exec()

    def chargeBalance(self):
        value, ok = QInputDialog.getInt(
            self, 'افزایش موجودی', 'مقداری که میخواهید شارژ کنید وارد نمایید:(به تومان)')
        if ok:
            if 10000000 > value > 0:
                User.chargeBalance(value, int(self.firstInit()))
                self.lblBalance.setText(
                    str(int(User.getBalance(self.firstInit()))))
                self.showMsg('موجودی شما با موفقیت افزایش یافت',
                             'عملیات موفقیت آمیز')
            else:
                self.showMsg('لطفا مقدار معتبری وارد کیند!', 'خطا')
                self.chargeBalance()

    def reserveFood(self):
        foodNameList = self.foodNameList()
        if len(foodNameList) == 0:
            self.showMsg("متاسفیم فعلا غذایی برای رزرو وجود ندارد", "خطا")
            return
        option, ok = QInputDialog.getItem(
            self, 'رزرو غذا', 'غذای مورد نظر را انتخاب کنید:', foodNameList, editable=False)
        if ok:
            foodName = option.split(' قیمت ')[0]
            selectFoodState = User.userFoodReserve(
                int(self.firstInit()), foodName)
            if selectFoodState == 'food reserve':
                self.showMsg('شما این غذا را رزرو کرده اید!', 'خطا')
                self.reserveFood()
            elif selectFoodState == 'BalanceNotEnough':
                self.showMsg(
                    'شما موجودی کافی برای رزرو این غذا ندارید!', 'خطا')
            else:
                self.lblBalance.setText(str(User.getBalance(self.firstInit())))
                self.lblFoodReserve.setText(
                    User.getFoodReserve_by_ID(self.firstInit()))
                self.showMsg('غذا با موفقیت رزرو شد', 'عملیات موفقیت آمیز')
