#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
列表的基础语法使用
author: gxcuizy
date: 2018-10-17
"""

# 程序主入口
if __name__ == '__main__':
    # 列表的定义
    team_list = ['da_biao_guo', 'xiao_biao_mei', 'team']
    print(team_list)

    # 用len()输出列表长度
    list_len = len(team_list)
    print(list_len)

    # 访问列表的元素值
    # 访问第1个元素
    print(team_list[0])
    # 访问第3个元素
    print(team_list[2])
    # 访问倒数第2个数
    print(team_list[-2])

    # 追加元素至末尾
    team_list.append('python')
    print(team_list)

    # 插入元素到指定的位置
    team_list.insert(3, 'learning')
    print(team_list)

    # 删除末尾的一个元素
    team_list.pop()
    print(team_list)

    # 删除指定位置的一个元素
    team_list.pop(2)
    print(team_list)

    # 更新某个元素值
    team_list[1] = '小表妹'
    print(team_list)

    # 列表元素值类型，可以不同
    team_list[0] = ['da', 'biao', 'guo']
    team_list[2] = 666
    print(team_list)
