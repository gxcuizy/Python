#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pickle模块序列化字典的使用
author: gxcuizy
date: 2018-10-25
"""

import pickle

# 程序主入口
if __name__ == '__main__':
    # 定义一个字典
    dict_list = {'python': 99, 'php': 96, 'java': 98}

    # 利用pickle.dumps()序列化字典
    dumps = pickle.dumps(dict_list)
    print(dumps)

    # 利用pickle.loads()反序列化出字典
    loads_list = pickle.loads(dumps)
    print(loads_list)

    # 利用pickle.dump()直接把对象序列化写入文件
    with open('test.txt', 'wb') as file:
        pickle.dump(dict_list, file)

    # 利用pickle.loads()方法反序列化出对象
    with open('test.txt', 'rb') as file:
        load_list = pickle.load(file)
        print(load_list)

