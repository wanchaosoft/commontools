#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:43'

"""


def cache_filter(queryset, **option):
    """queryset 缓存filter"""
    return [query for query in queryset if all(getattr(query, k) == v for k, v in option.iteritems())]


def cache_get(queryset, **option):
    """queryset 缓存get"""
    result = cache_filter(queryset, **option)
    if len(result) != 1:
        raise ValueError("get should return one record, but now:%s" % len(result))
    return result[0]



