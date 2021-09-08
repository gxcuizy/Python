#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
自动登陆账号邮箱
author: gxcuizy
date: 2021-09-06
"""

from selenium import webdriver
import pymysql
import time
import os
import re


class LoginMail(object):
    """邮箱账号自动登陆"""

    def __init__(self):
        """定义实例属性，初始化"""
        # 初始化浏览器驱动
        self.chrome_option = webdriver.ChromeOptions()
        # 关闭左上角的监控提示
        self.chrome_option.add_argument("""--no-sandbox""")
        self.chrome_option.add_argument("""--disable-gpu""")
        self.chrome_option.add_experimental_option('useAutomationExtension', False)
        self.chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = None
        # 浏览器驱动
        self.chrome_driver = 'driver/chromedriver93.exe'
        # 邮箱登陆网站入口
        self.gmail_url = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        self.ex_mail_url = 'https://exmail.qq.com/login'
        self.outlook_url = 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000'
        self.yahoo_url = 'https://login.yahoo.com/?display=login'
        self.qq_url = 'https://mail.qq.com/cgi-bin/loginpage'
        self.aliyun_qiye_url = 'https://qiye.aliyun.com/'
        self.wangyi_url = 'https://mail.163.com/'
        self.wangyi_qiye_url = 'https://qiye.163.com/login/'
        self.aliyun_url = 'https://mail.aliyun.com/'
        self.kuaiyun_url = 'https://mail.kuaiyunec.com/mail/'
        # Mysql数据库链接参数
        self.db_host = '127.0.0.1'
        self.db_name = 'name'
        self.db_user = 'root'
        self.db_pw = 'root'
        self.db_port = 2701
        # 登陆输出信息
        self.login_msg = ''
        # 输入账号
        self.site_code = ''

    def get_mail_config(self):
        """获取邮箱配置数据"""
        # 创建一个连接
        db = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_pw, db=self.db_name,
                             port=self.db_port)
        # 用cursor()创建一个游标对象
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        # 查询邮箱配置列表
        sql = 'SELECT site_code,cmc_mail_account,cmc_mail_login_pwd,imap_id FROM crm_mail_config WHERE site_code = "' + str(
            self.site_code) + '" AND cmc_mail_imap_status = 1 AND mail_type = 1'
        cursor.execute(sql)
        return cursor.fetchone()

    def handle_exception(self, error_msg):
        """异常信息处理"""
        try:
            error_msg = str(error_msg)
            print(error_msg)
            match_res = re.match(r'[\s\S]*?Current browser version is (.*) with binary path[\s\S]*?', error_msg)
            if match_res:
                # 版本问题切换版本重试
                version_str = match_res.group(1)
                # 分割出版本
                version_list = version_str.split(".")
                version_num = version_list[0]
                self.chrome_driver = 'driver/chromedriver' + str(version_num) + '.exe'
                self.run(self.site_code)
        except Exception as error_info:
            # 异常处理
            print(error_info)

    def login_gmail(self, account, pwd):
        """登陆谷歌Gmail邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.gmail_url)
            time.sleep(1)
            # 输入邮箱
            self.driver.find_element_by_id("identifierId").send_keys(account)
            # 点击下一步
            self.driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
            time.sleep(3)
            # 输入密码
            self.driver.find_element_by_xpath("//div[@class='Xb9hP']/input[1]").send_keys(pwd)
            # 下一步登陆
            self.driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_outlook(self, account, pwd):
        """登陆微软Outlook邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.outlook_url)
            time.sleep(1)
            # 输入邮箱
            self.driver.find_element_by_id("i0116").send_keys(account)
            # 点击下一步
            self.driver.find_element_by_id("idSIButton9").click()
            time.sleep(3)
            # 输入密码
            self.driver.find_element_by_id("i0118").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id("idSIButton9").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_ex_mail(self, account, pwd):
        """登陆腾讯企业邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.ex_mail_url)
            time.sleep(1)
            # 输入邮箱和密码
            self.driver.find_element_by_class_name("js_show_pwd_panel").click()
            self.driver.find_element_by_id("inputuin").send_keys(account)
            self.driver.find_element_by_id("pp").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id("btlogin").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_yahoo(self, account, pwd):
        """登陆雅虎邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.yahoo_url)
            time.sleep(1)
            # 输入邮箱
            self.driver.find_element_by_id("login-username").send_keys(account)
            # 点击下一步
            self.driver.find_element_by_id("login-signin").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_qq(self, account, pwd):
        """登陆腾讯企业邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.qq_url)
            time.sleep(1)
            # 切换到登录框并输入账号密码
            self.driver.switch_to.frame('login_frame')
            self.driver.find_element_by_name('u').send_keys(account)
            self.driver.find_element_by_name('p').send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id('login_button').click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_aliyun_qiye(self, account, pwd):
        """登陆阿里云企业邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.aliyun_qiye_url)
            time.sleep(1)
            # 切换到登录框并输入账号密码
            self.driver.switch_to.frame(self.driver.find_element_by_class_name("login_panel_iframe"))
            self.driver.find_element_by_class_name('dingding-mail-login-option-m').click()
            self.driver.switch_to.frame('ding-login-iframe')
            self.driver.find_element_by_id("username").send_keys(account)
            self.driver.find_element_by_id("password").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id("login_submit_btn").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_wangyi(self, account, pwd):
        """登陆网易个人邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.wangyi_url)
            time.sleep(1)
            # 分割出账号
            account_list = account.split("@")
            account_name = account_list[0]
            # 切换到登录框并输入账号密码
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//div[@id='loginDiv']/iframe"))
            self.driver.find_element_by_name("email").send_keys(account_name)
            self.driver.find_element_by_name("password").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id("dologin").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_wangyi_qiye(self, account, pwd):
        """登陆网易企业邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.wangyi_qiye_url)
            time.sleep(1)
            # 切换到登录框并输入账号密码
            self.driver.find_element_by_id("accname").send_keys(account)
            self.driver.find_element_by_id("accpwd").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_class_name("w-button-account").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_aliyun(self, account, pwd):
        """登陆阿里云个人邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.aliyun_url)
            time.sleep(1)
            # 分割出账号
            account_list = account.split("@")
            account_name = account_list[0]
            # 切换到登录框并输入账号密码
            self.driver.switch_to.frame('alibaba-login-box')
            self.driver.find_element_by_name("loginId").send_keys(account_name)
            self.driver.find_element_by_name("password").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id("fm-login-submit").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def login_kuaiyun(self, account, pwd):
        """登陆快云邮箱"""
        try:
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver, chrome_options=self.chrome_option)
            self.driver.maximize_window()
            self.driver.get(self.kuaiyun_url)
            time.sleep(1)
            # 输入账号密码
            self.driver.find_element_by_id("rcmloginuser").send_keys(account)
            self.driver.find_element_by_id("rcmloginpwd").send_keys(pwd)
            # 点击登陆
            self.driver.find_element_by_id("rcmloginsubmit").click()
        except Exception as error_info:
            # 异常处理
            self.handle_exception(error_info)

    def run(self, site_code):
        """脚本执行方法"""
        self.site_code = site_code.strip()
        mail_config = self.get_mail_config()
        if mail_config == None:
            print('当前账号邮箱配置不存在')
            return
        self.login_msg = '\n开始登陆邮箱，站点:[' + str(mail_config['site_code']) + ']，邮箱:[' + str(
            mail_config['cmc_mail_account']) + ']，密码:[' + str(mail_config['cmc_mail_login_pwd'] + ']\n')
        print(self.login_msg)
        if mail_config['imap_id'] == 1:
            # Gmail邮箱登陆
            self.login_gmail(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 2:
            # 腾讯企业邮箱
            self.login_ex_mail(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 3:
            # 微软邮箱
            self.login_outlook(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 4:
            # 雅虎邮箱
            self.login_yahoo(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 6:
            # QQ邮箱
            self.login_qq(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 7:
            # 阿里云企业邮箱
            self.login_aliyun_qiye(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 8:
            # 网易个人邮箱
            self.login_wangyi(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 9:
            # 网易企业邮箱
            self.login_wangyi_qiye(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 10:
            # 阿里云个人邮箱
            self.login_aliyun(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        elif mail_config['imap_id'] == 11:
            # 快云邮箱
            self.login_kuaiyun(mail_config['cmc_mail_account'], mail_config['cmc_mail_login_pwd'])
        else:
            print('暂不支持该类型邮箱登陆')


# 程序主入口
if __name__ == "__main__":
    obj = LoginMail()
    input_code = input('请输入您需要登陆的站点（然后回车执行）：')
    obj.run(input_code)
    os.system('pause')
