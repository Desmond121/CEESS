"""
@file       : Setting.py
@description: For setting windows.
@date       : 2021/03/22 18:03:32
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
import json
import base64
import os
from PySide2.QtCore import QByteArray, QFile, Qt, Signal, Slot
from PySide2.QtWidgets import QFileDialog, QInputDialog, QLineEdit, QMainWindow, QMessageBox
from ui.generate.Ui_Setting import Ui_Setting
from utility.DataManager import _DATABASE_TYPE, _MYSQL, _SQLITE, DataManager


class Setting(QMainWindow):
    switchDisplaySignal = Signal()
    signOutSignal = Signal()
    userId = None

    def __init__(self, userId, isTeacher, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)

        # get user infomation from database.
        db = DataManager()
        self.ui.userName.setText(db.getNameById(userId))
        self.ui.userAccount.setText(db.getAccountById(userId))
        db.closeConnect()
        # store user id and type
        self.userId = userId

        if isTeacher:
            if _DATABASE_TYPE == _SQLITE:
                self.ui.tabWidget.setTabText(2, "成绩导入")
                self.ui.gradeTabStack.setCurrentIndex(0)
            else:
                self.ui.gradeTab.hide()
        else:
            self.ui.tabWidget.setTabText(2, "成绩查询")
            self.ui.gradeTabStack.setCurrentIndex(1)

            db = DataManager()
            self.gradeInfoList = db.getGradeByUid(userId)
            testTypeDict = db.getTestTypeDict()
            db.closeConnect()

            gradeText = "姓名：" + self.ui.userName.text() + "\n" + "成绩:\n"
            for gradeInfo in self.gradeInfoList:
                testTypeId = gradeInfo[0]
                score = gradeInfo[1]
                gradeText += "--" + testTypeDict.get(testTypeId) + "  " + str(
                    score) + "分\n"
            if len(self.gradeInfoList) < len(testTypeDict):
                gradeText += "还未完成所有内容！请注意！\n"
            self.ui.gradeInfoText.setText(gradeText)

            if _DATABASE_TYPE == _MYSQL:
                self.ui.btnExport.hide()

    # slot for changing theme.
    @Slot()
    def on_switchDisplayMode_clicked(self):
        self.switchDisplaySignal.emit()

    # slot for sign out.
    @Slot()
    def on_btnSignOut_clicked(self):
        self.signOutSignal.emit()

    @Slot()
    def on_btnChangePsw_clicked(self):
        originalPsw = QInputDialog.getText(
            self, "CEESS-修改密码", "请输入原始密码", QLineEdit.Normal, "",
            Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        # getText return a tuple in form of (input_text,is_input_successful)
        if originalPsw[1]:  # input successfully
            db = DataManager()  # database open ----------------
            if db.isPasswordCorrectById(self.userId, originalPsw[0]):
                newPsw = QInputDialog.getText(
                    self, "CEESS-修改密码", "请输入新密码", QLineEdit.Normal, "",
                    Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
                if newPsw[1]:  # new password input successfully.
                    db.changePasswordById(self.userId, newPsw[0])
                    QMessageBox.information(self, "CEESS-通知", "密码修改成功！")
                    self.signOutSignal.emit()
            else:
                QMessageBox.warning(self, "CEESS-提醒", "密码输入错误！")
            db.closeConnect()  # database close ----------------

    @Slot()
    def on_rename_clicked(self):
        newName = QInputDialog.getText(
            self, "CEESS-修改姓名", "请输入姓名", QLineEdit.Normal, "",
            Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        if newName[1]:
            self.ui.userName.setText(newName[0])
            db = DataManager()  # database open ----------------
            db.changeNameById(self.userId, newName[0])
            db.closeConnect()  # database open ----------------
            QMessageBox.information(self, "CEESS-通知", "姓名修改成功！")

    @Slot()
    def on_btnExport_clicked(self):
        gradeInfoDict = dict()
        for gradeInfo in self.gradeInfoList:
            gradeInfoDict.setdefault(gradeInfo[0], gradeInfo[1])
        jsonStr = json.dumps({self.userId: gradeInfoDict})
        encodeStr = self.encode(jsonStr)

        filename = self.ui.userName.text() + ".grade"
        filePath = QFileDialog.getSaveFileName(self, "CEESS-成绩导出", filename)[0]
        if filePath != 0:
            with open(filePath, 'w') as file:
                file.write(encodeStr)
                QMessageBox.information(self, "CEESS-成绩导出", "导出成功！")

    @Slot()
    def on_btnImport_clicked(self):
        importGradesList = list()
        directory = QFileDialog.getExistingDirectory(
            self, "CEESS-上传成绩", "/",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if len(directory) != 0:
            for filename in os.listdir(directory):
                # check surfix .grade
                if os.path.splitext(filename)[1] != ".grade":
                    continue
                fileDir = directory + "/" + filename
                with open(fileDir) as file:
                    encodeStr = file.read()

                decodeStr = self.decode(encodeStr)
                result = json.loads(decodeStr)
                for uid, gradeInfo in result.items():
                    for tid, score in gradeInfo.items():
                        importGradesList.append((int(uid), int(tid), score))

            # upload grades to database
            if len(importGradesList) > 0:
                db = DataManager()
                db.deleteAllGrade()
                db.insertGrade(importGradesList)
                db.closeConnect()
                QMessageBox.information(self, "CEESS-成绩导出", "导入成功！")

    def encode(self, str: str):
        return base64.standard_b64encode(str.encode("utf8")).decode()

    def decode(self, str: str):
        return base64.standard_b64decode(str.encode("utf8")).decode()
