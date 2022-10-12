"""
@file       : TestManage.py
@description: A window for test questions managing.
@date       : 2021/03/22 18:34:15
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

from PySide2.QtCore import QFile, Qt, Slot
from PySide2.QtWidgets import (QFileDialog, QListWidget, QMainWindow,
                               QMessageBox)
from ui.generate.Ui_TestManage import Ui_TestManage
from utility.DataManager import DataManager
from utility.ExcelManager import ExcelManager

_CHOICE_TYPE = 0
_TRUE_FALSE_TYPE = 1


class TestManage(QMainWindow):
    choiceBank = None  # question bank for single choice question.
    trueFalseBank = None  # question bank for TF question.

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_TestManage()
        self.ui.setupUi(self)

        self.loadQuestion()

    def loadQuestion(self):
        # load all questions from database
        db = DataManager()
        # load single choice questions first.
        self.choiceBank = db.getAllQuestion(_CHOICE_TYPE)
        choiceSize = len(self.choiceBank)
        for i in range(choiceSize):
            # bank[i][1] is the number i question's body.
            self.ui.choiceList.addItem(self.choiceBank[i][1])

        # then load all TF question.
        self.trueFalseBank = db.getAllQuestion(_TRUE_FALSE_TYPE)
        trueFalseSize = len(self.trueFalseBank)
        for i in range(trueFalseSize):
            # bank[i][1] is the number i question's body.
            self.ui.trueFalseList.addItem(self.trueFalseBank[i][1])
        db.closeConnect()
        # display the number of questions
        self.ui.choiceLCD.display(choiceSize)
        self.ui.trueFalseLCD.display(trueFalseSize)

    def deleteSelectedQuestion(self, questionList: QListWidget,
                               questionBank: list):
        # selected = questionList.selectedIndexes()
        # idList = list()
        # for item in selected:
        #     idList.append(questionBank[item.row()][0])
        # db = DataManager()
        # db.deleteQuestionById(idList)
        # db.closeConnect()

        # self.loadQuestion()
        selected = questionList.selectedIndexes()
        deleteIdList = list()
        removeCount = 0  # counting how many items have been removed.

        for item in selected:
            # if one of the item is removed, index of item which is behind
            # will be smaller by 1
            row = item.row()
            questionList.takeItem(row - removeCount)
            deletedItem = questionBank.pop(row - removeCount)
            # a list of tuple contain only one element
            deleteIdList.append((deletedItem[0], ))
            removeCount += 1
        db = DataManager()  # connect to database
        db.deleteQuestionById(deleteIdList)
        db.closeConnect()  # disconnect to database

    def deleteAllQuestion(self):
        # delete questions in database
        db = DataManager()
        db.deleteAllQuestion()
        db.closeConnect()
        # delete questions in bank
        self.choiceBank.clear()
        self.trueFalseBank.clear()
        # delete questions in list
        self.ui.trueFalseList.clear()
        self.ui.choiceList.clear()

    def importQuestionsFromExcel(self, isOverride: bool):
        file = QFileDialog().getOpenFileName(self, "上传文件", "./",
                                             "Excel Files (*.xls)")
        filePath = file[0]
        if len(filePath) != 0:
            if isOverride:
                self.deleteAllQuestion()
            excel = ExcelManager(filePath)
            # get import quesion list
            questionList = excel.getQuestionList()

            # checked import type.
            checkedQuestionList = list()
            error = self.mistakeFilter(questionList, checkedQuestionList)

            # upload to database
            db = DataManager()
            db.addQuestionFromList(checkedQuestionList)
            db.closeConnect()

            # reload bank and list
            self.loadQuestion()

            if error[0] != 0:
                QMessageBox.warning(self, "CEESS-提醒", error[1])

    def mistakeFilter(self, oldQuestionList: list, newQuestionList: list):
        # error handling.
        errorString = "#######错误提示#######\n"
        errorCount = 0

        # import check.
        for i in range(len(oldQuestionList)):
            body = oldQuestionList[i][0]
            choiceA = oldQuestionList[i][1]
            choiceB = oldQuestionList[i][2]
            choiceC = oldQuestionList[i][3]
            choiceD = oldQuestionList[i][4]
            type = oldQuestionList[i][5]
            answer = oldQuestionList[i][6]
            if type == 0:  # single choice.
                if (len(body) * len(choiceA) * len(choiceB) * len(choiceC) *
                        len(choiceD)) == 0:
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 2) +
                                    "行，题干或选项ABCD不能为空！\n")
                elif answer not in (1, 2, 3, 4):
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 2) +
                                    "行，导入选择题答案只能是1、2、3或4！\n")
                else:
                    newQuestionList.append(oldQuestionList[i])
            elif type == 1:
                if len(body) == 0:
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 2) +
                                    "行，题干不能为空！\n")
                elif answer not in (1, 2):
                    errorCount += 1
                    errorString += (str(errorCount) + ".第" + str(i + 2) +
                                    "行，导入选择题答案只能是1或者2！\n")
                else:
                    newQuestionList.append(oldQuestionList[i])
            else:
                errorCount += 1
                errorString += (str(errorCount) + ".第" + str(i + 2) +
                                "行，题目类型只能为0或1，分别为选择或判断！\n")

        errorString += "其他无错误内容已成功导入。"
        return (errorCount, errorString)

    @Slot()
    def on_choiceList_itemClicked(self):
        index = self.ui.choiceList.currentRow()  # question index.
        body = self.choiceBank[index][1] + "\n\n"  # question body.{text}
        answerCode = self.choiceBank[index][7]  # question answer.{1,2,3,4}
        optionA = "A." + self.choiceBank[index][2] + "\n"
        optionB = "B." + self.choiceBank[index][3] + "\n"
        optionC = "C." + self.choiceBank[index][4] + "\n"
        optionD = "D." + self.choiceBank[index][5] + "\n"
        if answerCode == 1:
            answerString = "答案： " + "A"
        elif answerCode == 2:
            answerString = "答案： " + "B"
        elif answerCode == 3:
            answerString = "答案： " + "C"
        else:  # answerCode == 4:
            answerString = "答案： " + "D"
        result = body + optionA + optionB + optionC + optionD \
            + "\n\n" + answerString
        self.ui.textBrowser.setText(result)

    @Slot()
    def on_trueFalseList_itemClicked(self):
        index = self.ui.trueFalseList.currentRow()  # question index.
        body = self.trueFalseBank[index][1] + "\n\n"  # question body.{text}
        answerCode = self.trueFalseBank[index][7]  # question answer.{1,2}
        answerString = "答案： " + ("正确" if answerCode == 1 else "错误")
        result = body + "\n\n" + answerString
        self.ui.textBrowser.setText(result)

    @Slot()
    def on_btnDeletetrueFalse_clicked(self):
        self.deleteSelectedQuestion(self.ui.trueFalseList, self.trueFalseBank)
        self.ui.trueFalseLCD.display(len(self.trueFalseBank))

    @Slot()
    def on_btnDeleteChoice_clicked(self):
        self.deleteSelectedQuestion(self.ui.choiceList, self.choiceBank)
        self.ui.choiceLCD.display(len(self.choiceBank))

    @Slot()
    def on_btnDownload_clicked(self):
        file = QFile("./resources/download/testImportTemplate")
        if file.open(QFile.ReadOnly):
            filePath = QFileDialog.getSaveFileName(self, "CEESS-模板下载",
                                                   "题库导入模板.xls",
                                                   "Excel Files (*.xls)")
            if len(filePath[0]) != 0:
                file.copy(filePath[0])
        else:
            QMessageBox.warning(self, "CEESS-通知", "模板文件丢失，请检查软件的完整性或重新安装本系统！")

    @Slot()
    def on_btnImport_clicked(self):
        isOverride = True if self.ui.btnIsOverride.isChecked() else False
        if isOverride:
            result = QMessageBox().warning(self, "CEESS-警告",
                                           "全量导入将会覆盖所有原有的题目，继续吗？",
                                           QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                self.importQuestionsFromExcel(isOverride)
        else:
            self.importQuestionsFromExcel(isOverride)
