#! /usr/bin/python
# _*_ encode:utf-8_*_

"""
图林机器人聊天
author: gxcuizy
time: 2018-09-19
"""

import json
import socket
import uuid
from urllib.request import urlopen, Request
from urllib.parse import urlencode


class TuringChatMode(object):
    def __init__(self):
        # API接口地址
        self.turing_url = 'http://www.tuling123.com/openapi/api?'
        # AppKey密钥
        self.app_key = '82622364a28142878dd8ad634eec401c'

    def getTuringText(self, text):
        """获取聊天返回内容"""
        # 用户IP
        user_ip = self.getHostIp()
        # MAC地址
        mac_id = self.getMacId()
        # 请求参数
        turing_url_data = dict(
            # AppKey密钥
            key=self.app_key,
            # 聊天请求内容
            info=text,
            # 用户唯一标志（可以传IP地址或者MAC地址，或者其他的唯一标识）
            userid=mac_id
        )
        # 发送聊天请求
        request = Request(self.turing_url + urlencode(turing_url_data))
        try:
            w_data = urlopen(request)
        except Exception as error_info:
            return error_info
        response_text = w_data.read().decode('utf-8')
        json_result = json.loads(response_text)
        return json_result['text']

    def getHostIp(self):
        """获取用户IP"""
        socket_info = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_info.connect(('8.8.8.8', 80))
        ip = socket_info.getsockname()[0]
        return ip

    def getMacId(self):
        """获取MAC地址"""
        node = uuid.getnode()
        mac = uuid.UUID(int=node).hex[-12:]
        return mac


# 聊天程序主入口
if __name__ == '__main__':
    print("您可以和机器人聊天了（退出请输入q）")
    turing = TuringChatMode()
    while True:
        msg = input("\n我:")
        # 设定输入q，退出聊天。
        if msg == 'q':
            exit("聊天结束!")
        else:
            turing_data = turing.getTuringText(msg)
            print("机器人:", turing_data)
