#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
元组的基础语法使用
author: gxcuizy
date: 2018-10-17
"""

# 程序主入口
if __name__ == '__main__':
    # 定义一个元组
    team_tuple = ('da_biao_guo', 'xiao_biao_mei', 'team')
    print(team_tuple)

    # 访问元素值
    # 访问第1个元素
    print(team_tuple[0])
    # 访问第3个元素
    print(team_tuple[2])
    # 访问倒数第2个元素
    print(team_tuple[-2])

    # 定义一个元素值的元组，必须加一个逗号,
    best_language = ('python',)
    print(best_language)

    # 元组长度同样用len()
    tuple_len = len(team_tuple)
    print(tuple_len)
