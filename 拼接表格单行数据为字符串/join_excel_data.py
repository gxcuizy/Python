#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
拼接Excel表格单行数据，并写入文本
author: gxcuizy
time: 2021-03-01
"""

import pandas
import random
import os
import time


def print_msg(msg=''):
    """打印信息"""
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('[' + now_time + '] ' + msg)


# 程序主入口
if __name__ == "__main__":
    # 获取传入参数
    file_name = input('请输入当前目录下的表格文件名（例如“01.xlsx”）：')
    line_num = input('请输入要拼装的数据第几列（例如“1”）：')
    # 判断文件是否存在
    if os.path.exists(file_name) == False:
        print_msg('文件不存在')
        os.system("pause")
        exit(0)
    # 判断输入的行数是否为数字
    if line_num.isdigit() == False:
        print_msg('请输入列数的数字')
        os.system("pause")
        exit(0)
    try:
        # 获取表格数据
        print_msg('开始获取文件[' + file_name + ']的第[' + str(line_num) + ']列数据')
        line_num = int(line_num) - 1
        sheet = pandas.read_excel(io=file_name, usecols=[line_num])
        data = sheet.values.tolist()
        str_data = ''
        # 循环处理数据
        print_msg('已获取列数据条数[' + str(len(data)) + ']，开始处理数据……')
        for x in range(len(data)):
            if str(data[x][0]) != 'nan':
                str_data += "'" + str(data[x][0]) + "',"
        # 写入文本文件
        print_msg('数据处理完毕，开始写入……')
        random_num = random.randint(1000, 9999)
        with open('str_' + str(random_num) + '.txt', 'w') as f:
            f.write(str_data.strip(','))
        print_msg('数据写入完毕.')
    except Exception as err_info:
        # 异常信息
        print_msg(str(err_info))
    # 防止exe程序执行结束闪退
    os.system("pause")
