#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
字典的基础使用和练习
author: gxcuizy
date: 2018-10-18
"""

# 程序主入口
if __name__ == '__main__':
    # 定义一个空字典
    dict_none = {}
    print(dict_none)

    # 定义一个非空字典
    score_dict = {'math': 96, 'english': 97, 'chinese': 98}
    print(score_dict)

    # 使用使用dict()创建字典
    tuple_math = ('math', '96')
    tuple_english = ('english', '97')
    tuple_chinese = ('chinese', '98')
    dict_a = dict([tuple_math, tuple_english, tuple_chinese])
    print(dict_a)

    # 使用zip()合并两个列表分别作为字典的key和value
    list_key = ['math', 'english', 'chinese']
    list_value = [96, 97, 98]
    score = dict(zip(list_key, list_value))
    print(score)

    # 读取字典的value
    print(score_dict['math'])

    # 修改字典的value
    score_dict['chinese'] = 100
    print(score_dict)

    # keys()获取字典所有的key
    dict_key = score_dict.keys()
    print(dict_key)

    # values()获取字典所有的value
    dict_value = score_dict.values()
    print(dict_value)

    # 使用get()获取key值对应的value
    math_value = score_dict.get('math')
    print(math_value)

    # in 和 not in 判断key在字典中是否存在
    print('math' in score_dict)
    print('history' not in score_dict)

    # 使用items()把字典的对应的key和value组成一个元组返回一个列表
    score_list = score_dict.items()
    print(score_list)

    # 使用copy()复制一个字典
    score_copy = score_dict.copy()
    print(score_copy)

    # 使用clear()清空字典所有元素
    score_copy.clear()
    print(score_copy)

    # pop()删除一个key对应的元素，key存在，返回对应的value，可以指定不存在时的默认返回值
    pop_result = score_dict.pop('english')
    print(pop_result)
    pop_result = score_dict.pop('history', '不存在')
    print(pop_result)

    # 使用update()更新字典，也就是追加元素的意思
    score_dict.update({'history': 95})
    print(score_dict)

    # 使用fromkyes()创建一个新的字典，key来自序列，value来自自定义（默认为None）
    score_new = score_copy.fromkeys([11, 22, 33, 44], 100)
    print(score_new)
