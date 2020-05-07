#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
遍历目录下的文件夹和文件
author: gxcuizy
date: 2018-10-23
"""

import os


def for_dirs(path):
    """递归遍历文件夹"""
    for path_value in os.listdir(path):
        if os.path.isfile(os.path.join(path, path_value)):
            print('这是文件-%s' % os.path.join(path, path_value))
        else:
            current_path = os.path.join(path, path_value)
            print('这是目录-%s' % current_path)
            for_dirs(current_path)


def walk_dirs(path):
    """os.walk()遍历文件夹"""
    for current_path, dir_list, file_list in os.walk(path):
        for file_name in file_list:
            print('这是文件-%s' % os.path.join(current_path, file_name))
        for dir_name in dir_list:
            print('这是目录-%s' % os.path.join(current_path, dir_name))


# 程序主入口
if __name__ == '__main__':
    # 遍历的目录
    dir_path = 'language'
    # 自定义递归遍历
    print('-----------------递归遍历--------------------------')
    for_dirs(dir_path)
    # os.walk()遍历文件夹
    print('-----------------os.wal()-------------------------')
    walk_dirs(dir_path)
    print('-----------------遍历结束--------------------------')
