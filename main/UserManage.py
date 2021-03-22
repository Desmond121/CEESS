from PySide2.QtCore import QFile, Slot
from PySide2.QtWidgets import (QFileDialog, QHeaderView, QMainWindow,
                               QMessageBox, QTableWidgetItem)
from ui.generate.Ui_UserManage import Ui_UserManage
from utility.DataManager import DataManager
from utility.ExcelManager import ExcelManager


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
        db = DataManager()
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
                self.ui.userTableWidget.setItem(row, 2,
                                                QTableWidgetItem("管理员"))
            else:
                self.ui.userTableWidget.setItem(row, 2, QTableWidgetItem("学生"))

    @Slot()
    def deleteUser(self):
        items = self.ui.userTableWidget.selectedItems()
        db = DataManager()
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
            db = DataManager()
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
        file = QFileDialog.getOpenFileName(self, "上传文件", "./",
                                           "Excel Files (*.xls)")
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
                    db = DataManager()
                    if db.isOccupied(account):
                        errorCount += 1
                        errorString += (str(errorCount) + ".第" + str(i + 3) +
                                        "行，用户名已存在！\n")
                    else:
                        db.addNewUser(account, name, isAdmin)
                        self.loadInfo()
                    db.closeConnect()
                else:
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 3) +
                                    "行，账户或姓名格式错误！\n")

            # error handling.
            if errorCount != 0:
                errorString += "请更正上述错误，其他正确数据已经导入。\n"
                QMessageBox().warning(self, "CEESS-导入信息", errorString)

    @Slot()
    def downloadTemplate(self):
        file = QFile("./resources/template/userImportTemplate.xls")
        if file.open(QFile.ReadOnly):
            filePath = QFileDialog.getSaveFileName(self, "CEESS-模板下载",
                                                   "用户导入模板.xls",
                                                   "Excel Files (*.xls)")
            file.copy(filePath[0])
        else:
            QMessageBox.warning(self, "CEESS-通知", "模板文件丢失，请重新安装本系统！")
