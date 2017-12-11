#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:46'

"""


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


def pager(objects, page=1, size=10):
    """分页"""
    paginator = Paginator(objects, size)
    try:
        res = paginator.page(page)

    except PageNotAnInteger:
        res = paginator.page(1)

    except EmptyPage:
        res = paginator.page(paginator.num_pages)
    if int(page) > int(paginator.num_pages):
        res = []
    return res, str(paginator.num_pages), str(paginator.count)


# todo 不返回总页数，校验下一页，适用于手机APP下滑的操作

