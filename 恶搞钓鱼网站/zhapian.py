#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
模拟手机浏览器刷钓鱼诈骗网站
author: gxcuizy
date: 2021-09-03
"""

from selenium import webdriver
import random


class PreventFraud(object):
    """刷钓鱼网站数据类"""

    def __init__(self):
        """定义实例属性，初始化"""
        # 初始化浏览器驱动
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
        self.driver = None
        # 网站
        self.url = 'https://tz8gnkznst.bsj138168.xyz/x_kms.asp'

    def open_url(self, id_card):
        """打开网址，并输入信息"""
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=self.chrome_option)
        self.driver.get(self.url)
        # 输入身份证
        self.driver.find_element_by_id("accountNo").send_keys(id_card)
        # 提交下一步
        self.driver.find_element_by_id("btn").click()
        # 输入银行卡相关信息
        self.driver.find_element_by_id("xmxm").send_keys(self.get_user_name())
        self.driver.find_element_by_id("t4").send_keys('42010119850414' + str(random.randint(1000, 9999)))
        self.driver.find_element_by_id("t5").send_keys('1571664' + str(random.randint(1000, 9999)))
        self.driver.find_element_by_id("t3").send_keys(random.randint(100000, 999999))
        self.driver.find_element_by_id("je").send_keys(random.randint(10000, 99999))
        # 同意提交
        self.driver.find_element_by_xpath("//div[@class='tjbtn']/input[1]").click()
        # 关闭浏览器
        self.driver.close()

    def get_user_name(self):
        """随机生成姓名"""
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        return bytes.fromhex(val).decode('gb2312') + bytes.fromhex(val).decode('gb2312')

    def run(self):
        """脚本执行方法"""
        while True:
            self.open_url('622202075661528' + str(random.randint(1000, 9999)))


# 程序主入口
if __name__ == "__main__":
    obj = PreventFraud()
    obj.run()
