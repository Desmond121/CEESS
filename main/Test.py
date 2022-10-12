"""
@file       : Test.py
@description: For testing module.
@date       : 2021/03/22 18:23:26
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""

import time

from PySide2.QtCore import QTimer, Slot
from PySide2.QtGui import QCloseEvent, QColor, QIcon, Qt
from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.generate.Ui_test import Ui_Test
from utility.DataManager import DataManager

_IMG_PATH = "./resources/img/"
_CHOICE_TYPE = 0
_TRUE_FALSE_TYPE = 1
_CHOICE_AMOUNT = 2  # default amount of single choice questions.
_TRUE_FALSE_AMOUNT = 2  # default amount of true or false questions.
_TEST_TIME = 1800  # seconds of default testing time
_TEST_TYPE_ID = 1
# in datasheet TEST_TYPE, 1 means "安全测试" which is this module


class Test(QMainWindow):
    def __init__(self, UID, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Test()
        self.ui.setupUi(self)

        # save and diplay user info
        self.userId = UID
        db = DataManager()
        self.userName = db.getNameById(UID)
        db.closeConnect()
        self.ui.lblNameStart.setText("姓名： " + self.userName)

        # setup question bank
        self.questionBank = None  # question bank for single choice question.
        self.qIndex = 0  # the index of current question.

        # setup icons.
        self.ui.btnTrue.setIcon(QIcon(_IMG_PATH + "btnTrue.svg"))
        self.ui.btnFalse.setIcon(QIcon(_IMG_PATH + "btnFalse.svg"))
        self.ui.btnStart.setIcon(QIcon(_IMG_PATH + "start.svg"))
        self.ui.btnSubmit.setIcon(QIcon(_IMG_PATH + "submit.svg"))

        # display start page.
        self.ui.pages.setCurrentIndex(0)

    def questionDisplay(self, question: tuple):
        questionNum = str(self.qIndex + 1) + "."
        body = question[1] + "\n\n"
        if question[6] == _CHOICE_TYPE:
            optionA = "A." + question[2] + "\n"
            optionB = "B." + question[3] + "\n"
            optionC = "C." + question[4] + "\n"
            optionD = "D." + question[5] + "\n"
            result = questionNum + body + optionA + optionB + optionC + optionD
        else:
            questionNum = str(self.qIndex + 1) + "."
            result = questionNum + body
        self.ui.questionBrowser.setText(result)

    def finishingCheck(self):
        unfinished = []
        for i in range(len(self.questionBank)):
            item = self.ui.questionTable.item(i, 0)
            if (item.text() == ""):
                unfinished.append(i + 1)  # append unfinished question number.
        return unfinished

    def answerCheck(self):
        choiceMistake = 0
        trueFalseMistake = 0

        # answer mapping.
        choiceMap = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        trueFalseMap = {'T': 1, 'F': 2}

        # calculate wrong answer.
        for i in range(_CHOICE_AMOUNT):
            answer = choiceMap.get(self.ui.questionTable.item(i, 0).text())
            if answer != self.questionBank[i][7]:
                choiceMistake += 1
        for i in range(_CHOICE_AMOUNT, _CHOICE_AMOUNT + _TRUE_FALSE_AMOUNT):
            answer = trueFalseMap.get(self.ui.questionTable.item(i, 0).text())
            if answer != self.questionBank[i][7]:
                trueFalseMistake += 1

        # grading
        mistakeRate = (choiceMistake / _CHOICE_AMOUNT) * 0.6 + (
            trueFalseMistake / _TRUE_FALSE_AMOUNT) * 0.4
        score = (1 - mistakeRate) * 100
        return score

    def uploadGrade(self):
        grade = float(self.ui.lblGrade.text())
        db = DataManager()
        # if existing, = EXISTING_SCORE, else = -1
        exist = db.gradeDuplicateCheck(self.userId, _TEST_TYPE_ID)

        if exist == -1:
            db.insertGrade([(self.userId, _TEST_TYPE_ID, grade)])
            QMessageBox().information(self, "CEESS-通知", "成绩上传成功！")
        else:
            info = "当前测试成绩已存在：\n" + str(round(exist, 2)) + " 分\n" + "是否更新成绩？"
            result = QMessageBox().warning(self, "CEESS-警告", info,
                                           QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                db.updateGrade(self.userId, _TEST_TYPE_ID, grade)
                QMessageBox().information(self, "CEESS-通知", "成绩上传成功！")
        db.closeConnect()

    @Slot()
    def on_btnStart_clicked(self):
        # load question bank.
        db = DataManager()
        self.questionBank = db.getRandomQuestion(
            _CHOICE_TYPE, _CHOICE_AMOUNT) + db.getRandomQuestion(
                _TRUE_FALSE_TYPE, _TRUE_FALSE_AMOUNT)
        db.closeConnect()
        if len(self.questionBank) < (_CHOICE_AMOUNT + _TRUE_FALSE_AMOUNT):
            QMessageBox().warning(self, "CEESS-警告",
                                  "当前题库数量少于设置数量，无法开始测试。请联系管理员。")
            self.close()

        # setup question table on the left of view.
        self.ui.questionTable.setRowCount(_CHOICE_AMOUNT + _TRUE_FALSE_AMOUNT)
        for i in range(_CHOICE_AMOUNT):
            self.ui.questionTable.setItem(i, 0, QTableWidgetItem())
            self.ui.questionTable.item(i,
                                       0).setBackgroundColor(QColor(0x96B97D))
        for i in range(_CHOICE_AMOUNT, _CHOICE_AMOUNT + _TRUE_FALSE_AMOUNT):
            self.ui.questionTable.setItem(i, 0, QTableWidgetItem())
            self.ui.questionTable.item(i,
                                       0).setBackgroundColor(QColor(0xFBF2D4))

        # automatically select first question at the beginning.
        self.ui.questionTable.item(self.qIndex, 0).setSelected(True)
        self.questionDisplay(self.questionBank[self.qIndex])
        # show a b c d button rather than true false at first
        self.ui.answerPages.setCurrentIndex(0)

        # switch to the test page.
        self.ui.pages.setCurrentIndex(1)

        # timing
        # initial time display label
        self.ui.lblTime.setText("{:0>2}:{:0>2}".format(round(_TEST_TIME // 60),
                                                       round(_TEST_TIME) % 60))
        # setup a 1s timer to update the remaining time display widget
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        # record current second
        self.startTime = time.time()

    @Slot(int, int)
    def on_questionTable_cellClicked(self, row, column):
        self.qIndex = row
        self.questionDisplay(self.questionBank[row])
        if self.qIndex < _CHOICE_AMOUNT:
            self.ui.answerPages.setCurrentIndex(0)
        else:
            self.ui.answerPages.setCurrentIndex(1)

    @Slot()
    def on_btnNext_clicked(self):
        if self.qIndex + 1 < len(self.questionBank):
            self.ui.questionTable.item(self.qIndex, 0).setSelected(False)
            self.ui.questionTable.item(self.qIndex + 1, 0).setSelected(True)
            self.on_questionTable_cellClicked(self.qIndex + 1, 0)
            # ensure item is visible
            self.ui.questionTable.scrollToItem(
                self.ui.questionTable.item(self.qIndex + 1, 0))

    @Slot()
    def on_btnPrev_clicked(self):
        if self.qIndex > 0:
            self.ui.questionTable.item(self.qIndex, 0).setSelected(False)
            self.ui.questionTable.item(self.qIndex - 1, 0).setSelected(True)
            self.on_questionTable_cellClicked(self.qIndex - 1, 0)
            # ensure item is visible
            self.ui.questionTable.scrollToItem(
                self.ui.questionTable.item(self.qIndex - 1, 0))

    @Slot()
    def on_btnA_clicked(self):
        self.ui.questionTable.selectedItems()[0].setText("A")
        self.on_btnNext_clicked()

    @Slot()
    def on_btnB_clicked(self):
        self.ui.questionTable.selectedItems()[0].setText("B")
        self.on_btnNext_clicked()

    @Slot()
    def on_btnC_clicked(self):
        self.ui.questionTable.selectedItems()[0].setText("C")
        self.on_btnNext_clicked()

    @Slot()
    def on_btnD_clicked(self):
        self.ui.questionTable.selectedItems()[0].setText("D")
        self.on_btnNext_clicked()

    @Slot()
    def on_btnTrue_clicked(self):
        self.ui.questionTable.selectedItems()[0].setText("T")
        self.on_btnNext_clicked()

    @Slot()
    def on_btnFalse_clicked(self):
        self.ui.questionTable.selectedItems()[0].setText("F")
        self.on_btnNext_clicked()

    @Slot()
    def on_btnSubmit_clicked(self):
        unfinished = self.finishingCheck()
        if (len(unfinished) != 0):
            info = "下述题目未完成：\n"
            for i in unfinished:
                info = info + str(i) + " "
            QMessageBox.warning(self, "CEESS-警告", info)
        else:
            self.timer.stop()
            score = self.answerCheck()
            self.ui.lblGrade.setText(str(round(score, 2)))
            self.ui.lblNameFinished.setText(self.userName)
            self.ui.pages.setCurrentIndex(2)

    @Slot()
    def updateTime(self):
        remainTime = _TEST_TIME - (time.time() - self.startTime)
        if (remainTime > 0):
            self.ui.lblTime.setText("{:0>2}:{:0>2}".format(
                round(remainTime // 60), round(remainTime % 60)))
        else:
            self.ui.lblTime.setText("时间到！")
            self.timer.stop()
            QMessageBox.warning(self, "CEESS-提醒", "考试时间到！")
            score = self.answerCheck()
            self.ui.lblGrade.setText(str(score))
            self.ui.lblNameFinished.setText(self.userName)
            self.ui.pages.setCurrentIndex(2)

    # update grade when close window
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.ui.pages.currentIndex() == 2:
            self.uploadGrade()

        # only update grade when finished.
        return super().closeEvent(event)
