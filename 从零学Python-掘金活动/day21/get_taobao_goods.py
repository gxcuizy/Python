#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
selenium模拟浏览器抓取淘宝商品信息
author: gxcuizy
date: 2018-11-13
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class GetTaobaoGoods(object):
    """模拟浏览器，抓取淘宝商品"""

    def __init__(self, goods):
        """初始化变量"""
        self.driver = webdriver.Chrome()
        self.taobao_url = 'https://www.taobao.com'
        self.goods = goods

    def search_goods(self):
        """进入浏览器，搜索商品"""
        # 全屏
        self.driver.maximize_window()
        # 打开淘宝首页
        self.driver.get(self.taobao_url)
        # 输入商品，回车搜索
        search = self.driver.find_element_by_name('q')
        search.send_keys(self.goods)
        search.send_keys(Keys.RETURN)
        # 登陆淘宝
        self.login()

    def login(self):
        """登陆淘宝"""
        if 'login' in self.driver.current_url:
            print('请扫码登陆……')
            while True:
                if 'login' in self.driver.current_url:
                    sleep(1.5)
                else:
                    print('恭喜，登陆成功！')
                    break

    def scroll_to_button(self):
        # 滑动至底部
        for i in range(0, 4):
            # 每次滑动1000像素
            height = 1000 * i
            js_code = "window.scrollBy(0," + str(height) + ")"
            self.driver.execute_script(js_code)
            sleep(2)

    def get_goods_info(self):
        # 获取商品列表
        goods_list = self.driver.find_elements_by_class_name('J_MouserOnverReq')
        for goods_info in goods_list:
            goods = {}
            # 商品图片
            img_element = goods_info.find_element_by_class_name('img')
            goods_img = 'https:' + img_element.get_attribute('data-src')
            goods.update({'img': goods_img})
            # 商品价格
            price_element = goods_info.find_element_by_css_selector('.g_price strong')
            goods_price = price_element.text
            goods.update({'price': goods_price})
            # 购买人数
            count_element = goods_info.find_element_by_class_name('deal-cnt')
            goods_sale = count_element.text
            goods.update({'sale': goods_sale})
            # 商品名称
            title_element = goods_info.find_element_by_class_name('title')
            goods_title = title_element.text
            goods.update({'title': goods_title})
            # 店铺
            shop_element = goods_info.find_element_by_class_name('shop')
            goods_shop = title_element.text
            goods.update({'shop': goods_shop})
            # 所在地
            location_element = goods_info.find_element_by_class_name('location')
            goods_location = location_element.text
            goods.update({'location': goods_location})
            # 链接
            href_element = goods_info.find_element_by_css_selector('.title a')
            goods_href = href_element.get_attribute('href')
            goods.update({'href': goods_href})
            print(goods)

    def run(self):
        """执行脚本"""
        # 打开网页搜索商品
        self.search_goods()
        page_num = 1
        while True:
            print('正在获取第%s页的商品……' % page_num)
            # 滑动底部
            self.scroll_to_button()
            # 抓取商品
            self.get_goods_info()
            print('第%s页的商品抓取结束！' % page_num)
            # 查找下一页
            next_element = self.driver.find_element_by_class_name('next')
            next_page = next_element.find_element_by_tag_name('a')
            if next_page:
                next_page.click()
                page_num += 1
                sleep(2)
            else:
                break
        # 退出浏览器
        self.driver.quit()


# 程序主入口
if __name__ == '__main__':
    search_goods = '三只松鼠'
    tao_bao = GetTaobaoGoods(search_goods)
    tao_bao.run()
