import sqlite3


class DBManager():
    def __init__(self, database):
        try:
            self._conn = sqlite3.connect(database)
            self._cursor = self._conn.cursor()
        except sqlite3.DatabaseError as dbe:
            print("数据库链接错误")

    def closeConnect(self):
        self._cursor.close()
        self._conn.close()

    def getTypeById(self, uid):
        self._cursor.execute(
            "SELECT USER_TYPE FROM USER WHERE USER_ID ==?;", (uid,))
        result = self._cursor.fetchone()
        return(result[0])

    def isPasswordCorrect(self, uid, password):
        self._cursor.execute(
            "SELECT PASSWORD FROM USER WHERE USER_ID == ?;", (uid,))
        result = self._cursor.fetchone()
        if result is None:
            return False
        return(bool(result[0] == password))
