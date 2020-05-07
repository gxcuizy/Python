#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常见的内建模块练习之xml、HTMLParser
author: gxcuizy
date: 2018-10-30
"""

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


# 程序主入口
if __name__ == '__main__':
    # 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
    # SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
    # 正常情况下，优先考虑SAX，因为DOM实在太占内存。
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
        <li><a href="/ruby">PHP</a></li>
    </ol>
    '''
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

    # Python提供了HTMLParser来非常方便地解析HTML
    # HTMLParser这是什么东西，真的是不好用，果断放弃，选择用第三方的beautiful soup
    # 今天就到这，push，然后下班……
