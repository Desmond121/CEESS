"""
@file       : excelManager.py
@description: This class is built to import infomation from excel files.
@date       : 2021/03/02 17:22:10
@author     : Desmond
@e-mail     : dmz990121@outlook.com
@version    : 0.0.1
"""

import xlrd


class ExcelManager():
    def __init__(self, filePath):
        self.book = xlrd.open_workbook(filePath)
        self.sheet = self.book.sheet_by_index(0)

    def getUserData(self):
        userList = list()
        for row in range(2, self.sheet.nrows):
            user = self.sheet.row_values(row, 0, 3)
            userList.append(user)
        return userList
