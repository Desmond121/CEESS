"""
@file       : dataManager.py
@description: Contain all methods of database operation.
@date       : 2021/02/10 17:36:43
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

import sqlite3

import pymysql

# select a database type
_SQLITE = 0
_MYSQL = 1
_DATABASE_TYPE = _SQLITE

_SQLITE_DATABASE = "./data/db.sqlite3"
_MYSQL_IP = "101.132.143.156"
_MYSQL_PORT = 33060
_MYSQL_NAME = "CEESS"
_MYSQL_PASSWORD = "1234567890"
_MYSQL_DATABASE = "CEESS"


class DataManager():
    def __init__(self, database=_SQLITE_DATABASE):
        if _DATABASE_TYPE == 1:
            self._conn = pymysql.connect(host=_MYSQL_IP,
                                         port=_MYSQL_PORT,
                                         user=_MYSQL_NAME,
                                         password=_MYSQL_PASSWORD,
                                         database=_MYSQL_DATABASE)
            self._cursor = self._conn.cursor()

        else:
            self._conn = sqlite3.connect(database)
            self._conn.execute(
                "PRAGMA foreign_keys = 1")  # open foreign key support
            self._cursor = self._conn.cursor()

    def closeConnect(self):
        self._cursor.close()
        self._conn.close()

    # operation on table "USER"
    def getNameById(self, userId):
        sql = "select USER_NAME from USER where UID = %s limit 1;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [userId])
        result = self._cursor.fetchone()
        return str(result[0])

    def getAccountById(self, userId):
        sql = "select USER_ACCOUNT from USER where UID = %s limit 1;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [userId])
        result = self._cursor.fetchone()
        return str(result[0])

    def isPasswordCorrectById(self, UID, password):
        sql = "select PASSWORD from USER where UID = %s limit 1;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [UID])
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)

    def changePasswordById(self, UID, newPassword):
        sql = "update USER set PASSWORD = %s where UID = %s;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [newPassword, UID])
        self._conn.commit()

    def changeNameById(self, UID, newName):
        sql = "update USER set USER_NAME = %s where UID = %s;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [newName, UID])
        self._conn.commit()

    def getTypeAndIdByAccount(self, account):
        sql = "select USER_TYPE, UID from USER \
            where USER_ACCOUNT = %s limit 1;"

        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [account])
        result = self._cursor.fetchone()
        # result is a tuple whose content is in form of (USER_TYPE,UID)
        return result

    def isPasswordCorrectByAccount(self, account, password):
        sql = "select PASSWORD from USER where USER_ACCOUNT = %s limit 1;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [account])
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)

    def getAllUserInfoDict(self):
        sql = "select USER_ACCOUNT, USER_NAME, USER_TYPE, UID from USER;"
        self._cursor.execute(sql)
        users = self._cursor.fetchall()
        userInfoDict = dict()
        for user in users:
            userInfoDict.setdefault(user[0], (user[1], user[2], user[3]))
        # userInfoDict: {"userAccount":(name, type, id), "xxx":(...)}
        return userInfoDict

    def getStudentNames(self):
        sql = "select UID, USER_NAME from USER where USER_TYPE = 0;"
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def addNewUserByList(self, userInfoList: list):
        """userInfoList = [(account, name, isAdmin), (...)]"""

        sql = "insert into USER (USER_ACCOUNT, USER_NAME, USER_TYPE) \
                values (%s, %s, %s);"

        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")

        self._cursor.executemany(sql, userInfoList)
        self._conn.commit()

    def deleteUserByIdList(self, idList: list):
        sql = "delete from USER where UID = %s;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.executemany(sql, idList)
        self._conn.commit()

    # operation on table "QUESTION_BANK"
    def getAllQuestion(self, type):
        sql = "select * from QUESTION_BANK where TYPE = %s;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [type])
        return list(self._cursor.fetchall())

    def getRandomQuestion(self, type, amount):
        sql = "select * from QUESTION_BANK where TYPE = %s order by rand() \
                limit %s;"

        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?").replace("rand", "random")

        self._cursor.execute(sql, [type, amount])
        return list(self._cursor.fetchall())

    def deleteAllQuestion(self):
        if _DATABASE_TYPE == _SQLITE:
            self._cursor.execute("delete from QUESTION_BANK;")
            self._cursor.execute("update sqlite_sequence SET seq = 0 \
                    WHERE name = 'QUESTION_BANK';")
            self._conn.commit()
        else:
            self._cursor.execute("truncate table QUESTION_BANK;")
            self._conn.commit()

    def addQuestionFromList(self, questionList: list):
        sql = "insert into QUESTION_BANK (BODY, A, B, C, D, TYPE, ANSWER) \
            values (%s, %s, %s, %s, %s, %s, %s);"

        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")

        self._cursor.executemany(sql, questionList)
        self._conn.commit()

    def deleteQuestionById(self, idList: list):
        sql = "delete from QUESTION_BANK where QID = %s;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.executemany(sql, idList)
        self._conn.commit()

    # operation on table "GRADE"
    def deleteAllGrade(self):
        if _DATABASE_TYPE == _SQLITE:
            sql = "delete from GRADE;"
        else:
            sql = "truncate GRADE;"
        self._cursor.execute(sql)
        self._conn.commit()

    def gradeDuplicateCheck(self, uid, tid):
        sql = "select SCORE from GRADE where (UID, TID) = (%s, %s);"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [uid, tid])
        result = self._cursor.fetchone()
        if result is None:
            return -1
        else:
            return result[0]

    # insert by list: [(uid, tid, grade), ...]
    def insertGrade(self, gradelist: list):
        sql = "insert into GRADE (UID, TID, SCORE) values (%s, %s, %s);"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.executemany(sql, gradelist)
        self._conn.commit()

    def updateGrade(self, uid, tid, newGrade):
        sql = "update GRADE set SCORE = %s where (UID, TID) = (%s, %s);"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [newGrade, uid, tid])
        self._conn.commit()

    def getAllGrade(self):
        sql = "select * from GRADE;"
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def getGradeByUid(self, uid):
        sql = "select TID, SCORE from GRADE where UID = %s;"
        if _DATABASE_TYPE == _SQLITE:
            sql = sql.replace("%s", "?")
        self._cursor.execute(sql, [uid])
        return self._cursor.fetchall()

    # operation on table "TEST_TYPE"
    def getTestTypeDict(self):
        sql = "select * from TEST_TYPE;"
        self._cursor.execute(sql)
        result = self._cursor.fetchall()
        typeDict = dict()
        for id, name in result:
            typeDict.setdefault(id, name)
        return typeDict
