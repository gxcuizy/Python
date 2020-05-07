#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用pymysql模块管理mysql的连接和CURD基础使用
author: gxcuizy
date: 2018-10-24
"""

import pymysql


def show_version():
    """基础使用，查看mysql版本"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 使用execute()执行一个mysql语句查询
    cursor.execute('select version();')
    # 使用fetchone()获取一条数据
    mysql_version = cursor.fetchone()
    print(mysql_version)
    # 关闭连接
    cursor.close()
    db.close()


def create_table(t_name):
    """创建一张数据表"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 如果表存在则删除
    print('开始建表')
    cursor.execute("DROP TABLE IF EXISTS %s" % t_name)
    # 表结构sql
    sql = 'create table %s (id int not null auto_increment,name varchar(50) null,age int default "0",primary key (id))charset=utf8;' % t_name
    # 执行建表
    cursor.execute(sql)
    # 关闭连接
    cursor.close()
    db.close()
    print('建表成功！')


def add_data(t_name, data):
    """新增一条数据"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 插入数据sql
    print('开始新增一条数据：%s' % data)
    data.insert('0', t_name)
    sql = 'insert into %s (name, age) values (%s, %s);' % data
    # 执行插入
    cursor.execute(sql)
    # commit()提交执行，如果发生异常，db.rollback()可以回滚
    db.commit()
    # 关闭连接
    cursor.close()
    db.close()
    print('新增数据成功！')


def select_data(t_name, user_id):
    """查询表数据"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 查询数据sql
    print('查询id为%s的数据' % user_id)
    sql = 'select * from %s where id = %s' % (t_name, user_id)
    # 执行查询
    cursor.execute(sql)
    # 获取查询结果fetchone()获取一条，fetchall()获取全部查询数据
    data = cursor.fetchall()
    print(data)
    # 关闭连接
    cursor.close()
    db.close()
    print('查询完毕！')


def update_data(t_name):
    """update修改表数据"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 更新数据sql
    print('查询表%s的数据' % t_name)
    sql = 'update %s set age = %s where id = %s' % (t_name, 20, 1)
    # 执行更新操作
    cursor.execute(sql)
    # 获取执行之后的影响行数
    result = cursor.rowcount()
    if result > 0:
        # 提交执行
        db.commit()
    else:
        # 执行失败，回滚
        db.rollback()
    # 关闭连接
    cursor.close()
    db.close()
    print('更新完毕，影响行数为%s' % result)


def delete_data(t_name, user_id):
    """delete删除表数据"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor()
    # 删除数据sql
    print('删除id为%s的数据' % user_id)
    sql = 'delete from %s where id = %s' % (t_name, user_id)
    # 执行删除操作
    cursor.execute(sql)
    # 获取执行之后的影响行数
    result = cursor.rowcount()
    if result > 0:
        # 提交执行
        db.commit()
    else:
        # 执行失败，回滚
        db.rollback()
    # 关闭连接
    cursor.close()
    db.close()
    print('删除完毕，影响行数为%s' % result)


# 程序入住口
if __name__ == '__main__':
    # 数据库链接参数
    db_host = 'localhost'
    db_name = 'python'
    db_user = 'root'
    db_pw = 'root'
    # 查看mysql版本
    show_version()
    # 建表
    table_name = 'user'
    create_table(table_name)
    # 插入数据
    add_data(table_name, ['python', 10])
    # 查询数据
    select_data(table_name, 1)
    # 修改数据
    update_data(table_name)

    # 再次执行插入一条数据
    # 插入数据
    add_data(table_name, ['test', 18])
    # 查询数据
    select_data(table_name, 2)
    # 删除上面插入的数据
    delete_data(table_name, 2)
