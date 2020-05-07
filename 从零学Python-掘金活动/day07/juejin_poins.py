#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requests获取掘金沸点数据（用户信息，沸点内容和图片）
author: gxcuizy
date: 2018-10-21
"""

import os
import requests
from urllib import parse


def get_poins(url):
    """获取沸点的Json数据"""
    request = requests.get(url)
    poins = request.json()
    return poins


def deal_poins(poins_list):
    """处理沸点的信息"""
    # 循环沸点列表
    for poin_info in poins_list:
        # 沸点对象ID
        object_id = poin_info['objectId']
        # 创建文件夹
        make_dir(object_id)

        # 沸点内容
        content = poin_info['content']
        # 沸点内容存到txt文件中
        write_content(object_id, content)

        # 用户头像图片URL
        user_avatar = poin_info['user']['avatarLarge']
        # 保存用户头像
        save_avatar(object_id, user_avatar)

        # 沸点图片的list
        pictures = poin_info['pictures']
        # 保存沸点图片
        save_picture(object_id, pictures)


def make_dir(object_id):
    """创建文件夹"""
    dir_path = os.path.join('.', object_id)
    # 判断文件夹是否存在，不存在则创建
    exists_result = os.path.exists(dir_path)
    if not exists_result:
        os.mkdir(dir_path)


def write_content(object_id, content):
    """保存沸点内容"""
    # 拼接文件路径
    path = os.path.join('.', object_id)
    file_name = 'content.txt'
    file_path = os.path.join(path, file_name)
    # 内容写入txt文件
    print('开始写入文件：' + file_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        print('写入完毕！')


def save_avatar(object_id, pictures):
    """下载用户头像"""
    # 拼接图片路径
    path = os.path.join('.', object_id)
    # 图片名称
    img_name = 'avatar.jpg'
    img_path = os.path.join(path, img_name)
    print('开始下载图片:' + img_path)
    with open(img_path, 'wb') as img:
        # 下载图片
        img_re = requests.get(pictures)
        img.write(img_re.content)
        print('下载图片完毕！')


def save_picture(object_id, pictures):
    """下载沸点图片"""
    # 拼接图片路径
    path = os.path.join('.', object_id)
    for picture_url in pictures:
        # 图片名称
        url_data = parse.urlparse(url=picture_url)
        # 图片请求参数
        url_param = parse.parse_qs(url_data.query)
        if url_param:
            # 图片扩展名
            img_ext = url_param['f'][0]
            # 图片路径
            url_path = url_data.path
            # 图片标识ID
            img_id = os.path.split(url_path)[1]
            # 图片名称
            img_name = img_id + '.' + img_ext
            img_path = os.path.join(path, img_name)
            print('开始下载图片:' + img_path)
            with open(img_path, 'wb') as img:
                # 下载图片
                img_re = requests.get(picture_url)
                img.write(img_re.content)
                print('下载图片完毕！')


# 程序主入口
if __name__ == '__main__':
    # 沸点URL
    poin_url = 'https://short-msg-ms.juejin.im/v1/pinList/recommend?uid=59b0de6e5188250f4850ea06&device_id=1540029862766&token=eyJhY2Nlc3NfdG9rZW4iOiJUb0s4SzZPeG44OER4VHZvIiwicmVmcmVzaF90b2tlbiI6ImdEZDhkeDc4RXZZdWZpdWYiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ%3D%3D&src=web&before&limit=30'
    # 获取沸点list
    poin_data = get_poins(poin_url)
    poin_list = poin_data['d']['list']
    # 处理数据
    print('开始处理沸点数据……')
    deal_poins(poin_list)
    print('工作完毕，程序结束！')
