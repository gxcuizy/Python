#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用BeautifulSoup爬取省、市、区、街道、办事处五级地址
author: gxcuizy
date: 2018-11-01
"""

import requests
from bs4 import BeautifulSoup
from urllib import parse
import json
import os
from datetime import datetime
import threading


class GetCity(object):
    """爬取国家统计局省、市、区/县、乡/镇 四级地址"""
    # 地址
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'

    def __init__(self):
        """初始化属性"""
        self.json_folder = 'json'
        self.json_file = {'province': 'province.json', 'city': 'city.json', 'county': 'county.json', 'town': 'town.json'}
        self.lock = threading.Lock()

    @staticmethod
    def get_web_html(url):
        """请求html页面信息"""
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        try:
            request = requests.get(url=url, headers=header)
            request.encoding = 'gbk'
            html = request.text
            return html
        except Exception as except_msg:
            print(except_msg)
            return ''

    def get_city(self, origin_url, now_url, origin_code):
        """获取市级地址信息"""
        province_url = parse.urljoin(origin_url, now_url)
        # 解析市级的html
        print('开始解析市级信息……')
        html = self.get_web_html(province_url)
        soup = BeautifulSoup(html, 'lxml')
        city_list = soup.select('.citytr')
        for city_info in city_list:
            a_info = city_info.find_all(name='a')
            city_name = a_info[1].get_text()
            city_code = a_info[0].get_text()
            city_url = a_info[0].attrs['href']
            print(city_name, city_code, city_url)
            # 数据存入字典
            dict_info = {}
            dict_info.update({'name': city_name})
            dict_info.update({'code': city_code})
            dict_info.update({'parent_code': origin_code})
            dict_info.update({'level': 2})
            # 读写json数据
            self.read_write_by_json(dict_info, 'city')
            # 获取县区信息
            self.get_county(province_url, city_url, city_code)
        print('市级解析结束！')

    def get_county(self, origin_url, now_url, origin_code):
        """获取县、区级地址信息"""
        city_url = parse.urljoin(origin_url, now_url)
        # 解析县区的html
        print('开始解析县/区级信息……')
        html = self.get_web_html(city_url)
        soup = BeautifulSoup(html, 'lxml')
        county_list = soup.select('.countytr')
        for county_info in county_list:
            a_info = county_info.find_all(name='a')
            if a_info:
                county_name = a_info[1].get_text()
                county_code = a_info[0].get_text()
                county_url = a_info[0].attrs['href']
                print(county_name, county_code, county_url)
                # 数据存入字典
                dict_info = {}
                dict_info.update({'name': county_name})
                dict_info.update({'code': county_code})
                dict_info.update({'parent_code': origin_code})
                dict_info.update({'level': 3})
                # 读写json数据
                self.read_write_by_json(dict_info, 'county')
                # 获取乡镇信息
                self.get_town(city_url, county_url, county_code)
            else:
                td_info = county_info.find_all(name='td')
                county_name = td_info[1].get_text()
                county_code = td_info[0].get_text()
                county_url = ''
                print(county_name, county_code, county_url)
        print('县/区级解析结束！')

    def get_town(self, origin_url, now_url, origin_code):
        """获取乡镇地址信息"""
        county_url = parse.urljoin(origin_url, now_url)
        # 解析县区的html
        print('开始解析乡镇级信息……')
        html = self.get_web_html(county_url)
        soup = BeautifulSoup(html, 'lxml')
        town_list = soup.select('.towntr')
        for town_info in town_list:
            a_info = town_info.find_all(name='a')
            town_name = a_info[1].get_text()
            town_code = a_info[0].get_text()
            town_url = a_info[0].attrs['href']
            print(town_name, town_code, town_url)
            # 数据存入字典
            dict_info = {}
            dict_info.update({'name': town_name})
            dict_info.update({'code': town_code})
            dict_info.update({'parent_code': origin_code})
            dict_info.update({'level': 4})
            # 读写json数据
            self.read_write_by_json(dict_info, 'town')
        print('乡镇级解析结束！')

    def init_file(self):
        """初始化文件夹数据"""
        # 目录不存在，先创建
        if not os.path.exists(self.json_folder):
            os.mkdir(self.json_folder)
        # 文件不存在，也先初始化
        for file_name in self.json_file.values():
            # 初始化空列表写入
            file_path = os.path.join(self.json_folder, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump([], file)

    def read_write_by_json(self, data, city_type):
        """读写json文件"""
        self.lock.acquire()
        file_name = self.json_file[city_type]
        file_path = os.path.join(self.json_folder, file_name)
        # 读文件
        with open(file_path, 'r', encoding='utf-8') as read_file:
            data_list = json.load(read_file)
            data_list.append(data)
            # 写文件
            with open(file_path, 'w', encoding='utf-8') as write_file:
                json.dump(data_list, write_file, ensure_ascii=False)
        self.lock.release()

    def run(self):
        """执行入口"""
        # 初始化存储文件
        self.init_file()
        # 解析省份的html
        print('开始解析省份信息……')
        html = self.get_web_html(self.url)
        soup = BeautifulSoup(html, 'lxml')
        province_list = soup.select('.provincetr a')
        for province_info in province_list:
            province_name = province_info.get_text()
            province_url = province_info.attrs['href']
            province_code = province_url.split('.')[0]
            print(province_name, province_code, province_url)
            # 数据存入字典
            dict_info = {}
            dict_info.update({'name': province_name})
            dict_info.update({'code': province_code})
            dict_info.update({'parent_code': '0'})
            dict_info.update({'level': '1'})
            # 读写json数据
            self.read_write_by_json(dict_info, 'province')
            # 多线程爬取
            t = threading.Thread(target=self.get_city, name='LoopThread', args=(self.url, province_url, province_code))
            t.start()
            # 爬取市级信息
        print('省份解析结束！')


# 程序主入口
if __name__ == '__main__':
    # 实例化执行
    print('开始执行……')
    start_time = datetime.now()
    city = GetCity()
    city.run()
    end_time = datetime.now()
    print('程序执行结束！')
    print('开始时间：%s，结束时间：%s' % (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')))
