#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:42'

"""
from datetime import datetime
import os
import sys
NOW = None


def print_time(msg=None):
    """打印时间"""
    global NOW
    if not NOW:
        NOW = datetime.now()
    if msg is None:
        msg = ''
    print('%s cost time: %s' % (msg, (datetime.now() - NOW).total_seconds()))


def debugger():
    """在启动debug模式下，启动pdb调试
    生产环境DEBUG=False，自动禁用pdb调试
    """
    try:
        debug = eval(os.environ.get('DEBUG'))
    except:
        debug = False

    if debug:
        import pdb
        pdb.set_trace()
        # _pdb = pdb.Pdb()
        # _pdb.set_trace(sys._getframe().f_back)


# TODO profile, pstats, hotshot, timeit 用来做性能分析
# profile 性能分析
# pstats 对profile分写结果输出到的文件 进行排序
# hotshot 补充profile时间不精确的问题（毫秒级别），但是不适用于多线程的代码
# timeit小巧实用


# #### 性能优化的前提 ####
# • 保证程序正确
# • 可信赖的测试
# • 有收益

# • pstats 可用于解析 cProfile 生成的二进制文件
# • python –m cProfile –o bar.prof bar.py
# • graphviz
# • python gprof2dot.py -f pstats bar.prof | dot -Tpng
# -o bar_result.png

# • pip install line_profiler
# • @profile

# • pip install vprof
# • vprof -c <config> <src>

import timeit

def test():
    pass


def test_timeit():
    x = 0
    for i in range(1000000):
        x += 1
    print(x)

if __name__ == '__main__':
    # timeit 用法，可以打印出 代码片段/函数 消耗的时间
    timeit.timeit(stmt='test_timeit()', setup='from __main__ import test_timeit;')


