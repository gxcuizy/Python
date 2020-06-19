#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用requests+bs4爬取国内高匿代理IP
author: gxcuizy
date: 2020-06-19
"""

import requests
from bs4 import BeautifulSoup
import json


class GetIpData(object):
    """爬取50页国内高匿代理IP"""
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    base_url = 'https://www.xicidaili.com/nn/'
    check_url = 'https://www.ip.cn/'
    json_data = []

    def get_url_html(self, url):
        """请求页面html"""
        request = requests.get(url=url, headers=self.header, timeout=5)
        html = False
        if request.status_code == 200:
            html = request.content
        return html

    def check_ip(self, ip_info):
        """测试IP地址是否有效"""
        ip_url = ip_info['ip'] + ':' + str(ip_info['port'])
        proxies = {'http': 'http://' + ip_url, 'https': 'https://' + ip_url}
        res = False
        try:
            request = requests.get(url=self.check_url, headers=self.header, proxies=proxies, timeout=5)
            if request.status_code == 200:
                res = True
        except Exception as error_info:
            res = False
        return res

    def run(self):
        """执行入口"""
        page_list = range(1, 51)
        with open("ip.json", "w") as write_file:
            for page in page_list:
                # 分页爬取数据
                print('开始爬取第' + str(page) + '页IP数据')
                ip_url = self.base_url + str(page)
                html = self.get_url_html(ip_url)
                soup = BeautifulSoup(html, 'html.parser')
                # IP列表
                ip_list = soup.select('#ip_list .odd')
                for ip_tr in ip_list:
                    # 单条Ip信息
                    td_list = ip_tr.select('td')
                    ip_address = td_list[1].get_text()
                    ip_port = td_list[2].get_text()
                    ip_type = td_list[5].get_text()
                    info = {'ip': ip_address, 'port': ip_port, 'type': ip_type}
                    # 先校验一下IP的有效性再存储
                    check_res = self.check_ip(info);
                    if check_res:
                        print('IP有效：', info)
                        self.json_data.append(info)
                    else:
                        print('IP无效：', info)
            json.dump(self.json_data, write_file)


# 程序主入口
if __name__ == '__main__':
    # 实例化
    ip = GetIpData()
    # 执行脚本
    ip.run()
