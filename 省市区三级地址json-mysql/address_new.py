#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
爬取国家统计局最新地址库
省市区三级（Mysql_V2版本）（一张表）
author: gxcuizy
time: 2018-08-24
"""

import requests
from bs4 import BeautifulSoup
import os
import pymysql
from urllib import parse


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
    level = '1'
    parent_code = ''
    for province_tr in province_tr_list:
        if province_tr:
            province_href = province_tr.attrs['href']
            province_no = province_href.split('.')[0]
            province_code = province_no + '0000'
            province_name = province_tr.text
            province_info = 'INSERT INTO xfc_region_copy (name, level, parent_id, gid) VALUES ("' + str(
                province_name) + '", "' + str(level) + '", "' + str('0') + '", "' + str(province_code) + '");'
            province_id = add_data(province_info, province_code)
            # 市级
            get_city(province_href, province_id)
    print('抓取省份信息结束！')


def get_city(province_href, province_id):
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
    level = '2'
    for city_tr in city_tr_list:
        if city_tr:
            city_a_info = city_tr.select('a')
            city_href = city_a_info[0].attrs['href']
            city_code = city_a_info[0].text[:6]
            city_name = city_a_info[1].text
            city_info = 'INSERT INTO xfc_region_copy (name, level, parent_id, gid) VALUES ("' + str(
                city_name) + '", "' + str(level) + '", "' + str(province_id) + '", "' + str(city_code) + '");'
            city_id = add_data(city_info, city_code)
            # 区级
            get_area(city_href, city_id)
    print('抓取市级城市结束！')


def get_area(city_href, city_id):
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
    level = '3'
    # 遍历区级列表信息
    if area_tr_list:
        for area_tr in area_tr_list:
            area_a_info = area_tr.select('a')
            if area_a_info:
                area_code = area_a_info[0].text[:6]
                area_href = area_a_info[1].attrs['href']
                area_name = area_a_info[1].text
                area_info = 'INSERT INTO xfc_region_copy (name, level, parent_id, gid) VALUES ("' + str(
                    area_name) + '", "' + str(level) + '", "' + str(city_id) + '", "' + str(area_code) + '");'
                area_id = add_data(area_info, area_code)
                # 街道
                get_town(area_url, area_href, area_id)
        print('抓取区级信息结束！')
    else:
        town_list = soup.select('.towntr')
        for town_info in town_list:
            a_info = town_info.find_all(name='a')
            town_name = a_info[1].get_text()
            town_code = a_info[0].get_text()[:9]
            town_sql = 'INSERT INTO xfc_region_copy (name, level, parent_id, gid) VALUES ("' + str(
                town_name) + '", "' + str(level) + '", "' + str(city_id) + '", "' + str(town_code) + '");\n'
            add_data(town_sql, town_code)
        print('乡镇级解析结束！')


def get_town(origin_url, now_url, area_id):
    """获取乡镇地址信息"""
    county_url = parse.urljoin(origin_url, now_url)
    # 解析县区的html
    print('开始解析乡镇级信息……')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    request = requests.get(county_url, headers=headers)
    request.encoding = 'gbk'
    contry_html_text = str(request.text)
    soup = BeautifulSoup(contry_html_text, "html.parser")
    town_list = soup.select('.towntr')
    level = '4'
    if town_list:
        for town_info in town_list:
            a_info = town_info.find_all(name='a')
            town_name = a_info[1].get_text()
            town_code = a_info[0].get_text()[:9]
            town_sql = 'INSERT INTO xfc_region_copy (name, level, parent_id, gid) VALUES ("' + str(
                town_name) + '", "' + str(level) + '", "' + str(area_id) + '", "' + str(town_code) + '");\n'
            add_data(town_sql, town_code)
        print('乡镇级解析结束！')
    else:
        village_list = soup.select('.villagetr')
        for village_info in village_list:
            a_info = village_info.find_all(name='td')
            village_name = a_info[2].get_text()
            village_code = a_info[0].get_text()
            town_sql = 'INSERT INTO xfc_region_copy (name, level, parent_id, gid) VALUES ("' + str(
                village_name) + '", "' + str(level) + '", "' + str(area_id) + '", "' + str(village_code) + '");\n'
            add_data(town_sql, village_code)
        print('乡镇级解析结束！')


def add_data(sql, region_code):
    """新增一条数据"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 查询该地址数据是否已加入
    cursor.execute('SELECT * FROM `xfc_region_copy` WHERE gid = "' + str(region_code) + '";')
    if cursor.rowcount > 0:
        # 获取单条数据
        info = cursor.fetchone()
        insert_id = info['id']
    else:
        # 插入数据sql
        print('开始新增一条数据：%s' % sql)
        # 执行插入
        cursor.execute(sql)
        # commit()提交执行，如果发生异常，db.rollback()可以回滚
        db.commit()
        insert_id = cursor.lastrowid
    # 关闭连接
    cursor.close()
    db.close()
    print('新增数据成功！')
    return insert_id


# 程序主入口
if __name__ == "__main__":
    # 数据库链接参数
    db_host = '192.168.11.20'
    db_name = 'gshop'
    db_user = 'gshop'
    db_pw = 'T4dABtXMbs'
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    # 创建json目录
    mysql_folder = 'mysql_v2/'
    if not os.path.exists(mysql_folder):
        os.makedirs(mysql_folder)
    else:
        # 清空城市和地区
        city_file = open('mysql_v2/area.sql', 'w', encoding='utf-8')
        city_file.write('')
        city_file.close()
    get_province('index.html')
