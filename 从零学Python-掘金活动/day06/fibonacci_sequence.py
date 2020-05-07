#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用生成器创建斐波拉契数列
author: gxcuizy
date: 2018-10-20
"""


def get_sequence(num):
    """获取斐波拉契数列"""
    # 初始化数据
    n = 0
    one = 0
    two = 1
    # 获取各个数列值
    while n < num:
        # 返回数列值
        yield two
        # 替换位置计算
        tmp = one
        one = two
        two += tmp
        n += 1


# 程序主入口
if __name__ == '__main__':
    number = int(input('请输入一个数获取斐波拉契数列：'))
    # 获取数列
    number_list = get_sequence(number)
    # 打印数列
    for value in number_list:
        print(value)
