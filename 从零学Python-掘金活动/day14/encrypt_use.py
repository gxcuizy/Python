#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常见的内建模块练习之hashlib、hmac
author: gxcuizy
date: 2018-10-30
"""

import hashlib
import hmac

# 程序主入口
if __name__ == '__main__':
    # hashlib提供了常见的摘要算法，如MD5，SHA1……
    # 调用md5()方法进行加密字符串操作
    md5 = hashlib.md5()
    test_str = 'hello python'
    # 可以分块多次调用update()
    md5.update(test_str.encode('utf-8'))
    print(md5.hexdigest())

    # 调用sha1()方法进行加密字符串操作
    md5 = hashlib.sha1()
    test_str = 'hello python'
    md5.update(test_str.encode('utf-8'))
    print(md5.hexdigest())

    # Python自带的hmac模块可以实现标准的Hmac算法
    # md5方式加密字符串，key必须是bytes字节型
    key = b'test'
    hm = hmac.new(key, test_str.encode('utf-8'), digestmod='md5')
    print(hm.hexdigest())

    # sha1加密
    hm = hmac.new(key, test_str.encode('utf-8'), digestmod='sha1')
    print(hm.hexdigest())
