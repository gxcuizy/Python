#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
下载MP4、MP3、Image文件操作
author: gxcuizy
date: 2018-10-25
"""

import os
import requests


def dl_video(url):
    """下载MP4等视频文件"""
    request = requests.get(url)
    if request.status_code == 200:
        base_name = os.path.basename(url)
        print('正在下载视频-%s' % base_name)
        with open(base_name, 'wb') as video:
            for content in request.iter_content(10000):
                video.write(content)
            print('视频下载完毕！')
    else:
        print('视频下载路径错误！')


def dl_music(url):
    """下载MP3等音乐文件"""
    request = requests.get(url)
    if request.status_code == 200:
        base_name = os.path.basename(url)
        print('正在下载音乐-%s' % base_name)
        with open(base_name, 'wb') as music:
            for content in request.iter_content(10000):
                music.write(content)
            print('音乐下载完毕！')
    else:
        print('音乐下载路径错误！')


def dl_img(url):
    """下载图片文件"""
    request = requests.get(url)
    if request.status_code == 200:
        base_name = os.path.basename(url)
        print('正在下载图片-%s' % base_name)
        with open(base_name, 'wb') as img:
            img.write(request.content)
            print('图片下载完成！')
    else:
        print('图片下载路径错误！')


# 程序主入口
if __name__ == '__main__':
    # 下载视频文件
    video_url = 'http://www.runoob.com/try/demo_source/movie.mp4'
    dl_video(video_url)
    # 下载音乐文件
    music_url = 'https://m10.music.126.net/20181025202316/08d508c1bbefedd0b277dba211989ccc/ymusic/0291/8459/991f/3f72ad6646ff36803996bba499bb33e9.mp3'
    dl_music(music_url)
    # 下载图片文件
    img_url = 'http://img.shujuren.org/pictures/GB/57ff13a89b3b8.png'
    dl_img(img_url)
