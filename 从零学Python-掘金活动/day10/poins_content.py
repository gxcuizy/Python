#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requests获取掘金沸点内容
author: gxcuizy
date: 2018-10-24
"""

import requests


def get_poins(url):
    """获取掘金沸点数据"""
    request = requests.get(url)
    result = request.json()
    return result


if __name__ == '__main__':
    poins_url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=59b0de6e5188250f4850ea06&device_id=1540029862766&token=eyJhY2Nlc3NfdG9rZW4iOiJUb0s4SzZPeG44OER4VHZvIiwicmVmcmVzaF90b2tlbiI6ImdEZDhkeDc4RXZZdWZpdWYiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D&src=web&before&limit=30'
    poins_result = get_poins(poins_url)
    poin_list = poins_result['d']['list']
    print('开始写入沸点内容……')
    with open('poins.txt', 'w', encoding='utf-8') as file:
        for poin in poin_list:
            user_name = poin['user']['username']
            print('写入【%s】发布的沸点……' % user_name)
            content = poin['content']
            file.write('沸点用户：' + user_name + '\n')
            file.write(content + '\n\n')
            file.write('************************************************************************************************************************' + '\n\n')
            print('写入完成！')
    print('全部写入完成！')
