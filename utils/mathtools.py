#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:44'

"""


def check_phone(s):
    """校验手机号码合法性"""
    phone_prefix = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
                    '150', '151', '152', '153', '154', '155', '156', '157', '158', '159',
                    '170', '171', '172', '173', '174', '175', '176', '177', '178', '179',
                    '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', ]
    if len(s) != 11:
        return False
    else:
        if s.isdigit():
            if s[0] != '1':
                return False
            if s[:3] not in phone_prefix:
                return False
        else:
            return False
        return True
