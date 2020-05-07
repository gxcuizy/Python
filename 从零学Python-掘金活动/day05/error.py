#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
异常处理
author: gxcuizy
date: 2018-10-19
"""

# 程序主入口
if __name__ == '__main__':
    # 异常捕获
    try:
        result = 8 / 0
        print(result)
    except Exception as e:
        print('Error')

    # 具体的异常捕获
    try:
        result = 8 / 0
        print(result)
    except ValueError as e:
        print('ValueError')
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
    finally:
        print('finally')

