#-*- coding:utf-8 -*-

from openpyxl import Workbook
from createData import CreateData

class ExcelData(object):
    def __init__(self):
        self.data = CreateData()
        self.workbook = Workbook()
        self.get_sheet = self.workbook.active
    
    def create_data(self):
        for row in range(1, 10001):
            self.get_sheet.append(self.data.get_one_data())
        self.workbook.save("testDatas.xlsx")

# 测试代码
if __name__ == '__main__':
    excel = ExcelData()
    excel.create_data()