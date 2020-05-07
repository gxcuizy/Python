#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用matplotlib和numpy绘图
author: gxcuizy
date: 2018-11-14
"""

from matplotlib import pyplot
import numpy


def fun_1():
    """画一个基础x-y的坐标轴"""
    x = numpy.linspace(-1, 1, 50)
    y = 2 * x + 1
    # 定义图像窗口
    pyplot.figure()
    pyplot.plot(x, y)
    # 显示图像
    pyplot.show()


def fun_2():
    """x-y的坐标轴设置属性"""
    x = numpy.linspace(-1, 1, 50)
    y = x ** 2
    # 定义图像窗口
    pyplot.figure()
    # color属性设置颜色，linewidth属性设置线条宽度像素，linestyle属性设置线条样式
    pyplot.plot(x, y, color='red', linewidth=1, linestyle=':')
    # 显示图像
    pyplot.show()


def fun_3():
    """设置坐标轴的范围, 单位长度, 替代文字"""
    x = numpy.linspace(-1, 1, 50)
    y = x ** 2
    # 定义图像窗口
    pyplot.figure()
    # color属性设置颜色，linewidth属性设置线条宽度像素，linestyle属性设置线条样式
    pyplot.plot(x, y, color='red', linewidth=1, linestyle=':')
    # 使用pyplot.xlim()设置x坐标轴范围
    pyplot.xlim(-1, 2)
    # 使用pyplot.ylim()设置y坐标轴范围
    pyplot.ylim(-1, 2)
    # 使用pyplot.xlabel()设置x坐标轴名称
    pyplot.xlabel('this is X')
    # 使用pyplot.ylabel()设置y坐标轴名称
    pyplot.ylabel('this is Y')
    # pyplot.xticks()设置x轴刻度
    # pyplot.yticks()设置y轴刻度
    # 显示图像
    pyplot.show()


def fun_4():
    """设置显示图例"""
    x = numpy.linspace(-1, 1, 50)
    y = x ** 2
    y1 = x * 2 + 1
    # 定义图像窗口
    pyplot.figure()
    # color属性设置颜色，linewidth属性设置线条宽度像素，linestyle属性设置线条样式
    pyplot.plot(x, y, color='red', label='linear line')
    pyplot.plot(x, y1, color='purple', label='upper line')
    # 使用pyplot.xlim()设置x坐标轴范围
    pyplot.xlim(-1, 2)
    # 使用pyplot.ylim()设置y坐标轴范围
    pyplot.ylim(-1, 2)
    # 使用pyplot.xlabel()设置x坐标轴名称
    pyplot.xlabel('this is X')
    # 使用pyplot.ylabel()设置y坐标轴名称
    pyplot.ylabel('this is Y')
    # pyplot.xticks()设置x轴刻度
    # pyplot.yticks()设置y轴刻度
    # pyplot.legend()这是图例显示位置
    pyplot.legend(loc='upper right')
    # 显示图像
    pyplot.show()


def fun_5():
    """移动坐标轴、添加注释"""
    x = numpy.linspace(-3, 3, 50)
    y = x * 2 + 1
    pyplot.figure()
    pyplot.plot(x, y)
    # 设置上和下边框颜色
    ax = pyplot.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 移动坐标轴
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    # 做一条垂直线
    xx = 1
    yy = 2 * xx + 1
    pyplot.plot([xx, xx, ], [0, yy, ], '--', linewidth=2, color='red')
    pyplot.scatter([xx, ], [yy, ], s=50, color='black')
    # annotate添加注释
    pyplot.annotate(r'$2x+1=%s$' % yy, xy=(xx, yy), xycoords='data', xytext=(+30, -30), textcoords='offset points',
                    fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
    # text添加注释
    pyplot.text(-3.4, 3, r'$This\ is\ the\ some\ text.$', fontdict={'size': 16, 'color': 'r'})
    # 显示图像
    pyplot.show()


def fun_6():
    """Scatter 散点图"""
    n = 1024
    # 随机生成1024个x坐标值
    x = numpy.random.normal(0, 1, n)
    # 随机生成1024个y坐标值
    y = numpy.random.normal(0, 1, n)
    # 颜色值
    t = numpy.arctan2(y, x)
    # s为大小，c设置颜色，alpha设置透明度
    pyplot.scatter(x, y, s=20, c=t, alpha=5)
    pyplot.xlim(-1.5, 1.5)
    pyplot.ylim(-1.5, 1.5)
    # 利用pyplot.xtick()、pyplot.ytick()函数来隐藏坐标轴
    pyplot.xticks(())
    pyplot.yticks(())
    # 显示图像
    pyplot.show()


def fun_7():
    """Bar 柱状图"""
    # 生成12个整数
    n = 12
    X = numpy.arange(n)
    # 获取两个随机数据
    y1 = (1 - X / float(n)) * numpy.random.uniform(0.5, 1.0, n)
    y2 = (1 - X / float(n)) * numpy.random.uniform(0.5, 1.0, n)
    pyplot.bar(X, +y1)
    pyplot.bar(X, -y2)
    # 设置x坐标轴
    pyplot.xlim(-5, n)
    pyplot.xticks(())
    # 设置y坐标轴
    pyplot.ylim(-1.25, 1.15)
    pyplot.yticks(())
    # 设置颜色
    pyplot.bar(X, +y1, facecolor='#9999ff', edgecolor='white')
    pyplot.bar(X, -y2, facecolor='#ff9999', edgecolor='white')
    # 添加数值
    for x, y in zip(X, y1):
        pyplot.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X, y2):
        pyplot.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    # 显示图像
    pyplot.show()


def fun_8():
    """Image 图片"""
    # 用这样 3x3 的 2D-array 来表示点的颜色
    a = numpy.array(
        [0.313660827978, 0.365348418405, 0.423733120134, 0.365348418405, 0.439599930621, 0.525083754405, 0.423733120134,
         0.525083754405, 0.651536351379]).reshape(3, 3)
    pyplot.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
    pyplot.colorbar(shrink=.92)
    # 去掉xy的刻度
    pyplot.xticks(())
    pyplot.yticks(())
    # 显示图像
    pyplot.show()


# 程序主入口
if __name__ == '__main__':
    fun_8()
