#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
selenium模拟浏览器执行的练习
author: gxcuizy
date: 2018-11-08
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# 程序主入口
if __name__ == '__main__':
    # 安装selenium
    # pip install selenium

    # webdriver.Chrome()选择谷歌浏览器驱动，还支持Firefox以及IE等
    driver = webdriver.Chrome()
    # 访问url地址
    driver.get('https://www.google.com/')
    print(driver.title)
    # 确认标题是否包含“Python”一词
    assert 'Google' in driver.title
    # 查找搜索框的元素
    q_element = driver.find_element_by_name('q')
    # 向找到的元素输入信息
    q_element.send_keys('hello world')
    # 点击回车
    q_element.send_keys(Keys.RETURN)

    # element.click()可以实现一个点击事件

    #  WebDriver中提供了一个叫Select的方法
    # from selenium.webdriver.support.ui import Select
    # 根据索引来选择select_by_index()
    # 根据value值来选择select_by_value()
    # 根据option的文本内容来选择select_by_visible_text()
    # deselect_all()可以取消选择

    # 执行q_element.clear()可以清空刚才输入的值
    # 表单提交，还可以直接submit()方法处理

    # driver.switch_to_window()切换窗口，参数是窗口名称

    # driver.switch_to_alert()切换到弹框进行处理

    # driver.forward()前进和driver.back()后退

    # driver.add_cookie()可以为页面添加cookie值，参数是字典

    # driver.get_cookies()可以直接获取所有的cookie
    print(driver.get_cookies())
    # 获取当前url
    print(driver.current_url)
    # driver.close()是关闭当前标签页，driver.quit()退出整个浏览器
    driver.close()
