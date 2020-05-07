#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
os模块的相关使用-创建多级目录
author: gxcuizy
date: 2018-10-23
"""

import os


def make_dir(path):
    """逐个创建三级目录"""
    path_list = path.split('/')
    for path_value in path_list:
        # 目录不存在，则创建
        exists = os.path.exists(path_value)
        if not exists:
            os.mkdir(path_value)
            print('已创建目录-%s' % os.path.abspath(path_value))
        # 切换目录
        os.chdir(path_value)
        # 创建index.txt文件
        with open('index.txt', 'w') as file:
            file.write('hello world!')
        print('已创建文件-%s' % os.path.abspath('index.txt'))


# 程序主入口
if __name__ == '__main__':
    dir_path = 'language/python/learn'
    # 一次性创建多级文件夹
    os.makedirs(dir_path)
    # 删除多级目录
    os.removedirs(dir_path)
    # 逐个创建文件夹及文件
    make_dir(dir_path)
