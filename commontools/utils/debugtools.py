#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:42'

"""
from datetime import datetime

NOW = None


def print_time(msg=None):
    """打印时间"""
    global NOW
    if not NOW:
        NOW = datetime.now()
    if msg is None:
        msg = ''
    print('%s cost time: %s' % (msg, (datetime.now() - NOW).total_seconds()))



