#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
正则表达式的基本学习和使用
author: gxcuizy
date: 2018-10-29
"""

import re


def match_phone(number):
    """匹配手机号码"""
    match = r'^1\d{10}$'
    result = re.match(match, number)
    # 匹配结果，是否为真
    match_status = False
    if result:
        match_status = True
    return match_status


def match_id_card(number):
    """匹配身份证号码"""
    match = '^\d{17}[\d|x|X]{1}$'
    result = re.match(match, number)
    # 匹配结果，是否为真
    match_status = False
    if result:
        match_status = True
    return match_status


# 程序主入口
if __name__ == '__main__':
    # \d 匹配一个数字
    # \w 匹配数字一个数字或者字母
    # * 星号可以表示任意字符（0个或者0个以上）
    # + 加号表示至少一个字符
    # ? 问号表示0个或者1个字符
    # {n} 表示n个字符
    # {n,m} 表示n至m个字符
    # \s 表示一个空格
    # [] 表示范围，例如[1,9]表示数字1至9
    # | 竖线表示或，例如 1|2 表示匹配到1或者2都成立
    # ^ 表示正则表达式匹配的开头，例如 ^python 表示这个字符串必须以python作为开始
    # $ 表示正则表达式的结束，例如 python$ 表示这个字符串必须以python作为结束
    # \ 特殊字符串，使用反斜线\进行转移
    # r 为了不考虑转移，需要使用r开始的前缀，例如 r'010-10010010'的-就不用转义了
    # 使用正则表达式时，需要使用re模块，其中re模块的match()可以判定是否匹配正则表达式，匹配则返回Match对象，否则返回None

    # 测试匹配hello
    test_str = 'hello python'
    match_str = r'^hello'
    if re.match(match_str, test_str):
        print('success')
    else:
        print('fail')

    # re模块的split()方法可以切分字符串，而且比系统的split()方法要灵活
    split_str = 'a b,c,d,e'
    split_list = re.split(r'[\s\,]+', split_str)
    print(split_list)

    # 匹配则返回Match对象，可以使用group()方法提取子串
    # 其中，group(0)永远是表示源字符串，group(1)、group(2)……表示第1、2……个子串
    match_group = re.match(match_str, test_str)
    print(match_group.group(0))

    groups = re.match(match_str, test_str).groups()
    print(groups)

    # 简单校验手机号码
    phone_number = input('请输入一个手机号码：')
    is_phone = match_phone(phone_number)
    if is_phone:
        print('这是手机号码')
    else:
        print('这不是手机号码')

    # 简单校验身份证号码
    card_number = input('请输入一个身份证号码；')
    is_card = match_id_card(card_number)
    if is_card:
        print('这是身份证号码')
    else:
        print('这不是身份证号码')
