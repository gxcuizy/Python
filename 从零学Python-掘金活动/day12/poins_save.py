#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
掘金沸点内容，各种方式存储练习
author: gxcuizy
date: 2018-10-24
"""

import requests
import json
import csv
import openpyxl


def get_poins(url):
    """请求沸点数据"""
    request = requests.get(url)
    # 判断请求结果，返回数据
    if request.status_code == 200:
        result = request.json()
        return result['d']['list']
    else:
        return []


def save_by_json(data):
    """通过json格式存储"""
    print('沸点json格式存储……')
    with open('poins.json', 'w') as file:
        json.dump(data, file)
        print('存储完毕！')


def save_by_excel(data):
    """通过xlsx表格格式存储"""
    print('沸点xlsx格式存储……')
    wb = openpyxl.Workbook()
    # 获取默认工作表
    sheet = wb.active
    # 写入表头
    print('写入表头')
    poins_header = ['objectId', 'urlTitle', 'content', 'commentCount', 'likedCount', 'username', 'userCompany',
                    'userTitle', 'uerRole', 'updatedAt', 'isTopicRecommend']
    sheet.append(poins_header)
    # 写入行数据，逐行写入
    save_list = get_data(data)
    for data in save_list:
        if data:
            print('正在写入行 %s' % data)
            sheet.append(data)
    # 保存并生成表格
    wb.save('poins.xlsx')


def save_by_csv(data):
    """通过csv格式存储"""
    print('沸点csv格式存储……')
    save_list = get_data(data)
    poins_header = ['objectId', 'urlTitle', 'content', 'commentCount', 'likedCount', 'username', 'userCompany',
                    'userTitle', 'uerRole', 'updatedAt', 'isTopicRecommend']
    # 打开DictWriter文件对象
    with open('poins.csv', 'w', encoding='utf-8') as file:
        f_csv = csv.writer(file)
        # 写入header标题
        print('正在写入csv表头……')
        f_csv.writerow(poins_header)
        # 写入多行数据
        print('正在写入行数据……')
        f_csv.writerows(save_list)
        print('写入完成！')


def get_data(data):
    """格式化存储格式化"""
    poins = []
    for poin in data:
        poin_info = []
        poin_info.append(poin['objectId'])
        poin_info.append(poin['urlTitle'])
        poin_info.append(poin['content'])
        poin_info.append(poin['commentCount'])
        poin_info.append(poin['likedCount'])
        poin_info.append(poin['user']['username'])
        poin_info.append(poin['user']['company'])
        poin_info.append(poin['user']['jobTitle'])
        poin_info.append(poin['user']['role'])
        poin_info.append(poin['updatedAt'])
        poin_info.append(poin['isTopicRecommend'])
        poins.append(poin_info)
    return poins


# 程序入住口
if __name__ == '__main__':
    # 沸点数据url
    poins_url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?src=web&before&limit=20'
    poin_list = get_poins(poins_url)
    # 如果请求不到数据，则为异常，不继续执行
    if not poin_list:
        exit()
    # json格式存储
    save_by_json(poin_list)
    # CSV表格存储
    save_by_csv(poin_list)
    # Excel表格存储
    save_by_excel(poin_list)
