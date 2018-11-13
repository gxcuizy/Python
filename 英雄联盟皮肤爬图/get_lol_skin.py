#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
抓取英雄联盟英雄全皮肤
author: gxcuizy
date: 2018-11-13
"""

import requests
import json
from urllib import parse
import os


class GetLolSkin(object):
    """抓取LOL英雄皮肤"""

    def __init__(self):
        """初始化变量"""
        self.hero_url = 'https://lol.qq.com/biz/hero/champion.js'
        self.hero_detail_url = 'http://lol.qq.com/biz/hero/'
        self.skin_folder = 'skin'
        self.skin_url = 'https://ossweb-img.qq.com/images/lol/web201310/skin/big'

    @staticmethod
    def get_html(url):
        """下载html"""
        request = requests.get(url)
        request.encoding = 'gbk'
        if request.status_code == 200:
            return request.text
        else:
            return "{}"

    def get_hero_list(self):
        """获取英雄的完整信息列表"""
        hero_js = self.get_html(self.hero_url)
        # 删除左右的多余信息，得到json数据
        out_left = "if(!LOLherojs)var LOLherojs={};LOLherojs.champion="
        out_right = ';'
        hero_list = hero_js.replace(out_left, '').rstrip(out_right)
        return json.loads(hero_list)

    def get_hero_info(self, hero_id):
        """获取英雄的详细信息"""
        # 获取js详情
        detail_url = parse.urljoin(self.hero_detail_url, hero_id + '.js')
        detail_js = self.get_html(detail_url)
        # 删除左右的多余信息，得到json数据
        out_left = "if(!herojs)var herojs={champion:{}};herojs['champion'][%s]=" % hero_id
        out_right = ';'
        hero_info = detail_js.replace(out_left, '').rstrip(out_right)
        return json.loads(hero_info)

    def download_skin_list(self, skin_list, hero_name):
        """下载皮肤列表"""
        # 循环下载皮肤
        for skin_info in skin_list:
            # 拼接图片名字
            if skin_info['name'] == 'default':
                skin_name = '默认皮肤'
            else:
                if ' ' in skin_info['name']:
                    name_info = skin_info['name'].split(' ')
                    skin_name = name_info[0]
                else:
                    skin_name = skin_info['name']
            hero_skin_name = hero_name + '-' + skin_name + '.jpg'
            self.download_skin(skin_info['id'], hero_skin_name)

    def download_skin(self, skin_id, skin_name):
        """下载皮肤图片"""
        # 下载图片
        img_url = self.skin_url + skin_id + '.jpg'
        request = requests.get(img_url)
        if request.status_code == 200:
            print('downloading……%s' % skin_name)
            img_path = os.path.join(self.skin_folder, skin_name)
            with open(img_path, 'wb') as img:
                img.write(request.content)
        else:
            print('img error!')

    def make_folder(self):
        """初始化，创建图片文件夹"""
        if not os.path.exists(self.skin_folder):
            os.mkdir(self.skin_folder)

    def run(self):
        # 获取英雄列表信息
        hero_json = self.get_hero_list()
        hero_keys = hero_json['keys']
        # 循环遍历英雄
        for hero_id, hero_code in hero_keys.items():
            hero_name = hero_json['data'][hero_code]['name']
            hero_info = self.get_hero_info(hero_id)
            if hero_info:
                skin_list = hero_info['result'][hero_id]['skins']
                # 下载皮肤
                self.download_skin_list(skin_list, hero_name)
            else:
                print('英雄【%s】的皮肤获取有问题……' % hero_name)


# 程序执行入口
if __name__ == '__main__':
    lol = GetLolSkin()
    # 创建图片存储文件
    lol.make_folder()
    # 执行脚本
    lol.run()
