#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
简易计算器的实现
author: gxcuizy
date: 2018-10-16
"""

# 程序主入口
if __name__ == '__main__':
    # 运算方式
    operate_type = input('请选择运算类型：1加法，2减法，3乘法，4除法：')
    # 判断类型是否有效
    while int(operate_type) not in (1, 2, 3, 4):
        print('类型选择错误，只能为1-4')
        operate_type = input('请重新选择运算类型：1加法，2减法，3乘法，4除法：')
    # 第一个数
    number_one = int(input('请输入第一个数：'))
    # 第二个数
    number_two = int(input('请输入第二个数：'))
    if operate_type == '1':
        # 1加法
        result = number_one + number_two
        print('加法运算，结果是：' + str(result))
    elif operate_type == '2':
        # 2减法
        result = number_one - number_two
        print('减法运算，结果是：' + str(result))
    elif operate_type == '3':
        # 3乘法
        result = number_one * number_two
        print('乘法运算，结果是：' + str(result))
    elif operate_type == '4':
        # 4除法
        if number_two == 0:
            print('第二个数即除数不能为0')
        else:
            result = number_one / number_two
            print('除法运算，结果是：' + str(result))
    else:
        print('算法类型错误')
