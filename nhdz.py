#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
爬取百度贴吧，段友之家的图片和视频
author: cuizy
time：2018-05-19
"""

import requests
import bs4
import os


def write_file(file_url, file_type):
    """写入文件"""
    res = requests.get(file_url)
    res.raise_for_status()
    # 文件类型分文件夹写入
    if file_type == 1:
        file_folder = 'nhdz\\jpg'
    elif file_type == 2:
        file_folder = 'nhdz\\mp4'
    else:
        file_folder = 'nhdz\\other'
    folder = os.path.exists(file_folder)
    # 文件夹不存在，则创建文件夹
    if not folder:
        os.makedirs(file_folder)
    # 打开文件资源，并写入
    file_name = os.path.basename(file_url)
    str_index = file_name.find('?')
    if str_index > 0:
        file_name = file_name[:str_index]
    file_path = os.path.join(file_folder, file_name)
    print('正在写入资源文件：', file_path)
    image_file = open(file_path, 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
    print('写入完成！')


def download_file(web_url):
    """获取资源的url"""
    # 下载网页
    print('正在下载网页： %s...' % web_url)
    result = requests.get(web_url)
    soup = bs4.BeautifulSoup(result.text, "html.parser")
    # 查找图片资源
    img_list = soup.select('.vpic_wrap img')
    if img_list == []:
        print('未发现图片资源！')
    else:
        # 找到资源，开始写入
        for img_info in img_list:
            file_url = img_info.get('bpic')
            write_file(file_url, 1)
    # 查找视频资源
    video_list = soup.select('.threadlist_video a')
    if video_list == []:
        print('未发现视频资源！')
    else:
        # 找到资源，开始写入
        for video_info in video_list:
            file_url = video_info.get('data-video')
            write_file(file_url, 2)
    print('下载资源结束：', web_url)
    next_link = soup.select('#frs_list_pager .next')
    if next_link == []:
        print('下载资料结束！')
    else:
        url = next_link[0].get('href')
        download_file('https:' + url)


# 主程序入口
if __name__ == '__main__':
    web_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=段友之家'
    download_file(web_url)
