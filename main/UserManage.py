from PySide2.QtCore import QFile, Qt, Slot
from PySide2.QtWidgets import (QFileDialog, QHeaderView, QMainWindow,
                               QMessageBox, QTableWidgetItem)
from ui.generate.Ui_UserManage import Ui_UserManage
from utility.DataManager import DataManager
from utility.ExcelManager import ExcelManager


class UserManage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_UserManage()
        self.ui.setupUi(self)
        self.ui.userTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.loadInfo()

    def loadInfo(self):
        # Get userInfo list, each unit is tuple.
        db = DataManager()
        self.userInfoDict = db.getAllUserInfoDict()
        db.closeConnect()

        # setup the table
        self.ui.userTableWidget.setRowCount(len(self.userInfoDict))

        row = 0
        for userAccount, userInfo in self.userInfoDict.items():
            self.ui.userTableWidget.setItem(row, 0,
                                            QTableWidgetItem(str(userAccount)))
            self.ui.userTableWidget.setItem(row, 1,
                                            QTableWidgetItem(str(userInfo[0])))
            if userInfo[1] == 1:
                self.ui.userTableWidget.setItem(row, 2, QTableWidgetItem("管理"))
            else:
                self.ui.userTableWidget.setItem(row, 2, QTableWidgetItem("学生"))
            row += 1

        self.ui.userTableWidget.clearSelection()

    @Slot()
    def on_btnDelete_clicked(self):
        items = self.ui.userTableWidget.selectedItems()
        deleteUserIds = list()
        # the number of item is multiple of 3
        # in this loop, we can get 1nd item in each 3 items.
        # which contain text of user account
        for i in range(0, len(items), 3):
            # get account of whom was chosen to be deleted
            account = items[i].text()
            userId = self.userInfoDict.pop(account)[2]
            deleteUserIds.append((userId, ))  # the element is a tuple

        db = DataManager()
        db.deleteUserByIdList(deleteUserIds)
        db.closeConnect()
        self.loadInfo()

    @Slot()
    def on_btnNew_clicked(self):
        account = self.ui.accEdit.text()
        name = self.ui.nameEdit.text()
        isAdmin = int(self.ui.isAdminButtom.isChecked())

        if (not account.isalnum()) or (len(account) > 20):
            QMessageBox().warning(self, "CEESS-提醒", "账号只能由数字和字母组成，长度小于20位。")
        elif len(name) > 20:
            QMessageBox().warning(self, "CEESS-提醒", "姓名长度只能小于20位。")
        elif account in self.userInfoDict:
            QMessageBox().warning(self, "CEESS-提醒",
                                  "已存在该账号：\"" + account + "\"")
        else:
            db = DataManager()
            db.addNewUserByList([(account, name, isAdmin)])
            db.closeConnect()
            self.loadInfo()

    @Slot()
    def on_btnImport_clicked(self):
        # get file path from explore.
        file = QFileDialog.getOpenFileName(self, "上传文件", "./",
                                           "Excel Files (*.xls)")
        filePath = file[0]

        # get user data list.
        if len(filePath) != 0:
            excel = ExcelManager(filePath)
            userData = excel.getUserList()

            # error handling.
            errorString = "#######错误提示#######\n"
            errorCount = 0

            # import user data.
            userInfoList = list()
            newUserName = set()
            # the newUserNameSet are design to check whether there is any
            #  duplicate userName in excel file.
            for i in range(len(userData)):
                # setup data.
                name = str(userData[i][0])
                account = str(userData[i][1])

                if userData[i][2] == "学生":
                    isAdmin = 0
                else:
                    isAdmin = 1
                # check format and duplication

                if (not account.isalnum()) or (len(account) > 20):
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 3) +
                                    "行，账号只能由数字和字母组成，长度小于20位。\n")
                elif len(name) > 20:
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 3) +
                                    "行，姓名长度只能小于20位。\n")
                elif ((account in self.userInfoDict)
                      or (account in newUserName)):
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 3) +
                                    "行，已存在此账号：\"" + account + "\"\n")
                else:
                    userInfoList.append((account, name, isAdmin))
                    newUserName.add(account)

            # error handling.
            if errorCount == 0:
                db = DataManager()
                db.addNewUserByList(userInfoList)
                db.closeConnect()
                self.loadInfo()
                QMessageBox().information(self, "CEESS-导入信息", "导入成功！")
            else:
                errorString += "请更正上述错误再尝试导入。\n"
                QMessageBox().warning(self, "CEESS-导入信息", errorString)

    @Slot()
    def on_btnDownload_clicked(self):
        file = QFile("./resources/download/userImportTemplate")
        if file.open(QFile.ReadOnly):
            filePath = QFileDialog.getSaveFileName(self, "CEESS-模板下载",
                                                   "用户导入模板.xls",
                                                   "Excel Files (*.xls)")
            if len(filePath[0]) != 0:
                file.copy(filePath[0])
        else:
            QMessageBox.warning(self, "CEESS-通知", "模板文件丢失，请重装本系统或联系管理员！")

    @Slot()
    def on_accEdit_returnPressed(self):
        self.ui.nameEdit.setFocus()

    @Slot()
    def on_nameEdit_returnPressed(self):
        self.on_btnNew_clicked()
