#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
if、while逻辑判断的用法
author: gxcuizy
date: 2018-10-18
"""

# 程序主入口
if __name__ == '__main__':
    # 简单if
    name = 'big_brother'
    if name == 'da_biao_guo':
        print('Please take me fly!')

    # if……else 的用法
    if name == 'da_biao_guo':
        print('Please take me fly!')
    else:
        print('Please take us fly!')

    # if……elif……else 的用法
    if name == 'da_biao_guo':
        print('Please take me fly!')
    elif name == 'xiao_biao_mei':
        print('Please take us fly!')
    else:
        print('Please take you fly!')

    # while的用法-计算100以内所有偶数的和
    sum = 0
    n = 0
    while n <= 100:
        if n % 2 == 0:
            sum += n
        n += 1
    print(sum)
