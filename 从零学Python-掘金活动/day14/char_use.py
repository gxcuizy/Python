#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常见的内建模块练习之base64、struct
author: gxcuizy
date: 2018-10-30
"""

import base64
import struct

# 程序主入口
if __name__ == '__main__':
    # Base64是一种用64个字符来表示任意二进制数据的方法。python使用base64模块可以直接进行base64的编解码
    # base64提供了b64encode()的编码方法
    test_str = b'binary\x00string'
    encode_str = base64.b64encode(test_str)
    print(encode_str)

    # 同时base64提供了b64decode()的解码方法
    decode_str = base64.b64decode(encode_str)
    print(decode_str)

    # struct模块可以解决bytes和其他二进制数据类型的转换。
    # struct模块的pack()方法可以把任意数据类型变为bytes字节型
    test_number = 888888
    i_number = struct.pack('>I', test_number)
    print(i_number)

    # struct的unpack()方法可以把bytes变成相应的数据类型
    un_bytes = b'\xf0\xf0\xf0\xf0\x80\x80'
    i_h_number = struct.unpack('>IH', un_bytes)
    print(i_h_number)
