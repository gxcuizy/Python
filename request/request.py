#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 程序主入口
if __name__ == "__main__":
    """模仿浏览器，请求api信息"""
    url = 'http://xssychina.com/plus/count.php?view=yes&aid=206&mid=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    request = requests.get(url, headers=headers)
    html_text = request.text
    print(html_text)
