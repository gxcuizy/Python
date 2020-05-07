#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
json模块序列化字典的使用
author: gxcuizy
date: 2018-10-25
"""

import json

# 程序主入口
if __name__ == '__main__':
    # 定义一个字典
    dict_list = {'python': 99, 'php': 96, 'java': 98}

    # dumps()序列化字典得到一个字符串
    json_str = json.dumps(dict_list)
    print('序列化的结果：%s' % json_str)

    # loads()反序列化字符串出字典
    loads_list = json.loads(json_str)
    print('序列化的结果：%s' % loads_list)

    # dump()直接把对象序列化写入文件
    with open('test.json', 'w') as file:
        json.dump(dict_list, file)

    # loads()方法反序列化出字典
    with open('test.json', 'r') as file:
        load_list = json.load(file)
        print('读取文件反序列化的结果：%s' % load_list)

