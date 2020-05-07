#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
csv读写文件数据
author: gxcuizy
date: 2018-10-26
"""

import csv


def write_csv_by_list(file):
    """操作写CSV文件（列表类型）"""
    # 定义csv表头和主要内容
    csv_header = ['no', 'language', 'score', 'grade']
    csv_data = [
        ('1', 'python', '100', 'A'),
        ('2', 'php', '97', 'A+'),
        ('3', 'java', '99', 'B')
    ]
    # 打开一个文件write对象
    with open(file, 'w') as f:
        f_csv = csv.writer(f)
        # 写入头部，注意是row()
        print('正在写入表头……')
        f_csv.writerow(csv_header)
        # 写入行数据，注意是rows()
        print('正在写入行数据……')
        f_csv.writerows(csv_data)
        print('写入完成！')


def write_csv_by_dict(file):
    """操作写CSV文件（字典类型）"""
    # 定义csv表头和主要内容
    csv_header = ['no', 'language', 'score', 'grade']
    csv_data = [
        {'no': '1', 'language': 'python', 'score': '100', 'grade': 'A'},
        {'no': '2', 'language': 'php', 'score': '96', 'grade': 'B'},
        {'no': '3', 'language': 'java', 'score': '98', 'grade': 'A+'}
    ]
    # 打开一个文件DictWriter对象
    with open(file, 'w') as f:
        f_csv = csv.DictWriter(f, csv_header)
        # 写入头部，注意是writeheader()
        print('正在写入表头……')
        f_csv.writeheader()
        # 写入行数据，注意是rows()
        print('正在写入行数据……')
        f_csv.writerows(csv_data)
        print('写入完成！')


def read_csv_by_next(file):
    """操作读CSV文件（next逐个获取）"""
    with open(file) as f:
        f_csv = csv.reader(f)
        print('-------------next逐个获取-------------')
        csv_header = next(f_csv)
        next(f_csv)
        csv_row = next(f_csv)
        # 打印头部
        print(csv_header)
        # 打印第一行数据
        print(csv_row)


def read_csv_by_normal(file):
    """操作读CSV文件（普通获取）"""
    with open(file) as f:
        f_csv = csv.reader(f)
        print('-------------全部普通获取-------------')
        for row in f_csv:
            if row:
                print(row)


def read_csv_by_dict(file):
    """操作读CSV文件（输出字典类型）"""
    with open(file) as f:
        # 主要使用DictReader()字典型读取
        f_csv = csv.DictReader(f)
        print('-------------下面是输出字典类型-------------')
        for row in f_csv:
            print(dict(row))


# 程序主入口
if __name__ == '__main__':
    # 生成一个csv文件，并写入数据
    # list列表类型数据写入
    write_csv_by_list('list.csv')
    # dict字典类型数据写入
    write_csv_by_dict('dict.csv')
    # next逐个读取
    read_csv_by_next('dict.csv')
    # 普通直接读取
    read_csv_by_normal('dict.csv')
    # 转为字典型读取
    read_csv_by_dict('dict.csv')
