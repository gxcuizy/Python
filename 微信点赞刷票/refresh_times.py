#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
刷新网页的浏览次数
author: gxcuizy
date: 2021-03-25
"""

import requests

# 程序主入口
if __name__ == "__main__":
    # 请求刷新次数
    times = int(input('请输入刷新次数：'))
    # 活动网页地址
    url = 'http://191456.szyuansl.com//topfirst.php?g=Wap&m=Vote&a=detail&token=WMFAUktmdTwiHtTe&id=237&zid=11883&href=1'
    # 请求头信息
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1320.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)'
    }
    # 循环刷新
    while times > 0:
        try:
            requests.get(url=url, headers=header)
            times -= 1
            print('剩余刷新次数：' + str(times))
        except Exception as err_info:
            # 异常信息
            print(err_info)
