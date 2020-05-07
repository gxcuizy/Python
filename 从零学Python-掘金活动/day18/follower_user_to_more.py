#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用requests抓取掘金用户的关注者
无限抓取关注者的关注者……
author: gxcuizy
date: 2018-11-06
"""

import requests
import os
import json


class GetFollwerUser(object):
    """抓取掘金用户的关注者"""

    def __init__(self):
        """初始化变量"""
        self.base_url = 'https://follow-api-ms.juejin.im/v1/getUserFollowerList'
        self.user_id = ''
        self.src = 'web'
        self.before = ''
        self.param = {}
        self.user_list = []
        self.json_file = 'follower_user.json'
        self.user_count = 0

    def get_users(self):
        """获取一页的用户"""
        # 请求关注者列表数据
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.param.update({'uid': self.user_id})
        self.param.update({'before': self.before})
        self.param.update({'src': self.src})
        request = requests.get(self.base_url, params=self.param, headers=headers)
        # 用户列表
        follower_list = []
        if request.status_code == 200:
            data = request.json()
            follower_list = data['d']
        return follower_list

    def get_follower_user(self, user_id):
        """获取关注者的关注者"""
        print('开始爬取用户【%s】的关注者' % user_id)
        self.user_id = user_id
        self.before = ''
        while True:
            # 获取关注者，无关注者，则停止爬取
            followers = self.get_users()
            if not followers:
                break
            # 处理数据
            for follower_info in followers:
                # 获取用户ID和昵称，存入json
                user_info = {}
                object_id = follower_info['follower']['objectId']
                user_info.update({'user_id': object_id})
                user_info.update({'user_name': follower_info['follower']['username']})
                print('爬取到的关注者-%s' % user_info)
                # 用户存入json
                user_list = self.read_write_by_json([])
                # 关注者的所有关注者
                if user_info not in user_list:
                    self.user_count += 1
                    # 爬取关注者的关注者
                    self.read_write_by_json(user_info)
                    self.get_follower_user(object_id)
                # 更新下一页的before值
                self.before = follower_info['createdAtString']
        print('爬取结束！')

    def read_write_by_json(self, data):
        """读写json文件"""
        if not os.path.exists(self.json_file):
            # 写文件
            with open(self.json_file, 'w', encoding='utf-8') as write_file:
                json.dump([], write_file, ensure_ascii=False)
        # 读文件
        with open(self.json_file, 'r', encoding='utf-8') as read_file:
            data_list = json.load(read_file)
            if data and data not in data_list:
                data_list.append(data)
                # 写文件
                with open(self.json_file, 'w', encoding='utf-8') as write_file:
                    json.dump(data_list, write_file, ensure_ascii=False)
        return data_list

    def run(self, user_id):
        """开始爬取"""
        print('开始爬取关注者-%s' % user_id)
        self.user_id = user_id
        while True:
            # 获取关注者，无关注者，则停止爬取
            followers = self.get_users()
            if not followers:
                break
            # 处理数据
            for follower_info in followers:
                # 获取用户ID和昵称，存入json
                user_info = {}
                object_id = follower_info['follower']['objectId']
                user_info.update({'user_id': object_id})
                user_info.update({'user_name': follower_info['follower']['username']})
                print('爬取到的关注者-%s' % user_info)
                user_list = self.read_write_by_json([])
                if user_info not in user_list:
                    self.user_count += 1
                    # 爬取关注者的关注者
                    # 用户存入json
                    self.read_write_by_json(user_info)
                    self.get_follower_user(object_id)
                # 更新下一页的before值
                self.user_id = user_id
                self.before = follower_info['createdAtString']
        print('爬取结束，用户总数【%s】' % self.user_count)


# 程序主入口
if __name__ == '__main__':
    juejin_user_id = '59b0de6e5188250f4850ea06'
    follower = GetFollwerUser()
    follower.run(juejin_user_id)
