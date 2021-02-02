# This file is used for managing all the forms.
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from ui.Ui_Login import Ui_Login
from ui.Ui_Student import Ui_Student
from ui.Ui_Teacher import Ui_Teacher
from dataManager import DBManager


class LoginForm(Ui_Login, QWidget):
    # Intermediate class for better Encapsulation.
    def __init__(self):
        super(LoginForm, self).__init__()
        self.setupUi(self)
        self.sizeAdapt(0.3)
        # Signal slots.
        self.loginButtom.clicked.connect(self.loginAndSwitch)

    def loginAndSwitch(self):
        userId = self.LineEdit_Account.text()
        password = self.lineEdit_Password.text()
        data = DBManager("./data/db.sqlite3")
        if data.isPasswordCorrect(userId, password):
            isTeacher = data.getTypeById(userId)
            if isTeacher:
                self.subForm = TeacherForm()
            else:
                self.subForm = StudentForm()
            self.subForm.show()
            self.close()
        else:
            print("密码错误")


class StudentForm(Ui_Student, QMainWindow):
    # Intermediate class for better encapsulation.
    def __init__(self):
        super(StudentForm, self).__init__()
        self.setupUi(self)
        # Signal slots.


class TeacherForm(Ui_Teacher, QMainWindow):
    # Intermediate class for better encapsulation.
    def __init__(self):
        super(TeacherForm, self).__init__()
        self.setupUi(self)
        # Signal slots.
