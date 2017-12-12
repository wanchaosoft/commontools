#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:46'

"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage, Page


def pager(objects, page=1, size=10):
    """这种分页，每次都会执行count操作（比较耗时）"""
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


class MyPaginator(object):  # 源码复制出来，进行删减和调整
    def __init__(self, object_list, per_page):
        self.object_list = object_list
        self.per_page = int(per_page)

    @staticmethod
    def validate_number(number):
        """
        Validates the given 1-based page number.
        """
        try:
            number = int(number)
        except (TypeError, ValueError):
            raise PageNotAnInteger('This page number is not an integer!')
        if number < 1:
            raise EmptyPage('This page number is less than 1!')
        return number

    def page(self, number):
        """
        Returns a Page object for the given 1-based page number.
        """
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        return self._get_page(self.object_list[bottom:top], number, self)

    @staticmethod
    def _get_page(*args, **kwargs):
        """
        Returns an instance of a single page.
        This hook can be used by subclasses to use an alternative to the
        standard :cls:`Page` object.
        """
        return Page(*args, **kwargs)


def my_paginator(objects, page, size=10):
    paginator = MyPaginator(objects, size)
    return paginator.page(page)
# todo 不返回总页数，校验下一页，适用于手机APP下滑的操作

