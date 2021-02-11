"""
@file       : dataManager.py
@description: Contain all methods of database operation.
@date       : 2021/02/10 17:36:43
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

import sqlite3


class DBManager():
    def __init__(self, database):
        self._conn = sqlite3.connect(database)
        self._cursor = self._conn.cursor()

    def closeConnect(self):
        self._cursor.close()
        self._conn.close()

    def getTypeById(self, uid):
        self._cursor.execute("SELECT USER_TYPE FROM USER WHERE USER_ID ==?;",
                             (uid, ))
        result = self._cursor.fetchone()
        return result[0]

    def isPasswordCorrect(self, uid, password):
        self._cursor.execute("SELECT PASSWORD FROM USER WHERE USER_ID == ?;",
                             (uid, ))
        result = self._cursor.fetchone()
        if result is None:
            return False
        return bool(result[0] == password)
