#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用代理IP刷点赞票（飞猪代理-多进程）
author: gxcuizy
date: 2021-03-26
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from multiprocessing import Process


class FeiZhuProcess(Process):
    def __init__(self):
        # 继承Process类
        super(FeiZhuProcess, self).__init__()
        # 点赞接口地址
        self.api_url = 'http://638140.szyuansl.com/topfirst.php?g=Wap&m=Vote&a=ticket'
        # 点赞请求参数
        self.post_param = {'zid': '11883', 'vid': '237', 'token': 'WMFAUktmdTwiHtTe'}
        # 接口请求头信息
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1320.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # 代理IP地址
        self.proxies = {}
        # 超时时间
        self.time_out = 20

    def get_proxies_ip(self, ip_url):
        """获取代理IP"""
        ip_request = requests.get(url=ip_url)
        html_content = ip_request.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # IP列表
        tr_list = soup.select('tbody tr')
        ip_list = []
        for tr in tr_list:
            td_info = tr.select('td')
            ip_host = td_info[0].text.strip()
            ip_port = td_info[1].text.strip()
            ip_base = '//' + ip_host + ':' + ip_port
            ip_list.append(ip_base)
        return ip_list

    def print_msg(self, msg=''):
        """打印信息"""
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('[' + now_time + '] ' + msg)

    def run(self):
        """执行程序"""
        while True:
            # 获取前500页
            page_list = range(1, 500)
            for page in page_list:
                request_url = 'https://www.kuaidaili.com/free/inha/' + str(page)
                # 获取IP地址
                ip_list = self.get_proxies_ip(request_url)
                for ip_info in ip_list:
                    self.proxies = {
                        'http': 'http:' + ip_info,
                        'https': 'https:' + ip_info
                    }
                    try:
                        # 发送post请求
                        request = requests.post(url=self.api_url, data=self.post_param, headers=self.header,
                                                proxies=self.proxies, timeout=self.time_out)
                        response_text = request.text
                        self.print_msg(response_text)
                    except Exception as err_info:
                        # 异常信息
                        self.print_msg(str(err_info))


# 程序主入口
if __name__ == '__main__':
    # 获取运行的进程数
    process_num = input('请输入运行进程数：')
    process_list = []
    for i in range(int(process_num)):
        p = FeiZhuProcess()
        # star默认执行run()方法
        p.start()
        process_list.append(p)
    # 循环执行多进程
    for process in process_list:
        process.join()
        # 每个进程间隔10秒执行
        time.sleep(10)
