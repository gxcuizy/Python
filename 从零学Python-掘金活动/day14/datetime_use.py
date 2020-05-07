#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常见的内建模块练习之datetime
author: gxcuizy
date: 2018-10-30
"""

from datetime import datetime
from datetime import timedelta
import calendar

# 程序主入口
if __name__ == '__main__':
    # datetime是python处理时间和日期的标准库
    # datetime.now()返回当前日期和时间
    now = datetime.now()
    print(now)

    # datetime()可以直接传参数来构造获取日期和时间
    date = datetime(2018, 10, 30, 18)
    print(date)

    # timestamp()可以把dateeime类型的时间转为timestamp时间戳
    times = now.timestamp()
    print(times)

    # datetime.fromtimestamp()把timestamp类型的时间戳转为datetime类型的时间
    dt = datetime.fromtimestamp(times)
    print(dt)

    #  datetime.strptime()可以实现str字符串类型的日期转为datetime类型
    day = datetime.strptime('2018-10-30 12:00:13', '%Y-%m-%d %H:%M:%S')
    print(day)

    # strftime()实现datetime类型的日期转为str的日期
    str_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print(str_date)

    # datetime的加减计算（timestamp时间戳不能进行此计算）
    add_now = now + timedelta(days=1)
    add_now = add_now + timedelta(hours=3)
    add_now = add_now + timedelta(minutes=20)
    add_now = add_now + timedelta(seconds=30)
    print(add_now)

    # 获取月日历
    month = calendar.month(2018, 10)
    print(month)

    # 获取星期几
    weekday = calendar.weekday(2018, 10, 30)
    print(weekday)

    # 获取每个月的天数，以及第一天的星期
    monthrange = calendar.monthrange(2016, 2)
    print(monthrange)

    # 判断是否是闰年
    isleap = calendar.isleap(2018)
    print(isleap)

    # 计算年份范围内，有多少个闰年
    leapdays = calendar.leapdays(2000, 2018)
    print(leapdays)
