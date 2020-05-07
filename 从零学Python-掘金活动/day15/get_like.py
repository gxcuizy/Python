#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用bs4爬取博客的猜你喜欢内容
author: gxcuizy
date: 2018-10-31
"""

import requests
from bs4 import BeautifulSoup
from urllib import parse
import os
import json


class GuessYourLike(object):
    """爬取博客，猜你喜欢的图片和标题等信息"""
    url = ''

    def __init__(self, url):
        self.url = url

    def get_html(self):
        """请求博客页面html"""
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        request = requests.get(url=self.url, headers=header)
        html = False
        if request.status_code == 200:
            html = request.content
        return html

    def get_img_name(self, url):
        """获取图片文件名"""
        url_data = parse.urlparse(url=url)
        # 图片参数
        param = parse.parse_qs(url_data.query)
        img_src = param['src'][0]
        print('开始下载图片 %s' % img_src)
        base_name = os.path.basename(img_src)
        return base_name

    def download_img(self, url):
        """下载图片"""
        # 获取图片文件名
        base_name = self.get_img_name(url)
        img_folder = 'images'
        if not os.path.exists(img_folder):
            os.mkdir(img_folder)
        img_path = os.path.join(img_folder, base_name)
        # 下载图片保存
        request = requests.get(url)
        dl_status = False
        if request.status_code == 200:
            with open(img_path, 'wb') as file:
                file.write(request.content)
                dl_status = True
                print('下载完毕！')
        return dl_status

    def save_by_json(self, data):
        """json格式保存喜欢信息"""
        print('开始存储json数据……')
        with open('data.json', 'w') as file:
            json.dump(data, file)
        print('存储数据完毕！')

    def run(self):
        """执行入口"""
        print('程序开始执行……')
        html = self.get_html()
        like_list = []
        if html:
            soup = BeautifulSoup(html, 'lxml')
            like_div = soup.find(class_='d_postlist')
            li_list = like_div.find_all(name='li')
            for li_info in li_list:
                like_info = {}
                # 文章链接
                article_href = li_info.a.attrs['href']
                # 文章标题
                article_title = li_info.find(class_='text').string
                # 文章发布时间和评论数
                muted_info = li_info.find_all(class_='muted')
                article_date = muted_info[0].string
                article_comment = muted_info[1].string
                # 文章头图
                article_img = li_info.img.attrs['src']
                # 信息存入json
                like_info.update({'href': article_href})
                like_info.update({'title': article_title})
                like_info.update({'date': article_date})
                like_info.update({'comment': article_comment})
                like_info.update({'img': article_img})
                like_list.append(like_info)
                # 下载图片
                self.download_img(article_img)
            # 猜你喜欢信息，存入json文件
            self.save_by_json(like_list)
        else:
            print('网络错误，请求失败！')
        print('程序执行完毕！')


# 程序主入口
if __name__ == '__main__':
    # 实例化
    blog_url = 'https://cuiqingcai.com/5548.html'
    gl = GuessYourLike(blog_url)
    # 执行脚本
    gl.run()
