#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
国家地理中文网-杂志阅读信息
author: gxcuizy
date: 2018-11-05
"""

import requests
from urllib import parse
import os
from bs4 import BeautifulSoup


class NgChina(object):
    """中国地理中文网图片和主要文字信息"""

    def __init__(self):
        self.domaim = 'http://www.ngchina.com.cn/'
        self.url = 'http://www.ngchina.com.cn/magazine/'
        self.base_folder = 'images'
        self.txt_folder = 'content'

    def get_html(self, web_url):
        """请求获取网页"""
        request = requests.get(web_url)
        request.raise_for_status()
        content = request.content
        return content

    def download_img(self, img_url):
        """下载图片"""
        print('开始下载图片-%s' % img_url)
        base_name = os.path.basename(img_url)
        year = base_name[:4]
        month = base_name[4:6]
        img_folder = os.path.join(self.base_folder, year, month)
        # 文件夹不存在，则创建
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)
        # 保存图片
        with open(os.path.join(img_folder, base_name), 'wb') as img:
            img_r = requests.get(img_url)
            img.write(img_r.content)
        print('图片下载结束！')

    def get_more_detail(self, more_url):
        """获取每期的更多详情"""
        print('正在获取更多信息-%s' % more_url)
        html = self.get_html(more_url)
        soup = BeautifulSoup(html, 'lxml')
        div_list = soup.select('.big_txt')
        print('正在写入更多信息……')
        for big_txt in div_list:
            # 获取标题和简述信息
            h4_text = big_txt.find(name='h4').text
            p_text = big_txt.find(name='p').text
            file_name = parse.urlparse(more_url).path.strip('/').replace('/', '-') + '.txt'
            self.save_by_txt(h4_text, p_text, file_name)
        print('更多信息写入完毕！')

    def save_by_txt(self, title, content, file_name):
        # 文件夹不存在，则创建
        if not os.path.exists(self.txt_folder):
            os.mkdir(self.txt_folder)
        """写入文本信息"""
        with open(os.path.join(self.txt_folder, file_name), 'a', encoding='utf-8') as txt:
            txt.write(title + '\n')
            txt.write(content + '\n')
            txt.write('--------------------------------------------------------------------------------' + '\n\n')

    def run(self):
        """程序执行入口"""
        print('开始执行……')
        html = self.get_html(self.url)
        soup = BeautifulSoup(html, 'lxml')
        div_list = soup.select('.img_list')
        for img_box in div_list:
            # 查找图片元素，并下载
            img_element = img_box.find(name='img')
            img_src = img_element.attrs['src']
            self.download_img(img_src)
            # 查找文本信息
            more_element = img_box.find(name='p').find(name='a')
            more_href = parse.urljoin(self.domaim, more_element.attrs['href'])
            self.get_more_detail(more_href)


# 程序主入口
if __name__ == '__main__':
    # 实例化执行
    ng = NgChina()
    ng.run()
