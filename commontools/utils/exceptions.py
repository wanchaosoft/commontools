#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/12 10:28'

"""


class RuntimeError(Exception):
    """定义一个运行时异常"""
    pass


def example1():
    try:
        int('N/A')
    except ValueError as e:  # 在捕获一个异常后抛出另外一个异常
        raise RuntimeError('A parsing error occurred')  # 这样写会打印出两种异常的堆栈信息
        # raise RuntimeError() from e  # 这样写会打印出两种异常的堆栈信息 适用于3.*
