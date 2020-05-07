#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
判断列表的所有数是否是素数（函数式）
将所有素数的元素打印为字典（函数式）
author: gxcuizy
date: 2018-10-19
"""


def is_prime(num_list):
    """判断列表的数字是否为素数"""
    prime_result = []
    for number_val in num_list:
        # 判断是否为素数
        prime_status = get_is_prime(number_val)
        # 结果添加到列表中
        prime_result.append(prime_status)
    return prime_result


def get_is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
        # 中间整数
    number_center = int(num / 2)
    # 最小数只能为2以上
    start = 2
    # 是否为素数
    prime_status = True
    # 循环整除中间数以下的数字
    while start <= number_center:
        # 能整除，不是素数
        if num % start == 0:
            prime_status = False
            break
        start += 1
    return prime_status


def print_dict(num_dict):
    """打印字典的key、value信息"""
    for key, value in num_dict.items():
        print(str(key) + '是素数吗？：' + str(value))


def get_prime(num_dict):
    """获取字典里所有的素数"""
    prime_dict = {}
    for key, value in num_dict.items():
        if value:
            prime_dict.update({key: key})
    return prime_dict


# 程序主入口
if __name__ == '__main__':
    # 数字列表
    number = [2, 6, 7, 9, 17]
    # 判断素数结果
    result = is_prime(number)
    # 数字和素数结果合并为字典
    number_dict = dict(zip(number, result))
    # 打印结果
    print_dict(number_dict)
    # 获取素数元素的字典
    prime = get_prime(number_dict)
    # 打印素数字典
    print(prime)
