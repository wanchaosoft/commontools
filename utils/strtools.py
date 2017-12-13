#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:53'

"""


def find_all_index_in_str(str, substr):
    findall = lambda s, sub: filter(lambda i: s[i:].startswith(sub), range(len(s)))
    res = findall(str, substr)
    return res

