#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
判断一个数是否是素数
author: gxcuizy
date: 2018-10-18
"""

# 程序主入口
if __name__ == '__main__':
    # 接收一个整数
    number = int(input('请输入一个整数：'))
    # 中间整数
    number_center = int(number / 2)
    # 最小数只能为2以上
    start = 2
    # 是否为素数
    is_prime = True
    # 循环整除中间数以下的数字
    while start <= number_center:
        if number % start == 0:
            is_prime = False
            break
        start += 1

    # 结果输出
    if is_prime:
        print(str(number) + '是素数')
    else:
        print(str(number) + '不是素数')
