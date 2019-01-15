#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
通过splinter刷12306火车票（多个车次查询）
进入登陆页面，可以选择扫码登陆或者账号密码登陆
登陆成功后，接下来的事情，交由脚本来做了，静静的等待抢票结果就好（刷票过程中，浏览器不可关闭）
抢票成功，会进行手机短信和邮件的通知
author: cuizy
time: 2018-12-28
"""

import re
from splinter.browser import Browser
from time import sleep
import sys
import httplib2
from urllib import parse
import smtplib
from email.mime.text import MIMEText
import time


class BrushTicket(object):
    """买票类及实现方法"""

    def __init__(self, passengers, from_time, from_station, to_station, numbers, seat_type, receiver_mobile,
                 receiver_email):
        """定义实例属性，初始化"""
        # 乘客姓名
        self.passengers = passengers
        # 起始站和终点站
        self.from_station = from_station
        self.to_station = to_station
        # 车次
        self.numbers = list(map(lambda number: number.capitalize(),numbers))
        # 乘车日期
        self.from_time = from_time
        # 座位类型所在td位置
        if seat_type == '商务座特等座':
            seat_type_index = 1
            seat_type_value = 9
        elif seat_type == '一等座':
            seat_type_index = 2
            seat_type_value = 'M'
        elif seat_type == '二等座':
            seat_type_index = 3
            seat_type_value = 0
        elif seat_type == '高级软卧':
            seat_type_index = 4
            seat_type_value = 6
        elif seat_type == '软卧':
            seat_type_index = 5
            seat_type_value = 4
        elif seat_type == '动卧':
            seat_type_index = 6
            seat_type_value = 'F'
        elif seat_type == '硬卧':
            seat_type_index = 7
            seat_type_value = 3
        elif seat_type == '软座':
            seat_type_index = 8
            seat_type_value = 2
        elif seat_type == '硬座':
            seat_type_index = 9
            seat_type_value = 1
        elif seat_type == '无座':
            seat_type_index = 10
            seat_type_value = 1
        elif seat_type == '其他':
            seat_type_index = 11
            seat_type_value = 1
        else:
            seat_type_index = 7
            seat_type_value = 3
        self.seat_type_index = seat_type_index
        self.seat_type_value = seat_type_value
        # 通知信息
        self.receiver_mobile = receiver_mobile
        self.receiver_email = receiver_email
        # 新版12306官网主要页面网址
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.init_my_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        # 浏览器驱动信息，驱动下载页：https://sites.google.com/a/chromium.org/chromedriver/downloads
        self.driver_name = 'chrome'
        self.driver = Browser(driver_name=self.driver_name)

    def do_login(self):
        """登录功能实现，手动识别验证码进行登录"""
        self.driver.visit(self.login_url)
        sleep(1)
        # 选择登陆方式登陆
        print('请扫码登陆或者账号登陆……')
        while True:
            if self.driver.url != self.init_my_url:
                sleep(1)
            else:
                break

    def start_brush(self):
        """买票功能实现"""
        # 浏览器窗口最大化
        self.driver.driver.maximize_window()
        # 登陆
        self.do_login()
        # 跳转到抢票页面
        self.driver.visit(self.ticket_url)
        sleep(1)
        try:
            print('开始刷票……')
            # 加载车票查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.from_station})
            self.driver.cookies.add({"_jc_save_toStation": self.to_station})
            self.driver.cookies.add({"_jc_save_fromDate": self.from_time})
            self.driver.reload()
            count = 0
            while self.driver.url == self.ticket_url:
                try:
                    self.driver.find_by_text('查询').click()
                except Exception as error_info:
                    print(error_info)
                    sleep(1)
                    continue
                sleep(0.5)
                count += 1
                local_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print('第%d次点击查询……[%s]' % (count, local_date))
                try:
                    start_list = self.driver.find_by_css('.start-t')
                    for start_time in start_list:
                        current_time = start_time.text
                        current_tr = start_time.find_by_xpath('ancestor::tr')
                        if current_tr:
                            car_no = current_tr.find_by_css('.number').text
                            if car_no in self.numbers:
                                if current_tr.find_by_tag('td')[self.seat_type_index].text == '--':
                                    print('%s无此座位类型出售……' % (car_no + '(' + current_time + ')',))
                                    sleep(0.2)
                                elif current_tr.find_by_tag('td')[self.seat_type_index].text == '无':
                                    print('%s无票……' % (car_no + '(' + current_time + ')',))
                                    sleep(0.2)
                                else:
                                    # 有票，尝试预订
                                    print(car_no + '(' + current_time + ')刷到票了（余票数：' + str(current_tr.find_by_tag('td')[self.seat_type_index].text) + '），开始尝试预订……')
                                    current_tr.find_by_css('td.no-br>a')[0].click()
                                    sleep(0.5)
                                    key_value = 1
                                    for p in self.passengers:
                                        if '()' in p:
                                            p = p[:-1] + '学生' + p[-1:]
                                        # 选择用户
                                        print('开始选择用户……')
                                        self.driver.find_by_text(p).last.click()
                                        # 选择座位类型
                                        print('开始选择席别……')
                                        if self.seat_type_value != 0:
                                            self.driver.find_by_xpath(
                                                "//select[@id='seatType_" + str(key_value) + "']/option[@value='" + str(
                                                    self.seat_type_value) + "']").first.click()
                                        key_value += 1
                                        sleep(0.2)
                                        if p[-1] == ')':
                                            self.driver.find_by_id('dialog_xsertcj_ok').click()
                                    print('正在提交订单……')
                                    self.driver.find_by_id('submitOrder_id').click()
                                    sleep(2)
                                    # 查看放回结果是否正常
                                    submit_false_info = self.driver.find_by_id('orderResultInfo_id')[0].text
                                    if submit_false_info != '':
                                        print(submit_false_info)
                                        self.driver.find_by_id('qr_closeTranforDialog_id').click()
                                        sleep(0.2)
                                        self.driver.find_by_id('preStep_id').click()
                                        sleep(0.3)
                                        continue
                                    print('正在确认订单……')
                                    self.driver.find_by_id('qr_submit_id').click()
                                    print('预订成功，请及时前往支付……')
                                    # 发送通知信息
                                    self.send_mail(self.receiver_email, '恭喜您，抢到票了，请及时前往12306支付订单！')
                                    self.send_sms(self.receiver_mobile, '您的验证码是：8888。请不要把验证码泄露给其他人。')
                                    sys.exit(0)
                        else:
                            print('当前车次异常')
                except Exception as error_info:
                    print(error_info)
                    # 跳转到抢票页面
                    self.driver.visit(self.ticket_url)
        except Exception as error_info:
            print(error_info)

    def send_sms(self, mobile, sms_info):
        """发送手机通知短信，用的是-互亿无线-的测试短信"""
        host = "106.ihuyi.com"
        sms_send_uri = "/webservice/sms.php?method=Submit"
        account = "C59782899"
        pass_word = "19d4d9c0796532c7328e8b82e2812655"
        params = parse.urlencode(
            {'account': account, 'password': pass_word, 'content': sms_info, 'mobile': mobile, 'format': 'json'}
        )
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib2.HTTPConnectionWithTimeout(host, port=80, timeout=30)
        conn.request("POST", sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str

    def send_mail(self, receiver_address, content):
        """发送邮件通知"""
        # 连接邮箱服务器信息
        host = 'smtp.163.com'
        port = 25
        sender = 'gxcuizy@163.com'  # 你的发件邮箱号码
        pwd = 'FatBoy666'  # 不是登陆密码，是客户端授权密码
        # 发件信息
        receiver = receiver_address
        body = '<h2>温馨提醒：</h2><p>' + content + '</p>'
        msg = MIMEText(body, 'html', _charset="utf-8")
        msg['subject'] = '抢票成功通知！'
        msg['from'] = sender
        msg['to'] = receiver
        s = smtplib.SMTP(host, port)
        # 开始登陆邮箱，并发送邮件
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())


if __name__ == '__main__':
    # 乘客姓名
    passengers_input = input('请输入乘车人姓名，多人用英文逗号“,”连接，（例如单人“张三”或者多人“张三,李四”，如果学生的话输入“王五()”）：')
    passengers = passengers_input.split(",")
    while passengers_input == '' or len(passengers) > 4:
        print('乘车人最少1位，最多4位！')
        passengers_input = input('请重新输入乘车人姓名，多人用英文逗号“,”连接，（例如单人“张三”或者多人“张三,李四”）：')
        passengers = passengers_input.split(",")
    # 乘车日期
    from_time = input('请输入乘车日期（例如“2018-08-08”）：')
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    while from_time == '' or re.findall(date_pattern, from_time) == []:
        from_time = input('乘车日期不能为空或者时间格式不正确，请重新输入：')
    # 城市cookie字典
    city_list = {
        'bj': '%u5317%u4EAC%2CBJP',  # 北京
        'hd': '%u5929%u6D25%2CTJP',  # 邯郸
        'nn': '%u5357%u5B81%2CNNZ',  # 南宁
        'wh': '%u6B66%u6C49%2CWHN',  # 武汉
        'cs': '%u957F%u6C99%2CCSQ',  # 长沙
        'ty': '%u592A%u539F%2CTYV',  # 太原
        'yc': '%u8FD0%u57CE%2CYNV',  # 运城
        'gzn': '%u5E7F%u5DDE%u5357%2CIZQ',  # 广州南
        'wzn': '%u68A7%u5DDE%u5357%2CWBZ',  # 梧州南
    }
    # 出发站
    from_input = input('请输入出发站，只需要输入首字母就行（例如北京“bj”）：')
    while from_input not in city_list.keys():
        from_input = input('出发站不能为空或不支持当前出发站（如有需要，请联系管理员！），请重新输入：')
    from_station = city_list[from_input]
    # 终点站
    to_input = input('请输入终点站，只需要输入首字母就行（例如北京“bj”）：')
    while to_input not in city_list.keys():
        to_input = input('终点站不能为空或不支持当前终点站（如有需要，请联系管理员！），请重新输入：')
    to_station = city_list[to_input]
    # 乘车车次
    number_input = input('请输入抢票车次号，多车次用英文逗号“,”链接，（例如单车次“Z285”或者多车次“Z285,G110”）：')
    numbers = number_input.split(",")
    while number_input == '':
        number_input = input('请重新输入抢票车次号，多车次用英文逗号“,”链接，（例如单车次“Z285”或者多车次“Z285,G110”）：')
        numbers = number_input.split(",")
    # 座位类型
    seat_type = input('请输入座位类型（例如“软卧”）：')
    while seat_type == '':
        seat_type = input('座位类型不能为空，请重新输入：')
    # 抢票成功，通知该手机号码
    receiver_mobile = input('请预留一个手机号码，方便抢到票后进行通知（例如：18888888888）：')
    mobile_pattern = re.compile(r'^1{1}\d{10}$')
    while receiver_mobile == '' or re.findall(mobile_pattern, receiver_mobile) == []:
        receiver_mobile = input('预留手机号码不能为空或者格式不正确，请重新输入：')
    receiver_email = input('请预留一个邮箱，方便抢到票后进行通知（例如：test@163.com）：')
    while receiver_email == '':
        receiver_email = input('预留邮箱不能为空，请重新输入：')
    # 开始抢票
    ticket = BrushTicket(passengers, from_time, from_station, to_station, numbers, seat_type, receiver_mobile,
                         receiver_email)
    ticket.start_brush()
