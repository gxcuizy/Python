#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
爬取国家统计局最新地址库
省市区三级（Mysql版本）（三张表）
author: gxcuizy
time: 2018-08-24
"""

import requests
from bs4 import BeautifulSoup
import os


def get_province(index_href):
    """抓取省份信息"""
    print('开始抓取省份信息……')
    province_url = url + index_href
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    request = requests.get(province_url, headers=headers)
    request.encoding = 'gbk'
    province_html_text = str(request.text)
    soup = BeautifulSoup(province_html_text, "html.parser")
    province_tr_list = soup.select('.provincetr a')
    # 遍历省份列表信息
    file = open('mysql/province.sql', 'w', encoding='utf-8')
    for province_tr in province_tr_list:
        if province_tr:
            province_href = province_tr.attrs['href']
            province_no = province_href.split('.')[0]
            province_code = province_no + '0000'
            province_name = province_tr.text
            province_info = 'INSERT INTO province (code, name) VALUES ("' + str(province_code) + '", "' + str(province_name) + '");\n'
            file.write(province_info)
            print('已写入省级：', province_info)
            # 市级
            get_city(province_href, province_code)
    print('抓取省份信息结束！')
    file.close()


def get_city(province_href, province_code):
    """抓取市级城市信息"""
    print('开始抓取市级信息')
    city_url = url + province_href
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    request = requests.get(city_url, headers=headers)
    request.encoding = 'gbk'
    city_html_text = str(request.text)
    soup = BeautifulSoup(city_html_text, "html.parser")
    city_tr_list = soup.select('.citytr')
    # 遍历市级城市列表信息
    file = open('mysql/city.sql', 'a+', encoding='utf-8')
    for city_tr in city_tr_list:
        if city_tr:
            city_a_info = city_tr.select('a')
            city_href = city_a_info[0].attrs['href']
            city_code = city_a_info[0].text[:6]
            city_name = city_a_info[1].text
            city_info = 'INSERT INTO city (code, name, province_code) VALUES ("' + str(city_code) + '", "' + str(city_name) + '", "' + str(province_code) + '");\n'
            file.write(city_info)
            print('已写入市级：', city_info)
            # 区级
            get_area(city_href, city_code)
    print('抓取市级城市结束！')
    file.close()


def get_area(city_href, city_code):
    """抓取区级信息"""
    print('开始抓取区级信息')
    area_url = url + city_href
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    request = requests.get(area_url, headers=headers)
    request.encoding = 'gbk'
    area_html_text = str(request.text)
    soup = BeautifulSoup(area_html_text, "html.parser")
    area_tr_list = soup.select('.countytr')
    # 遍历区级列表信息
    file = open('mysql/area.sql', 'a+', encoding='utf-8')
    for area_tr in area_tr_list:
        area_a_info = area_tr.select('td')
        if area_a_info:
            area_code = area_a_info[0].text[:6]
            area_name = area_a_info[1].text
            area_info = 'INSERT INTO area (code, name, city_code) VALUES ("' + str(area_code) + '", "' + str(area_name) + '", "' + str(city_code) + '");\n'
            file.write(area_info)
            print('已写入区级：', area_info)
    print('抓取区级信息结束！')
    file.close()


# 程序主入口
if __name__ == "__main__":
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    # 创建json目录
    mysql_folder = 'mysql/'
    if not os.path.exists(mysql_folder):
        os.makedirs(mysql_folder)
    else:
        # 清空城市和地区
        city_file = open('mysql/city.sql', 'w', encoding='utf-8')
        city_file.write('')
        city_file.close()
        area_file = open('mysql/area.sql', 'w', encoding='utf-8')
        area_file.write('')
        area_file.close()
    get_province('index.html')
