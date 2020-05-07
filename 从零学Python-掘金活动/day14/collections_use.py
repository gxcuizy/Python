#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
常见的内建模块练习之collections
author: gxcuizy
date: 2018-10-30
"""

import collections

# 程序主入口
if __name__ == '__main__':
    # collections提供了很多的集合类

    # 使用nametuple()可以定义一个tuple对象，并且规定了tuple的个数
    point = collections.namedtuple('point', ['x', 'y'])
    p = point(1, 2)
    print(p)
    # 可以直接访问tuple的元素值
    print(p.x)
    print(p.y)

    # deque()可以高效实现列表的插入和删除操作的双向类表
    deque = collections.deque(['x', 'y'])
    # append()添加元素，还支持pop()删除元素，以及appendleft()、popleft()
    deque.append('z')
    print(deque)
    print(list(deque))

    # defaultdict()可以为字典设置一个默认值，也就是访问不存在的key时返回的默认值
    test_dict = collections.defaultdict(lambda: '0')
    test_dict['ttt'] = '666'
    print(test_dict)
    print(test_dict['ttt'])
    print(test_dict['t'])

    # OrderedDict()可以对字典进行排序，排序规则是插入的顺序
    origin_dict = dict([('a', 111), ('b', 222), ('c', '333')])
    print(origin_dict)
    # 排序
    order_dict = collections.OrderedDict(origin_dict)
    print(order_dict)
    print(order_dict.keys())
    print(order_dict.values())

    # Counter()是个简单的计数器
    counter = collections.Counter()
    print(counter)
    for value in 'hello python':
        counter[value] = counter[value] + 1
        print(value)
    print(counter)
