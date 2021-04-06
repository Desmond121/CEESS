"""
@file       : dataManager.py
@description: Contain all methods of database operation.
@date       : 2021/02/10 17:36:43
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

import sqlite3

_DEFAULT_DATABASE = "./data/db.sqlite3"


class DataManager():
    def __init__(self, database=_DEFAULT_DATABASE):
        self._conn = sqlite3.connect(database)
        self._conn.execute(
            "PRAGMA foreign_keys = 1")  # open foreign key support
        self._cursor = self._conn.cursor()

    def closeConnect(self):
        self._cursor.close()
        self._conn.close()

    def getNameById(self, userId):
        self._cursor.execute(
            "select USER_NAME from USER \
                where UID == ? limit 1;", [userId])
        result = self._cursor.fetchone()
        return str(result[0])

    def getAccountById(self, userId):
        self._cursor.execute(
            "select USER_ACCOUNT from USER \
                where UID == ? limit 1;", [userId])
        result = self._cursor.fetchone()
        return str(result[0])

    def isPasswordCorrectById(self, UID, password):
        self._cursor.execute(
            "select PASSWORD from USER \
                where UID == ? limit 1;", [UID])
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)

    def changePasswordById(self, UID, newPassword):
        self._cursor.execute("update USER set PASSWORD = ? where UID = ?;",
                             [newPassword, UID])
        self._conn.commit()

    def changeNameById(self, UID, newName):
        self._cursor.execute("update USER set USER_NAME = ? where UID = ?;",
                             [newName, UID])
        self._conn.commit()

    def deleteQuestionById(self, questionId):
        self._cursor.execute("delete from QUESTION_BANK where QID = ?;",
                             [questionId])
        self._conn.commit()

    def getTypeAndIdByAccount(self, account):
        self._cursor.execute(
            "select USER_TYPE, UID from USER \
                where USER_ACCOUNT ==? limit 1;", [account])
        result = self._cursor.fetchone()
        # result is a tuple whose content is in form of (USER_TYPE,UID)
        return result

    def isPasswordCorrectByAccount(self, account, password):
        self._cursor.execute(
            "select PASSWORD from USER \
                where USER_ACCOUNT == ? limit 1;", [account])
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)

    def getAllUserInfo(self):
        self._cursor.execute(
            "select USER_NAME, USER_ACCOUNT, USER_TYPE from USER;")
        return self._cursor.fetchall()

    def getAllQuestion(self, type):
        self._cursor.execute("select * from QUESTION_BANK where TYPE = ?;",
                             [type])
        return self._cursor.fetchall()

    def getRandomQuestion(self, type, amount):
        self._cursor.execute(
            "select * from QUESTION_BANK where TYPE = ? order by random() \
                limit ?;", [type, amount])
        return self._cursor.fetchall()

    def deleteAllQuestion(self):
        self._cursor.execute("delete from QUESTION_BANK;")
        self._cursor.execute(
            "update sqlite_sequence SET seq = 0 WHERE name = 'QUESTION_BANK';")
        self._conn.commit()

    def deleteUserByAccount(self, account):
        self._cursor.execute("delete from USER where USER_ACCOUNT = ?;",
                             [account])
        self._conn.commit()

    def addNewUser(self, account, name, isAdmin):
        self._cursor.execute(
            "insert into USER (USER_ACCOUNT, USER_NAME, USER_TYPE) \
                values (?, ?, ?);", [account, name, isAdmin])
        self._conn.commit()

    def addNewQuestion(self, body, choiceA, choiceB, choiceC, choiceD, type,
                       answer):
        self._cursor.execute(
            "insert into QUESTION_BANK (BODY, A, B, C, D, TYPE, ANSWER) \
                values (?, ?, ?, ?, ?, ?, ?);",
            [body, choiceA, choiceB, choiceC, choiceD, type, answer])
        self._conn.commit()
        self._cursor.execute("select max(QID) from QUESTION_BANK;")
        return self._cursor.fetchone()

    def addGrade(self, uid, tid, grade):
        # check whether existing
        self._cursor.execute(
            "select SCORE from GRADE where (UID,TID) = (?, ?);", [uid, tid])
        result = self._cursor.fetchone()
        if result is None:
            self._cursor.execute(
                "insert into GRADE (UID, TID, SCORE) values (?, ?, ?);",
                [uid, tid, grade])
            self._conn.commit()
            return -1
        else:
            return result[0]  # the existing grade

    def updateGrade(self, uid, tid, grade):
        self._cursor.execute(
            "update GRADE set SCORE = ? where (UID, TID) = (?, ?);",
            [grade, uid, tid])
        self._conn.commit()
