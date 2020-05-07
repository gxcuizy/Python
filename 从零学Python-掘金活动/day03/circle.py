#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入圆长，计算圆周长和面积
author: gxcuizy
date: 2018-10-17
"""

# 程序主入口
if __name__ == '__main__':
    # 运算符的用法
    number_one = input('请输入第一个数：')
    number_two = input('请输入第二个数：')
    # + 加法的使用
    sum_value = float(number_one) + float(number_two)
    print('加法运算：' + number_one + ' + ' + number_two + ' = ' + str(sum_value))
    # - 减法的使用
    diff_value = float(number_one) - float(number_two)
    print('减法运算：' + number_one + ' - ' + number_two + ' = ' + str(diff_value))
    # * 乘法的使用
    mul_val = float(number_one) * float(number_two)
    print('乘法运算：' + number_one + ' * ' + number_two + ' = ' + str(mul_val))
    # / 除法的使用
    if number_two == '0':
        print('除法运算，除数不能为0')
    else:
        div_value = float(number_one) / float(number_two)
        print('除法运算：' + number_one + ' / ' + number_two + ' = ' + str(div_value))
    # % 取模的使用
    after_val = float(number_one) % float(number_two)
    print('取模运算：' + number_one + ' % ' + number_two + ' = ' + str(after_val))

    # π的值
    pai = 3.14
    # 圆长
    circle_len = int(input('请输入圆长计算周长和面积：'))
    # 计算圆周长
    circumference = 2 * pai * (circle_len / 2)
    print('圆周长为：' + str(circumference))
    # 计算圆面积
    area = pai * (circle_len / 2) ** 2
    print('圆面积为：' + str(area))
