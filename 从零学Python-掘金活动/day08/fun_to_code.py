#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
高阶函数的练习和使用（map()、reduce()、sorted()函数）
author: gxcuizy
date: 2018-10-22
"""

from functools import reduce
import functools
import time


def a(x):
    """计算一个数的平方"""
    return x ** 2


def b(x, y):
    """拼接字符串"""
    return str(x) + str(y)


def c(x):
    """首字母大写"""
    return x.title()


def d(x, y):
    """计算两个数的积"""
    return x * y


def e(x):
    """判断是否是偶数"""
    return x % 2 == 0


def f(x):
    """判断是否是回数"""
    x = str(x)
    mid = int(len(x) / 2)
    i = 0
    while i < mid:
        if x[i] != x[-(i + 1)]:
            return False
        i += 1
    return True


def g(x):
    """获取第一个元素"""
    return x[0]


def h(x):
    """获取第二个元素"""
    return x[1]


def i(x):
    """定义一个返回函数"""

    def j():
        return '这是返回函数的输出：%s' % x

    return j


def k(func):
    """定义一个装饰器函数"""

    def m(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return m


@k
def n():
    print('这是后输出')


def o(func):
    """定义一个装饰器，获取函数执行时间"""

    @functools.wraps(func)
    def p(*args, **kw):
        print('%s excuted time is %s' % (func.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return func(*args, **kw)

    return p


@o
def q(x):
    """计算一个数的平方"""
    return x ** 2


# 程序主入口
if __name__ == '__main__':
    # 利用map()计算1-9的平方结果
    square_list = map(a, range(1, 10))
    print(list(square_list))

    # 利用map()计算一堆字符串的长度
    str_list = ['123', '6666', 'hello', 'world']
    str_len = map(len, str_list)
    print(list(str_len))

    # 利用reduce()拼接字符串
    str_result = reduce(b, str_list)
    print(str_result)

    # 格式化，列表元素首字母大写
    list_info = ['adam', 'LISA', 'barT']
    format_result = map(c, list_info)
    print(list(format_result))

    # 利用reduce()计算一个列表元素的积
    prod_result = reduce(d, range(1, 10))
    print(prod_result)

    # 利用filter()过滤数据，过滤奇数
    even_list = filter(e, range(1, 10))
    print(list(even_list))

    # 过滤不是回数的数字
    num_list = [123321, 99899, 1234, 66988, 68968, 66966]
    re_list = filter(f, num_list)
    print(list(re_list))

    # 使用sorted()排序
    print(sorted(num_list))

    # 通过key自定义排序
    print(sorted(num_list, key=a))

    # 字母排序-默认ASCII
    print(sorted(['bob', 'about', 'Zoo', 'Credit']))
    # 统一转为小写，再排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    # 反向排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

    # 学生成绩，按照姓名排序
    stu_list = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(stu_list, key=g))
    # 按照成绩高低排序
    print(sorted(stu_list, key=h, reverse=True))

    # 调用函数，返回一个函数
    fun_name = i(666)
    print(fun_name)
    print(fun_name())

    # lambda匿名函数的使用
    # 匿名函数，只能是一个表达式
    print(list(map(lambda x: x ** 2, range(1, 9))))

    # 用匿名函数过滤不是偶数的列表元素
    print(list(filter(lambda x: x % 2 == 0, range(1, 9))))

    # 函数赋值给一个变量
    aa = a
    print(aa(4))

    # __name__属性获取函数名
    print(a.__name__)
    print(aa.__name__)

    # 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator），本质上，装饰器就是一个返回函数的高阶函数
    n()

    # 利用装饰器，获取程序执行时间
    print(q(7))

    # functools.partial可以创建一个新的函数,即偏函数的用法
    int2 = functools.partial(int, base=2)
    print(int2('100'))
