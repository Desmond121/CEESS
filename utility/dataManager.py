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

    def isPasswordCorrectById(self, UID, password):
        self._cursor.execute(
            "select PASSWORD from USER \
                where UID == ? limit 1;", [UID])
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)

    def getAllUserInfo(self):
        self._cursor.execute(
            "select USER_NAME, USER_ACCOUNT, USER_TYPE from USER limit 1;")
        return self._cursor.fetchall()

    def deleteUserByAccount(self, account):
        self._cursor.execute("delete from USER where USER_ACCOUNT = ?;",
                             [account])
        self._conn.commit()

    def addNewUser(self, account, name, isAdmin):
        self._cursor.execute(
            "insert into USER (USER_ACCOUNT, USER_NAME, USER_TYPE) \
                values (?, ?, ?);", [account, name, isAdmin])
        self._conn.commit()

    def isOccupied(self, account):
        self._cursor.execute(
            "select USER_ACCOUNT from USER \
                where USER_ACCOUNT == ? limit 1", [account])
        return bool(len(self._cursor.fetchall()))

    def changePasswordById(self, UID, newPassword):
        self._cursor.execute("update USER set PASSWORD = ? where UID = ?",
                             [newPassword, UID])
        self._conn.commit()

    def changeNameById(self, UID, newName):
        self._cursor.execute("update USER set USER_NAME = ? where UID = ?",
                             [newName, UID])
        self._conn.commit()
