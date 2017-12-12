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
        # pdb.set_trace()
        _pdb = pdb.Pdb()
        _pdb.set_trace(sys._getframe().f_back)


# TODO profile, pstats, hotshot, timeit 用来做性能分析
# profile 性能分析
# pstats 对profile分写结果输出到的文件 进行排序
# hotshot 补充profile时间不精确的问题（毫秒级别），但是不适用于多线程的代码
# timeit小巧实用



