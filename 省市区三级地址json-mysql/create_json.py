#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import json


def get_data(select_sql):
    """获取数据库地址信息"""
    # 创建一个连接
    db = pymysql.connect(db_host, db_user, db_pw, db_name)
    # 用cursor()创建一个游标对象
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 插入数据sql
    print('开始查询：%s' % select_sql)
    # 执行插入
    cursor.execute(select_sql)
    # 获取全部数据
    city_data = cursor.fetchall()
    # 关闭连接
    cursor.close()
    db.close()
    return city_data

    # 程序主入口


if __name__ == "__main__":
    # 数据库链接参数
    db_host = '192.168.11.20'
    db_name = 'gshop'
    db_user = 'gshop'
    db_pw = 'T4dABtXMbs'
    # 大json数据
    city_json = {'name': 'China', 'provinces': []}
    # 获取省份列表
    province_sql = 'select id,name,level,parent_id,big_id,gid from xfc_region where level = 1'
    province_list = get_data(province_sql)
    for (province_key, province) in enumerate(province_list):
        # 获取市级列表
        city_sql = 'select id,name,level,parent_id,big_id,gid from xfc_region where level = 2 and parent_id = ' + str(
            province['id'])
        city_list = get_data(city_sql)
        for (city_key, city) in enumerate(city_list):
            # 获取区级列表
            area_sql = 'select id,name,level,parent_id,big_id,gid from xfc_region where level = 3 and parent_id = ' + str(
                city['id'])
            area_list = get_data(area_sql)
            city_list[city_key]['areas'] = area_list
        province_list[province_key]['cities'] = city_list
        city_json['provinces'].append(province)
    file = open('address.json', 'w', encoding='utf-8')
    json.dump(city_json, file, ensure_ascii=False, indent=4)
