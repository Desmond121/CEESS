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

    def getTypeByAccount(self, account):
        self._cursor.execute(
            "select USER_TYPE from USER where USER_ACCOUNT ==?;", [account])
        result = self._cursor.fetchone()
        return result[0]

    def isPasswordCorrect(self, account, password):
        self._cursor.execute(
            "select PASSWORD from USER where USER_ACCOUNT == ?;", [account])
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)

    def getAllUserInfo(self):
        self._cursor.execute(
            "select USER_NAME, USER_ACCOUNT, USER_TYPE from USER;")
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
            "select USER_ACCOUNT from USER where USER_ACCOUNT == ?", [account])
        return bool(len(self._cursor.fetchall()))
