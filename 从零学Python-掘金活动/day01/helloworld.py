#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hello World
author: gxcuizy
date: 2018-10-15
"""

import random

# 程序主入口
if __name__ == '__main__':
    # 打印
    print('Hello World!')

    # 取4个随机数
    i = 0
    rand_list = []
    while i < 4:
        rand_num = random.randint(0, 499)
        if rand_num not in rand_list:
            rand_list.append(rand_num)
            i += 1
    # 输出组队随机编码
    print(rand_list)
