#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
距离下班时间倒计时
author: gxcuizy
date: 2021-04-27
"""

from tkinter import *
import time
import os


def refresh_current_time():
    """刷新当前时间"""
    clock_time = time.strftime('%Y-%m-%d %H:%M:%S')
    curr_time.config(text=clock_time)
    curr_time.after(1000, refresh_current_time)


def refresh_down_time():
    """刷新倒计时时间"""
    # 当前时间戳
    now_time = int(time.time())
    # 下班时间时分秒数据过滤
    work_hour_val = int(work_hour.get())
    if work_hour_val > 23:
        down_label.config(text='小时的区间为（00-23）')
        return
    work_minute_val = int(work_minute.get())
    if work_minute_val > 59:
        down_label.config(text='分钟的区间为（00-59）')
        return
    work_second_val = int(work_second.get())
    if work_second_val > 59:
        down_label.config(text='秒数的区间为（00-59）')
        return
    # 下班时间转为时间戳
    work_date = str(work_hour_val) + ':' + str(work_minute_val) + ':' + str(work_second_val)
    work_str_time = time.strftime('%Y-%m-%d ') + work_date
    time_array = time.strptime(work_str_time, "%Y-%m-%d %H:%M:%S")
    work_time = time.mktime(time_array)
    if now_time > work_time:
        down_label.config(text='已过下班时间')
        return
    # 距离下班时间剩余秒数
    diff_time = int(work_time - now_time)
    while diff_time > -1:
        # 获取倒计时-时分秒
        down_minute = diff_time // 60
        down_second = diff_time % 60
        down_hour = 0
        if down_minute > 60:
            down_hour = down_minute // 60
            down_minute = down_minute % 60
        # 刷新倒计时时间
        down_time = str(down_hour).zfill(2) + '时' + str(down_minute).zfill(2) + '分' + str(down_second).zfill(2) + '秒'
        down_label.config(text=down_time)
        tk_obj.update()
        time.sleep(1)
        if diff_time == 0:
            # 倒计时结束
            down_label.config(text='已到下班时间')
            # 自动关机，定时一分钟关机，可以取消
            # down_label.config(text='下一分钟将自动关机')
            # os.system('shutdown -s -f -t 60')
            break
        diff_time -= 1


# 程序主入口
if __name__ == "__main__":
    # 设置页面数据
    tk_obj = Tk()
    tk_obj.geometry('400x280')
    tk_obj.resizable(0, 0)
    tk_obj.config(bg='white')
    tk_obj.title('倒计时应用')
    Label(tk_obj, text='下班倒计时', font='宋体 20 bold', bg='white').pack()
    # 设置当前时间
    Label(tk_obj, font='宋体 15 bold', text='当前时间：', bg='white').place(x=50, y=60)
    curr_time = Label(tk_obj, font='宋体 15', text='', fg='gray25', bg='white')
    curr_time.place(x=160, y=60)
    refresh_current_time()
    # 设置下班时间
    Label(tk_obj, font='宋体 15 bold', text='下班时间：', bg='white').place(x=50, y=110)
    # 下班时间-小时
    work_hour = StringVar()
    Entry(tk_obj, textvariable=work_hour, width=2, font='宋体 12').place(x=160, y=115)
    work_hour.set('18')
    # 下班时间-分钟
    work_minute = StringVar()
    Entry(tk_obj, textvariable=work_minute, width=2, font='宋体 12').place(x=185, y=115)
    work_minute.set('00')
    # 下班时间-秒数
    work_second = StringVar()
    Entry(tk_obj, textvariable=work_second, width=2, font='宋体 12').place(x=210, y=115)
    work_second.set('00')
    # 设置剩余时间
    Label(tk_obj, font='宋体 15 bold', text='剩余时间：', bg='white').place(x=50, y=160)
    down_label = Label(tk_obj, font='宋体 23', text='', fg='gray25', bg='white')
    down_label.place(x=160, y=155)
    down_label.config(text='00时00分00秒')
    # 开始计时按钮
    Button(tk_obj, text='START', bd='5', command=refresh_down_time, bg='green', font='宋体 10 bold').place(x=150, y=220)
    tk_obj.mainloop()
