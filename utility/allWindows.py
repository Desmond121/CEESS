"""
@file       : allWindows.py
@description: This file create classes to encapsulate all the QT-uic generated
              files with "Ui_" prefix.
@date       : 2021/02/10 17:22:10
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""


from PySide2 import QtWidgets
from PySide2.QtCore import QFile, Qt, Signal, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QFileDialog, QHeaderView, QMainWindow,
                               QMessageBox, QTableWidgetItem)
from ui.Ui_Login import Ui_Login
from ui.Ui_Setting import Ui_Setting
from ui.Ui_Student import Ui_Student
from ui.Ui_Teacher import Ui_Teacher
from ui.Ui_test import Ui_Test
from ui.Ui_TestManage import Ui_TestManage
from ui.Ui_UserManage import Ui_UserManage

from utility.dataManager import DBManager
from utility.excelManager import ExcelManager

_IMG_PATH = "./resources/img/"
_NAVIGATOR_STYLESHEET = "./resources/qss/navigator.qss"


class Login(QMainWindow):
    # signal
    loginType = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

    @ Slot()
    def on_loginButtom_clicked(self):
        password = self.ui.pswLineEdit.text()
        userId = self.ui.accLineEdit.text()

        data = DBManager("./data/db.sqlite3")
        if data.isPasswordCorrect(userId, password):
            isTeacher = bool(data.getTypeByAccount(userId))
            self.loginType.emit(isTeacher)
        else:
            QMessageBox.information(self, "CEESS-提示", "用户名或密码错误!")
        data.closeConnect()


class Navigator(QMainWindow):
    def __init__(self, isTeacher=False):
        super().__init__()
        if isTeacher:
            self.setupTeacher()
        else:
            self.setupStudent()
        # Set icon style
        with open(_NAVIGATOR_STYLESHEET) as stylesheet:
            self.setStyleSheet(stylesheet.read())

    def setupTeacher(self):
        self.ui = Ui_Teacher()
        self.ui.setupUi(self)

        # Add icon for buttons
        self.ui.btnUserManage.setIcon(QIcon(_IMG_PATH + "btnUserManage"))
        self.ui.btnScoreAnalyse.setIcon(QIcon(_IMG_PATH + "btnScoreAnalyse"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting"))
        self.ui.btnTestManage.setIcon(QIcon(_IMG_PATH + "btnTestManage"))

        # Connect buttons with slot
        self.ui.btnUserManage.clicked.connect(self.openUserManage)
        self.ui.btnTestManage.clicked.connect(self.openTestManage)

    def setupStudent(self):
        self.ui = Ui_Student()
        self.ui.setupUi(self)

        # Add icon for buttons
        self.ui.btnDataProcess.setIcon(QIcon(_IMG_PATH + "btnDataProcess.svg"))
        self.ui.btnExpTest.setIcon(QIcon(_IMG_PATH + "btnExpTest.svg"))
        self.ui.btnPreparing.setIcon(QIcon(_IMG_PATH + "btnPrepare.svg"))
        self.ui.btnSafetyTest.setIcon(QIcon(_IMG_PATH + "btnSafetyTest.svg"))
        self.ui.btnSetting.setIcon(QIcon(_IMG_PATH + "btnSetting.svg"))
        self.ui.btnSimulator.setIcon(QIcon(_IMG_PATH + "btnSimulator.svg"))

        # Connect buttons with slot
        self.ui.btnExpTest.clicked.connect(self.openExpTest)
        self.ui.btnSetting.clicked.connect(self.openSetting)

    @ Slot()
    def openExpTest(self):
        # ! frameless
        # self.Test = FramelessWindow(Test(), True, self)
        self.Test = Test(self)
        self.Test.show()

    @ Slot()
    def openSetting(self):
        # ! frameless
        # self.setting = FramelessWindow(Setting(), True, self)
        self.setting = Setting(self)
        self.setting.show()

    @ Slot()
    def openUserManage(self):
        self.userManage = UserManage(self)
        self.userManage.show()

    @ Slot()
    def openTestManage(self):
        self.testManage = TestManage(self)
        self.testManage.show()


class Test(QMainWindow):
    def __init__(self, testType=0, parent=None):
        """__init__

        Keyword Arguments:
            testType {int} -- (default: {0})
            {0} means safety test
            {1} means experiment test
        """
        super().__init__(parent)
        self.ui = Ui_Test()
        self.ui.setupUi(self)


class Setting(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        self.ui.pushButton.setStyleSheet("border-color : red")


class UserManage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UserManage()
        self.ui.setupUi(self)
        self.loadInfo()

        # connect signal slot.
        self.ui.btnDelete.clicked.connect(self.deleteUser)
        self.ui.btnNew.clicked.connect(self.addNewUser)
        self.ui.btnImport.clicked.connect(self.importUser)
        self.ui.btnDownload.clicked.connect(self.downloadTemplate)

    def loadInfo(self):
        # Get userInfo list, each unit is tuple.
        db = DBManager()
        userInfo = db.getAllUserInfo()
        db.closeConnect()

        # setup the table
        self.ui.userTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.ui.userTableWidget.setRowCount(len(userInfo))
        for row in range(len(userInfo)):
            self.ui.userTableWidget.setItem(
                row, 0, QTableWidgetItem(str(userInfo[row][0])))
            self.ui.userTableWidget.setItem(
                row, 1, QTableWidgetItem(str(userInfo[row][1])))
            if userInfo[row][2] == 1:
                self.ui.userTableWidget.setItem(
                    row, 2, QTableWidgetItem("管理员"))
            else:
                self.ui.userTableWidget.setItem(
                    row, 2, QTableWidgetItem("学生"))

    @Slot()
    def deleteUser(self):
        items = self.ui.userTableWidget.selectedItems()
        db = DBManager()
        # the number of item is multiple of 3
        # in this loop, we can get 2nd item in each 3 items.
        # which contain texts of user account
        for i in range(1, len(items), 3):
            db.deleteUserByAccount(str(items[i].text()))
        db.closeConnect()
        self.loadInfo()

    @Slot()
    def addNewUser(self):
        account = self.ui.accEdit.text()
        name = self.ui.nameEdit.text()
        isAdmin = int(self.ui.isAdminButtom.isChecked())
        if (account.isalnum() and len(account) <= 20 and 0 < len(name) <= 20):
            db = DBManager()
            if db.isOccupied(account):
                QMessageBox().warning(self, "CEESS-提醒", "账号已存在！")
            else:
                db.addNewUser(account, name, isAdmin)
                self.ui.accEdit.setText("")
                self.ui.nameEdit.setText("")
                self.loadInfo()
            db.closeConnect()
        else:
            QMessageBox().warning(self, "CEESS-提醒", "请检查账号和姓名格式！")

    @Slot()
    def importUser(self):
        # get file path from explore.
        file = QFileDialog.getOpenFileName(
            self, "上传文件", "./", "Excel Files (*.xls)")
        filePath = file[0]

        # get user data list.
        if len(filePath) != 0:
            excel = ExcelManager(filePath)
            userData = excel.getUserData()

            # error handling.
            errorString = "#######错误提示#######\n"
            errorCount = 0

            # import user data.
            for i in range(len(userData)):
                # setup data.
                name = userData[i][0]
                account = userData[i][1]
                if userData[i][2] == "学生":
                    isAdmin = 0
                else:
                    isAdmin = 1
                # import to table.
                if (account.isalnum() and len(account) <= 20
                        and 0 < len(name) <= 20):
                    db = DBManager()
                    if db.isOccupied(account):
                        errorCount += 1
                        errorString += (str(errorCount) + ".第" +
                                        str(i+3) + "行，用户名已存在！\n")
                    else:
                        db.addNewUser(account, name, isAdmin)
                        self.loadInfo()
                    db.closeConnect()
                else:
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" +
                                    str(i+3) + "行，账户或姓名格式错误！\n")

            # error handling.
            if errorCount != 0:
                errorString += "请更正上述错误，其他正确数据已经导入。\n"
                QMessageBox().warning(self, "CEESS-导入信息", errorString)

    @Slot()
    def downloadTemplate(self):
        file = QFile("./resources/template/userImportTemplate.xls")
        if file.open(QFile.ReadOnly):
            filePath = QFileDialog.getSaveFileName(
                self, "CEESS-模板下载", "用户导入模板.xls", "Excel Files (*.xls)")
            file.copy(filePath[0])
        else:
            QMessageBox.warning(self, "CEESS-通知", "模板文件丢失，请重新安装本系统！")


class TestManage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TestManage()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem("这是第一题，测试测试测试测试测试...")
        self.ui.listWidget.addItem("这是第二题测试测试测试测试测试测...")
        self.ui.textBrowser.setTextBackgroundColor(Qt.white)


# class Simulator(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.web =
