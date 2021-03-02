#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pandas处理表格数据，在当前表格行中增加数据并保存到原表格
author: gxcuizy
time: 2021-03-02
"""

import pandas
from pandas import DataFrame
import pymysql


def get_mysql_info(cursor, order_code):
    """获取数据库数据（根据自己的实际情况来修改）"""
    # 组装数据sql
    sql = "SELECT order_total, order_status FROM order WHERE order_code = '%s'" % (order_code,)
    # 获取一条数据
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


# 程序主入口
if __name__ == "__main__":
    # 创建一个连接
    db_host = '127.0.0.1'
    db_name = 'test'
    db_user = 'root'
    db_pw = 'root'
    db_port = 3306
    db = pymysql.connect(host=db_host, user=db_user, password=db_pw, database=db_name, port=db_port)
    # 用cursor()创建一个游标对象
    cursor_obj = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 读取excel数据
    print('开始读取表格数据……')
    file_name = '1.xlsx'
    sheet = pandas.read_excel(file_name)
    # 数据转列表
    data = sheet.values.tolist()
    # 循环处理数据
    print('读取数据完毕，开始处理数据……')
    for i, val in enumerate(data):
        # 获取附加的行数据
        print('正在处理order_code=%s' % val[0])
        info = get_mysql_info(cursor_obj, val[0])
        if info:
            data[i].append(info['order_total'])
            data[i].append(info['order_status'])
    # 表头信息，转数据格式存储
    excel_header = ['sort', 'name', 'stu_no', 'course', 'score']
    data = pandas.DataFrame(data, columns=excel_header)
    data.to_excel(file_name, index=False, header=True)
    print('写入excel完成！')
