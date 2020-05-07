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
        self.hero_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.base_url = 'https://pvp.qq.com/web201605/herodetail/'
        self.detail_url = ''
        self.img_folder = 'skin'
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
        self.skin_detail_url = '116/116-bigskin-1.jpg'

    def get_hero(self):
        request = requests.get(self.hero_url)
        hero_list = request.json()
        return hero_list

    def get_hero_skin(self, hero_name, hero_no):
        url = parse.urljoin(self.base_url, self.detail_url)
        request = requests.get(url)
        request.encoding = 'gbk'
        html = request.text
        soup = BeautifulSoup(html, 'lxml')
        skip_list = soup.select('.pic-pf-list3')
        for skin_info in skip_list:
            img_names = skin_info.attrs['data-imgname']
            name_list = img_names.split('|')
            skin_no = 1
            for skin_name in name_list:
                self.skin_detail_url = '%s/%s-bigskin-%s.jpg' % (hero_no, hero_no, skin_no)
                skin_no += 1
                img_name = hero_name + '-' + skin_name + '.jpg'
                self.download_skin(img_name)

    def download_skin(self, img_name):
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
        if not os.path.exists(self.img_folder):
            os.mkdir(self.img_folder)

    def run(self):
        self.make_folder()
        hero_list = self.get_hero()
        for hero in hero_list:
            hero_no = str(hero['ename'])
            self.detail_url = hero_no + '.shtml'
            hero_name = hero['cname']
            self.get_hero_skin(hero_name, hero_no)


if __name__ == '__main__':
    skin = Skin()
    skin.run()
