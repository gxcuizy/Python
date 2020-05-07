#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
splinter模拟浏览器执行的练习
author: gxcuizy
date: 2018-11-09
"""

from splinter import Browser

# 程序主入口
if __name__ == '__main__':
    # 安装splinter
    # pip install splinter

    # Browser()创建Browser实例，driver_name的默认值是firefox，支持chrome，以及zopetestbrowser
    browser = Browser(driver_name='chrome')

    # 可以更改浏览器的User-Agent
    # 在实例化Browser的时候，传入User-Agent参数值即可
    # browser = Browser(driver_name='chrome', user_agent="Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)")

    # 使用visit()方法访问一个网页
    url = 'http://www.google.com'
    browser.visit(url=url)

    # browser.cookies.add()增加cookie
    browser.cookies.add({'test_key': 'test'})
    browser.cookies.add({'test_key_2': 'test'})

    # 通过browser.cookies.all()获取所有的cookie
    print(browser.cookies.all())

    # browser.cookies.delete()删除cookie，参数是cookie的key，可以传多个，如果什么都不传，则默认删除全部
    browser.cookies.delete('test_key_2')
    print(browser.cookies.all())

    # fill()方法输入关键字
    browser.fill('q', 'python')

    # splinter提供了css、xpath、tag、name、id、value以及text六种查找方法
    # 查找都是返回一个list，first获取第一个，last获取最后一个，也可以根据索引获取
    # 查找Google的logo图片的div
    print(browser.find_by_id('hplogo'))
    # splinter还支持链式查找

    # 点击事件
    browser.find_by_css('.gb_Qc').first.find_by_tag('a').click()

    # 鼠标移入移出，mouse_over()方法移入，mouse_out()移出
    browser.find_by_css('.gsri_a').mouse_over()
    browser.find_by_css('.gsri_a').mouse_out()

    # double_click()双击操作
    browser.find_by_id('SIvCob').double_click()

    # right_click()方法右击元素
    browser.find_by_id('SIvCob').first.find_by_tag('a').right_click()

    # 点击搜索按钮
    submit_button = browser.find_by_xpath('//input[@type="submit"]')

    # value属性获取元素的内容
    print(submit_button.first.value)

    # is_element_present()检查元素是否存在
    # is_text_present()检查文本是否存在

    # click()方法点击事件
    # submit_button.click()

    # execute_script()方法执行Javascript脚本

    print(browser.windows)

    # 刷新页面
    # browser.reload()

    # windows属性进行窗口管理
    # windows熟悉获取全部窗口
    # windows.current属性获取当前窗口
    # windows.is_current属性判断是否是当前窗口
    # windows.next()下一个窗口
    # windows.prev()上一个窗口
    # windows.close()关闭当前窗口
    # windows.close_others()关闭其他窗口

    # back()和forward()查看历史浏览
    # browser.back()后退
    # browser.forward()前进

    # title属性获取页面标题
    print(browser.title)

    # 使用html属性可以获取网页的html页面内容
    # print(browser.html)

    # 当前页面的url可以通过url属性访问
    print(browser.url)

    # quit()方法关闭浏览器
    # browser.quit()
