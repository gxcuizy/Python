#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据类型和变量的基础使用
author: gxcuizy
date: 2018-10-17
"""

# 程序主入口
if __name__ == '__main__':
    # 整型
    int_value = 666
    print(int_value)

    # 浮点数
    float_value = 6.6666
    print(float_value)

    # 字符串
    str_value = 'hello world!'
    print(str_value)
    # 转移字符串
    str_escape_value = '这是转义的\'hello world!\''
    print(str_escape_value)

    # 布尔值
    # 布尔值只有True、False两种值
    bool_true_value = True
    print(bool_true_value)
    bool_false_value = False
    print(bool_false_value)

    # 空值
    none_value = None
    print(none_value)

    # 常量-变量名全部大写
    CONS_VALUE = '大表锅'
    print(CONS_VALUE)
