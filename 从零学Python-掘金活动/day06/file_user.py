#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
文件操作的使用和练习
author: gxcuizy
date: 2018-10-20
"""

# 程序主入口
if __name__ == '__main__':
    # 以读文件的模式打开一个文件对象
    file_path = 'test.txt'
    file = open(file_path)

    # 调用方法read()一次读取文件的全部内容
    file_content = file.read()
    print(file_content)

    # 读完文件，使用close()进行关闭
    file.close()

    # 使用with语句来自动调用close()方法关闭文件
    with open(file_path) as file:
        print(file.read())

    # 调用readline()可以每次读取一行内容
    with open(file_path) as file:
        file_line_one = file.readline()
        file_line_two = file.readline()
        print(file_line_one)
        print(file_line_two)

    # 调用readlines()一次读取所有内容并按行返回list
    with open(file_path) as file:
        for line in file.readlines():
            print(line)

    # 使用'rb'模式打开二进制文件，例如图片、视频
    # open('test.jpg', 'rb')

    # 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
    # open('test.txt', 'r',  encoding='gbk')

    # 写文件，写文本的模式是'w'，写例如图片和视频等二进制文件的模式是'wb'，然后使用write()方法写入内容
    # 允许多次调用write()方法写入内容
    with open('ttt.txt', 'w') as file:
        file.write('hello python!\n')
        file.write('hello world!')

    # 'w'模式每次都会新建或者清空已存在的内容，如果需要追加就使用模式'a'打开文件
    with open('test.txt', 'a') as file:
        file.write('\n000000')
