#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
os模块的使用和练习
author: gxcuizy
date: 2018-10-21
"""

import os

# 程序主入口
if __name__ == '__main__':
    # 获取操作系统类型
    # posix说明系统是Linux、Unix或Mac OS X，如果是nt就是Windows系统
    os_name = os.name
    print(os_name)

    # 获取详细的系统信息，可以调用uname()函数
    # print(os.uname())，windows不支持

    # 使用environ属性打印环境变量
    env_info = os.environ
    print(env_info)

    # 调用os.environ.get('key')获取某个环境变量的值
    path_value = os.environ.get('path')
    print(path_value)

    # 查看当前目录的绝对目录
    abs_path = os.path.abspath('.')
    print(abs_path)

    # 目录拼接
    join_path = os.path.join('.', 'test')
    print(join_path)

    # mkdir()创建目录，创建多级目录用makedirs()
    os.mkdir('test')

    # rmdir()删除目录，删除多级目录用removedirs()
    os.rmdir('test')

    # 使用os.path.split()拆分目录信息
    split_info = os.path.split('/data/code/test.py')
    print(split_info)

    # 使用os.path.splitext()直接获取文件扩展名
    file_ext = os.path.splitext('/data/code/test.py')
    print(file_ext)

    # 使用rename()重命名，os.rename('test.py', 'test.txt')
    # 使用remove()删除文件，os.remove('test.txt')

    # shutil模块提供了copyfile()的复制文件的函数

    # listdir()获取路径下的文件目录
    list_dir = os.listdir('.')
    print(list_dir)

    # os.path.isdir()判断是否是目录
    # os.path.isfile()判断是否是文件
