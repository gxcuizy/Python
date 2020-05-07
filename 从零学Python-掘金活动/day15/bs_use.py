#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BeautifulSoup的基础使用
author: gxcuizy
date: 2018-10-31
"""

from bs4 import BeautifulSoup

# 程序主入口
if __name__ == '__main__':
    # BeautifulSoup就是Python的一个HTML或XML的解析库
    # 常用的解析方式有标准的html解析以及第三方的lxml的解析
    # 推荐使用lxml作为解析器,因为效率更高
    # lxml解析，第二个参数为lxml
    test_html = '<html><body><div><p class="test p">Hello bs4<span id="test">666</span></p></div>'
    soup_lxml = BeautifulSoup(test_html, 'lxml')
    # string属性可以拿到节点的文本内容，text属性也是一样的，但是string会要求无其他元素节点
    print(soup_lxml.p.text)

    # 标准的html解析，第二个参数为html.parser
    soup = BeautifulSoup(test_html, 'html.parser')
    print(soup.p.span.string)

    # 调用prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出，并且自动补全结束标签
    print(soup.prettify())

    # name属性可以获取节点的名称
    print(soup.p.name)

    # attrs属性可以获取节点的属性名和属性值
    print(soup.p.attrs)
    # 获取某个具体的属性值
    print(soup.p.attrs['class'])

    # children属性可以获取直属子节点，childrens可以获取其下所有的节点（包括子节点的子节点）
    print(list(soup.p.children))

    # parent属性可以获取父节点，指的是直属父节点
    print(soup.span.parent)

    # parents属性可以获取祖先节点
    print(list(soup.span.parents))

    # 获取兄弟节点，soup.span.parent
    # next_sibling和previous_sibling分别获取节点的下一个和上一个兄弟元素
    # next_siblings和previous_siblings则分别返回所有前面和后面的兄弟节点的生成器

    # find_all()方法查询所有符合条件的元素节点-name
    print(soup.find_all('p'))
    print(soup.find_all(name='p'))

    # find_all()方法查询所有符合条件的元素节点-attrs，attrs的参数类型，必须是字典类型
    print(soup.find_all(attrs={'class': 'test'}))

    # 对于一些常用的属性，比如id和class等，我们可以不用attrs来传递，直接传id或者class_
    # 注意，class时，class在Python里是一个关键字，所以后面需要加一个下划线
    print(soup.find_all(id='test'))
    print(soup.find_all(class_='test'))

    # text文本信息查找
    print(soup.find_all(text='666'))

    # 相比find_all()的查找，还有一个find()的方法，只返回一个符合条件的节点
    print(soup.find(class_='test'))

    # 除了find这些方法选择器之外，还有css选择器
    # css选择器的使用，只需要调用select()方法，然后传入相应的css选择器即可
    print(soup.select('span'))
    print(soup.select('#test'))
    print(soup.select('.test'))
    print(soup.select('p span'))

    # 同时，select()方法同样支持嵌套选择

    # 获取属性值
    # 获取全部属性
    print(soup.select('#test')[0].attrs)
    # 节点的id属性值
    print(soup.select('#test')[0]['id'])

    # 获取文本信息，string属性、text属性以及get_text()方法
    # 多个文本信息string获取不到，还有strings获取多个文本信息
    print(soup.select('.test')[0].string)
    print(list(soup.select('.test')[0].strings))
    print(soup.select('.test')[0].get_text())
    print(soup.select('.test')[0].text)

    # 推荐使用lxml解析库，必要时使用html.parser
    # 节点选择筛选功能弱但是速度快
    # 建议使用find()查询单个结果或者find_all()查询多个结果
    # 如果对CSS选择器熟悉的话，可以使用select()方法选择
