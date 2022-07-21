#-*- coding:utf-8 -*-
# writeIntoDatabase()

import pymysql
from createData import CreateData
# from createData.CreateData import get_one_data
from decoratorTime import timer

class ConnMysql(object):
    # 获取数据库连接
    def __init__(self):
        self.get_conn = pymysql.connect(host="192.168.196.130", 
        user="root", password="1233.rooT", database="python_test", port=3306, charset='utf8')
        # self.get_conn1 = pymysql.connect(host="192.168.196.130", 
        # user="root", password="1233.rooT", database="python_test", port=3306, charset='utf8')
        # 创建游标
        self.get_cursor = self.get_conn.cursor()

    # 定义SQL语句，并通过游标执行
    def create_table(self, tablename):
        # 定义创建表的SQL语句
        str_sql = "create table %s(student_name varchar(20), student_sex char(4), student_age int, student_email varchar(20));"%(tablename)
        
        # 通过游标执行SQL语句
        self.get_cursor.execute(str_sql)

    # 定义插入数据的方法
    @timer
    def insert_data(self, tablename, *args):
        str_sql = "insert into {0} values(%s, %s, %s, %s);".format(tablename)
        self.get_cursor.executemany(str_sql, args)
        self.get_conn.commit()
    
    # 定义一个关闭对象的方法
    def close_conn(self):
        self.get_conn.close()

# 测试代码
if __name__ == "__main__":
    conn = ConnMysql()
    createdate = CreateData()
    table_name = "student_test_220721"
    conn.create_table(table_name)
    list1 = []
    for i in range(1, 1000001):
        get_one = createdate.get_one_data()
        list1.append(get_one)
    conn.insert_data(table_name, *list1)
    conn.close_conn()
