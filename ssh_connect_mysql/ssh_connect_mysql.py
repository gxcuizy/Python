#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
通过跳板机，连接远程mysql数据库
author: gxcuizy
time: 2018-08-10
"""

import pymysql
from sshtunnel import SSHTunnelForwarder

# 程序主入口
if __name__ == "__main__":
    # 跳板机SSH连接
    with SSHTunnelForwarder(
            ('192.168.0.1', 22),
            ssh_username="test",
            ssh_pkey="test.pem",
            remote_bind_address=('*************mysql.rds.aliyuncs.com', 3306)
    ) as tunnel:
        # 数据库连接配置，host默认127.0.0.1不用修改
        conn = pymysql.connect(
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            user='root',
            password='root',
            db='test',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        # 获取游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 查询数据库，查询一条数据，其他CURD操作类似
        sql = "SELECT name FROM table_name WHERE id = '%s'"
        prams = ('1',)
        cursor.execute(sql % prams)
        info = cursor.fetchone()
        print(info)
        # 关闭连接
        cursor.close()
        conn.close()
