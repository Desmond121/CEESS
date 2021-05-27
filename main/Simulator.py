"""
@file       : Simulator.py
@description: For simulator module.
@date       : 2021/03/22 18:32:58
@author     : Desmond
@email      : dmz990121@outlook.com
@version    : 0.0.1
"""
from simulation.SignRecognizing import SignRecognizing
from simulation.fireExtinguisherUsing import fireExtingusherUsing
from simulation.AutoclaveSafety import AutoclaveSafety
from simulation.GasCylindersOperation import GasCylindersOperation
from utility.DataManager import DataManager
from simulation.LeaveTheLab import LeaveTheLab
from simulation.EnterTheLab import EnterTheLab
from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QMainWindow, QMessageBox
from ui.generate.Ui_Simulator import Ui_Simulator


class Simulator(QMainWindow):
    # simulationClassDict = {Id: simulationWidgetClass, ...}
    # must be aligned with the database sheet "TEST_TYPE"
    simulationsClassDict = {
        2: EnterTheLab,
        3: LeaveTheLab,
        4: GasCylindersOperation,
        5: AutoclaveSafety,
        6: fireExtingusherUsing,
        7: SignRecognizing
    }

    isFinished = False  # 0 is unfinished
    score = -1  # no score yet
    userId = None
    testTypeId = None

    def __init__(self, Uid, simulationId, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Simulator()
        self.ui.setupUi(self)
        self.setFixedSize(1000, 600)

        self.userId = Uid
        self.testTypeId = simulationId

        simulationClass = self.simulationsClassDict.get(simulationId)
        simulator = simulationClass(self)
        simulator.finishedSignal.connect(self.setFinish)
        self.setCentralWidget(simulator)

    def closeEvent(self, event):
        if self.isFinished:
            db = DataManager()
            # if existing, = EXISTING_SCORE, else = -1
            exist = db.gradeDuplicateCheck(self.userId, self.testTypeId)

            if exist == -1:
                db.insertGrade([(self.userId, self.testTypeId, self.score)])
                QMessageBox().information(self, "CEESS-通知", "成绩上传成功！")
            else:
                info = "当前测试成绩已存在：\n" + str(round(exist,
                                                  2)) + " 分\n" + "是否更新成绩？"
                result = QMessageBox().warning(
                    self, "CEESS-警告", info, QMessageBox.Yes | QMessageBox.No)
                if result == QMessageBox.Yes:
                    db.updateGrade(self.userId, self.testTypeId, self.score)
                    QMessageBox().information(self, "CEESS-通知", "成绩上传成功！")
            db.closeConnect()
            return super().closeEvent(event)
        else:
            result = QMessageBox().warning(self, "CEESS-警告", "还未完成练习，是否退出？",
                                           QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                return super().closeEvent(event)

    @Slot(int)
    def setFinish(self, score):
        self.isFinished = True
        self.score = score
