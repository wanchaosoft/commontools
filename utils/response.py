#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 17:01'
__description__ = '基于rest_framework的返回'
"""


from rest_framework.response import Response


def response(data, msg='ok', status=True, **kwargs):
    if status is True:
        status = "1"
    elif type(status) == int:
        status = status
    else:
        status = "-1"
    return Response({'data': data, 'status': status, 'msg': msg}, **kwargs)


def json_format(data):

    data = [{k: ''.join(v[0])} for k, v in data.items() if isinstance(v, list)]

    return data, data[0].keys()[0]



