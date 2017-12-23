#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:43'

from django.core.cache import cache
cache.set('my_key', 'hello, world!', 30)
cache.get('my_key') => 'hello, world!'
cache.set_many(['a', 'b']) =>
cache.get_many(['a', 'b']) => {'a': a_value, 'b': b_value}

cache.delete('a')
cache.delete_many(['a', 'b'])
cache.clear() => this will clear everything. Attention !!!


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



