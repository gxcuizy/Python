#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常见的内建模块练习之urllib
author: gxcuizy
date: 2018-10-30
"""

from urllib import request

# 程序主入口
if __name__ == '__main__':
    # 数据url
    url = 'https://api.douban.com/v2/book/2129650'
    # 发送请求
    r = request.urlopen(url)
    # 获取请求状态
    print(r.status)
    # 请求头
    print(r.getheaders())
    # 请求数据
    data = r.read()
    print(data)

    # 发送POST请求的话，data参数必须是bytes类型

    # 最后我只想说，还是第三方的requests好用，打死不用这个内置的
