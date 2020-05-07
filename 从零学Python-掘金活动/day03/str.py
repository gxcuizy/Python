#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
字符串的基础语法使用
author: gxcuizy
date: 2018-10-17
"""

# 程序主入口
if __name__ == '__main__':
    # 定义一个字符串
    str_value = '这是字符串string'
    print(str_value)

    # 字符串utf-8编码
    str_encode = str_value.encode('utf-8')
    print(str_encode)

    # 字符串utf-8解码
    str_decode = str_encode.decode('utf-8')
    print(str_decode)

    # 统计字符串的长度
    str_len = len(str_value)
    print(str_len)

    # 格式化字符串
    str_format = '这是字符串格式化： %s' % str_value
    print(str_format)
    # 格式化整数
    int_value = 666
    int_format = '这是整数格式化： %d' % int_value
    print(int_format)
    # 格式化浮点数
    float_value = 666.66
    float_format = '这是浮点数格式化： %f' % float_value
    print(float_format)
    # 综合使用
    format_value = '%s %d + %f 的值' % ('计算', 6, 6.66)
    print(format_value)

    # 格式化字符串format()的用法
    format_fun_value = '{0}的{1}成绩是{2}分'.format('小明', '数学', 99)
    print(format_fun_value)
