#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
压缩和解压缩zip文件
author: gxcuizy
time：2018-08-13
"""

import zipfile
import os


def create_zip(path):
    """创建一个压缩文件"""
    # 创建一个zip文件对象
    zip_file = zipfile.ZipFile(os.path.basename(path) + ".zip", "w")
    # 将文件写入zip文件中，即将文件压缩
    print('开始压缩文件……')
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            print("正在压缩文件夹：" + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
        for name in files:
            print("正在压缩文件：" + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
    # 关闭zip文件对象
    zip_file.close()


def uncompress_zip(path):
    """解压缩一个文件"""
    print('正在解压文件中……')
    zfile = zipfile.ZipFile(path, "r")
    zfile.extractall()


# 程序主入口
if __name__ == "__main__":
    # 打包（解压缩）的文件路径（文件名）
    path_info = 'test.zip'
    if os.path.isdir(path_info):
        # 打包
        create_zip(path_info)
        print('压缩完成！')
    elif os.path.isfile(path_info):
        # 解压
        uncompress_zip(path_info)
        print('解压完成！')
    else:
        print('文件类型错误，请重试！')
