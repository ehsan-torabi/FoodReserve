from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QInputDialog, QMessageBox
from Modules.FoodModule import Food
from Modules.UserModule import User
from pandas import DataFrame
import Modules.pdModel as pdm


class Ui_AdminForm(object):
    def setupUi(self, AdminForm):
        AdminForm.setObjectName("AdminForm")
        AdminForm.resize(551, 426)
        AdminForm.setMinimumSize(QtCore.QSize(551, 426))
        AdminForm.setMaximumSize(QtCore.QSize(551, 426))
        font = QtGui.QFont()
        font.setFamily("IRANSans(FaNum)")
        AdminForm.setFont(font)
        AdminForm.setWindowIcon(QtGui.QIcon('Files//admin.png'))
        AdminForm.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        AdminForm.setLocale(QtCore.QLocale(
            QtCore.QLocale.Language.Persian, QtCore.QLocale.Country.Iran))
        self.tabWidget = QtWidgets.QTabWidget(AdminForm)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 561, 431))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setGeometry(QtCore.QRect(300, 120, 91, 20))
        self.label.setObjectName("label")
        self.lblFoodCount = QtWidgets.QLabel(self.mainTab)
        self.lblFoodCount.setGeometry(QtCore.QRect(370, 170, 171, 20))
        self.lblFoodCount.setObjectName("lblFoodCount")
        self.label_3 = QtWidgets.QLabel(self.mainTab)
        self.label_3.setGeometry(QtCore.QRect(270, 50, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.mainTab)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblUserCount = QtWidgets.QLabel(self.mainTab)
        self.lblUserCount.setGeometry(QtCore.QRect(330, 200, 211, 20))
        self.lblUserCount.setObjectName("lblUserCount")
        self.reservVeiw = QtWidgets.QTableView(self.mainTab)
        self.reservVeiw.setGeometry(QtCore.QRect(20, 110, 281, 271))
        self.reservVeiw.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.reservVeiw.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.reservVeiw.setObjectName("reservVeiw")
        self.tabWidget.addTab(self.mainTab, "")
        self.foodTab = QtWidgets.QWidget()
        self.foodTab.setObjectName("foodTab")
        self.btnFoodDelete = QtWidgets.QPushButton(self.foodTab)
        self.btnFoodDelete.setGeometry(QtCore.QRect(230, 70, 131, 31))
        self.btnFoodDelete.setObjectName("btnFoodDelete")
        self.btnFoodAdd = QtWidgets.QPushButton(self.foodTab)
        self.btnFoodAdd.setGeometry(QtCore.QRect(380, 70, 131, 31))
        self.btnFoodAdd.setObjectName("btnFoodAdd")
        self.txtSearchFood = QtWidgets.QLineEdit(self.foodTab)
        self.txtSearchFood.setGeometry(QtCore.QRect(272, 20, 201, 24))
        self.txtSearchFood.setText("")
        self.txtSearchFood.setObjectName("txtSearchFood")
        self.label_4 = QtWidgets.QLabel(self.foodTab)
        self.label_4.setGeometry(QtCore.QRect(480, 20, 49, 21))
        self.label_4.setObjectName("label_4")
        self.btnSearchFood = QtWidgets.QPushButton(self.foodTab)
        self.btnSearchFood.setGeometry(QtCore.QRect(209, 20, 51, 24))
        self.btnSearchFood.setObjectName("btnSearchFood")
        self.FoodVeiw = QtWidgets.QTableView(self.foodTab)
        self.FoodVeiw.setGeometry(QtCore.QRect(20, 120, 521, 261))
        self.FoodVeiw.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.FoodVeiw.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.FoodVeiw.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.FoodVeiw.setObjectName("FoodVeiw")
        self.tabWidget.addTab(self.foodTab, "")
        self.studentTab = QtWidgets.QWidget()
        self.studentTab.setObjectName("studentTab")
        self.label_5 = QtWidgets.QLabel(self.studentTab)
        self.label_5.setGeometry(QtCore.QRect(480, 20, 49, 21))
        self.label_5.setObjectName("label_5")
        self.txtSearchUser = QtWidgets.QLineEdit(self.studentTab)
        self.txtSearchUser.setGeometry(QtCore.QRect(272, 20, 201, 24))
        self.txtSearchUser.setText("")
        self.txtSearchUser.setObjectName("txtSearchUser")
        self.btnUserDelete = QtWidgets.QPushButton(self.studentTab)
        self.btnUserDelete.setGeometry(QtCore.QRect(380, 70, 131, 31))
        self.btnUserDelete.setObjectName("btnUserDelete")
        self.btnFoodSearch = QtWidgets.QPushButton(self.studentTab)
        self.btnFoodSearch.setGeometry(QtCore.QRect(209, 20, 51, 24))
        self.btnFoodSearch.setObjectName("btnFoodSearch")
        self.UserTableVeiw = QtWidgets.QTableView(self.studentTab)
        self.UserTableVeiw.setGeometry(QtCore.QRect(20, 120, 521, 261))
        self.UserTableVeiw.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.UserTableVeiw.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.UserTableVeiw.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.UserTableVeiw.setObjectName("UserTableVeiw")
        self.tabWidget.addTab(self.studentTab, "")

        self.retranslateUi(AdminForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminForm)

    def retranslateUi(self, AdminForm):
        _translate = QtCore.QCoreApplication.translate
        AdminForm.setWindowTitle(_translate(
            "AdminForm", "سیستم رزرو غذا-پنل ادمین"))
        AdminForm.setWindowIcon(QtGui.QIcon('Files//admin.png'))
        self.label.setText(_translate("AdminForm", "غذا های رزرو شده:"))
        self.lblFoodCount.setText(_translate(
            "AdminForm", "در حال حاظر 0  غذا موجود  است."))
        self.label_3.setText(_translate("AdminForm", "سیستم رزرو غذا"))
        self.label_2.setText(_translate(
            "AdminForm", "به پنل مدیریت خوش آمدید"))
        self.lblUserCount.setText(_translate(
            "AdminForm", "در حال حاظر 0  دانشجو ثبت نام کرده است."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.mainTab), _translate("AdminForm", "اصلی"))
        self.btnFoodDelete.setText(_translate("AdminForm", "حذف غذا"))
        self.btnFoodAdd.setText(_translate("AdminForm", "افزودن غذا"))
        self.txtSearchFood.setPlaceholderText(
            _translate("AdminForm", "نام غذا"))
        self.label_4.setText(_translate("AdminForm", "جستجو:"))
        self.btnSearchFood.setText(_translate("AdminForm", "جستجو"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.foodTab), _translate("AdminForm", "مدیریت غذا"))
        self.label_5.setText(_translate("AdminForm", "جستجو:"))
        self.txtSearchUser.setPlaceholderText(_translate("AdminForm", "کدملی"))
        self.btnUserDelete.setText(_translate("AdminForm", "حذف دانشجو"))
        self.btnFoodSearch.setText(_translate("AdminForm", "جستجو"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.studentTab), _translate("AdminForm", "مدیریت دانشجوها"))
        self.firstInit()
        self.btnFoodAdd.clicked.connect(self.addFood)
        self.btnFoodSearch.clicked.connect(self.searchUser)
        self.btnSearchFood.clicked.connect(self.searchFood)
        self.btnUserDelete.clicked.connect(self.deleteUser)
        self.btnFoodDelete.clicked.connect(self.deleteFood)


################ myFunc##########################################


    def showMsg(self, massage, title):
        msg = QMessageBox()
        msg.setText(massage)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('Files//msg.png'))
        msg.exec()

    def showMsg2(self, massage, title):
        msg = QMessageBox()
        msg.setText(massage)
        msg.setWindowTitle(title)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setWindowIcon(QtGui.QIcon('Files//msg.png'))
        selectedBtn = msg.exec()
        return selectedBtn

    def firstInit(self):
        foodModel = pdm.pandasModel(Food.listFaHeader())
        self.FoodVeiw.setModel(foodModel)
        self.FoodVeiw.setColumnWidth(0, 150)
        self.FoodVeiw.setColumnWidth(1, 150)
        self.FoodVeiw.setColumnWidth(2, 150)
        userModel = pdm.pandasModel(User.getUsersFaHeader())
        self.UserTableVeiw.setModel(userModel)
        self.UserTableVeiw.setColumnWidth(2, 100)
        foodReserveModel = pdm.pandasModel(User.getUsersFoodReserve())
        self.reservVeiw.setModel(foodReserveModel)
        self.reservVeiw.setColumnWidth(0, 100)
        self.reservVeiw.setColumnWidth(1, 70)
        self.lblFoodCount.setText(
            f'درحال حاضر {len(Food.foodList())} غذا موجود است')
        self.lblUserCount.setText(
            f'در حال حاضر {len(User.getUsersList())} دانشجو ثبت نام کرده است.')

    def addFood(self):
        Name, foodNameSelect = QInputDialog.getText(
            self, "افزودن غذا", "نام غذا را وارد کنید:")
        if foodNameSelect:
            if Name != '':
                Price, priceSelect = QInputDialog.getText(
                    self, "افزودن غذا", f"قیمت {Name} را وارد کنید:")
                if priceSelect:
                    if Price == '':
                        self.showMsg("لطفا قیمت وارد کنید", "خطا")
                    else:
                        Food.addFood(Name, Price)
                        self.showMsg("غذا با موفقیت افزوده شد.", "عملیات موفق")
                        self.firstInit()

            else:
                self.showMsg("لطفا یک نام وارد کنید", "خطا")
                self.addFood()

    def searchUser(self):
        if self.txtSearchUser.text() != '':
            result_data = User.getInfo_by_ID(int(self.txtSearchUser.text()))
            final_result_dataFrame = DataFrame({"نام": result_data['Name'], "نام خانوادگی": result_data['Family'],
                                                'کدملی': result_data['ID'], 'رمز ورود': result_data['Password'], 'موجودی': result_data['Balance']})
            userModel = pdm.pandasModel(final_result_dataFrame)
            self.UserTableVeiw.setModel(userModel)
        else:
            self.firstInit()

    def searchFood(self):
        if self.txtSearchFood.text() != '':
            FoodModel = pdm.pandasModel(
                Food.foodData(self.txtSearchFood.text()))
            self.FoodVeiw.setModel(FoodModel)
        else:
            self.firstInit()

    def selected(self, Qtable):
        # this func return selected item ID(UserID or FoodID)
        if Qtable.selectedIndexes() != []:
            indexes = Qtable.selectionModel().selectedRows()
            for index in sorted(indexes):
                return (index.data())
        else:
            return 'None'

    def deleteFood(self):
        if self.selected(self.FoodVeiw) != 'None':
            msg = self.showMsg2('آیا از این کار مطمئنید؟', 'اخطار')
            if msg == QMessageBox.StandardButton.Yes:
                Food.removeFood(self.selected(self.FoodVeiw))
                self.firstInit()
                self.showMsg("غذا با موفقیت حذف شد", "عملیات موفق")

    def deleteUser(self):
        if self.selected(self.UserTableVeiw) != 'None':
            msg = self.showMsg2('آیا از این کار مطمئنید؟', 'اخطار')
            if msg == QMessageBox.StandardButton.Yes:
                name = self.selected(self.UserTableVeiw)
                User.remove(User.getID_by_Name(name))
                self.firstInit()
                self.showMsg("دانشجو با موفقیت حذف شد", "عملیات موفق")
        else:
            self.showMsg("لطفا یکی از دانشجو ها را انتخاب کنید", "خطا")
