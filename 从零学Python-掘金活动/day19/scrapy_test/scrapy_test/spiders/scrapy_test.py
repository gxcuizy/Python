#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
scrapy基础使用
author: gxcuizy
date: 2018-11-08
"""

import scrapy


class DmozSpider(scrapy.spiders.Spider):
    name = "juejin"
    allowed_domains = ["juejin.im"]
    start_urls = [
        "https://juejin.im/activities/posts",
        "https://juejin.im/activities/pins"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)


# 程序主入口
if __name__ == '__main__':
    pass
