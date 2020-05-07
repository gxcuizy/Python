#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
面向对象编程的使用和练习
author: gxcuizy
date: 2018-10-29
"""

import requests
import json


class Poins():
    """定义一个沸点类，存储沸点json信息"""

    def __init__(self, url):
        """初始化属性"""
        self.url = url

    def get_poins(self):
        """请求沸点数据"""
        request = requests.get(self.url)
        # 判断请求结果，返回数据
        if request.status_code == 200:
            result = request.json()
            return result['d']['list']
        else:
            return []

    def save_by_json(self):
        """通过json格式存储"""
        # 请求沸点数据
        data = self.get_poins()
        print('沸点json格式存储……')
        with open('poins.json', 'w') as file:
            json.dump(data, file)
            print('存储完毕！')


# 程序主入口
if __name__ == '__main__':
    # class关键字可以创建一个类
    # 类有成员属性和成员方法；在类里面，通过self.来调用；在类外面，通过实例化来调用
    # 类的__init__方法，可以初始化类的属性
    # 其中，类的方法的第一个参数，永远是self
    # 类是可以继承的，默认继承object

    # 定义一个沸点类
    poin_url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?src=web&before&limit=20'
    poin = Poins(poin_url)
    # 调用实例化方法
    poin.save_by_json()
