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


def new_response_v2(data, msg='ok', status=True, **kwargs):
    if status is True:
        status = "1"
    elif type(status) == int:
        status = str(status)
    else:
        status = "-1"
    return Response({'data': data, 'status': status, 'msg': msg}, **kwargs)


def new_response(data, msg='ok', status=True, **kwargs):
    if status is True:
        status = "1"
    elif type(status) == int:
        status = str(status)
    else:
        status = "-1"
    return Response({'data': data, 'code': status, 'msg': msg}, **kwargs)


def json_format(data):

    data = [{k: ''.join(v[0])} for k, v in data.items() if isinstance(v, list)]

    return data, data[0].keys()[0]


def ErrorResponse(data, msg='ok', status=True):

    data, key = json_format(data)

    if status and type(status) != int:
        status = "1"

    elif type(status) == int:
        status = status
    else:
        status = "-1"

    return Response({'data': {}, 'status': status, 'msg': data[0].values()[0]})


def FireErrorResponse(data, msg='ok', status=True):
    data, key = json_format(data)

    if data[0].values()[0] == u'字段缺失':
        status = "-1"

    if data[0].values()[0] != u'字段缺失' and status and type(status) != int:
        status = "1"

    elif type(status) == int:
        status = str(status)

    else:
        status = "-1"

    return Response({'data': {}, 'code': status, 'msg': data[0].values()[0]})


