#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
抓取王者荣耀皮肤
author: gxcuizy
date: 2018-11-06
"""

import requests
from bs4 import BeautifulSoup
from urllib import parse
import os


class Skin(object):
    def __init__(self):
        # 英雄的json数据
        self.hero_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        # 英雄详细页的通用url前缀信息
        self.base_url = 'https://pvp.qq.com/web201605/herodetail/'
        # 英雄详细页url后缀信息
        self.detail_url = ''
        # 图片存储文件夹
        self.img_folder = 'skin'
        # 图片url的通用前缀
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
        # 图片url的后缀信息
        self.skin_detail_url = ''

    def get_hero(self):
        """获取英雄的json数据"""
        request = requests.get(self.hero_url)
        hero_list = request.json()
        return hero_list

    def get_hero_skin(self, hero_name, hero_no):
        """获取详细页英雄皮肤展示的信息，并爬图"""
        url = parse.urljoin(self.base_url, self.detail_url)
        request = requests.get(url)
        request.encoding = 'gbk'
        html = request.text
        # 获取皮肤信息的节点
        soup = BeautifulSoup(html, 'lxml')
        skip_list = soup.select('.pic-pf-list3')
        for skin_info in skip_list:
            # 获取皮肤名称
            img_names = skin_info.attrs['data-imgname']
            name_list = img_names.split('|')
            skin_no = 1
            # 循环下载皮肤图片
            for skin_name in name_list:
                self.skin_detail_url = '%s/%s-bigskin-%s.jpg' % (hero_no, hero_no, skin_no)
                skin_no += 1
                img_name = hero_name + '-' + skin_name + '.jpg'
                self.download_skin(img_name)

    def download_skin(self, img_name):
        """下载皮肤图片"""
        img_url = parse.urljoin(self.skin_url, self.skin_detail_url)
        request = requests.get(img_url)
        if request.status_code == 200:
            print('download-%s' % img_name)
            img_path = os.path.join(self.img_folder, img_name)
            with open(img_path, 'wb') as img:
                img.write(request.content)
        else:
            print('img error!')

    def make_folder(self):
        """创建图片存储文件夹"""
        if not os.path.exists(self.img_folder):
            os.mkdir(self.img_folder)

    def run(self):
        """脚本执行入口"""
        self.make_folder()
        hero_list = self.get_hero()
        for hero in hero_list:
            hero_no = str(hero['ename'])
            self.detail_url = hero_no + '.shtml'
            hero_name = hero['cname']
            self.get_hero_skin(hero_name, hero_no)


# 程序执行入口
if __name__ == '__main__':
    skin = Skin()
    skin.run()
