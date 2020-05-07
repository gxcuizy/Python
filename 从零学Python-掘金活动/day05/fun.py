#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
函数的使用
author: gxcuizy
date: 2018-10-19
"""


def fun(number=18):
    """定义函数，传参数并带默认值"""
    if number > 18:
        return '成年人'
    else:
        return '小屁孩'


def re_fun(number):
    """递归调用，计算某个数的阶乘"""
    if number == 1:
        return number
    return number * re_fun(number - 1)


# 程序主入口
if __name__ == '__main__':
    # 取绝对值
    print(abs(-200))

    # 取最大值
    numbers = (1, 2, 6, 8, 6, 9)
    print(max(numbers))

    # 类型转换-int()转为整数型
    print(int('666'))

    # 类型转换-float()转为浮点数型
    print(float('666'))

    # 类型转换-str()转为字符串型
    print(str(666))

    # 类型转换-bool()转为布尔型
    print(bool(666))

    # 自定义一个函数，并传参数
    result = fun(20)
    print(result)

    # 阶乘计算，递归函数的定义和调用
    re_result = re_fun(4)
    print(re_result)
