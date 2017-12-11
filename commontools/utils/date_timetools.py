#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:45'

"""
import time

from datetime import timedelta


def date_during(begin_time, end_time):
    time_during = time.mktime(end_time.timetuple())-time.mktime(begin_time.timetuple())
    return time_during


def change_time(all_time):
    """将时间以`时`, `分`, `秒` 的形式展现出来

    in: 12200  # type: int
    out: 1天12时37秒  # type: str
    """
    day = 24 * 60 * 60
    hour = 60 * 60
    minute = 60
    if all_time > day:
        days = divmod(all_time, day)
        return u"%d天 %s" % (int(days[0]), change_time(days[1]))
    elif all_time > hour:
        hours = divmod(all_time, hour)
        return u'%d时%s' % (int(hours[0]), change_time(hours[1]))
    else:
        minutes = divmod(all_time, minute)
        return u"%d分" % (int(minutes[0]))


def weekday_start_end_date(base_date=None, is_range_needed=None, choice=None):
    """一周内的统计其实时间计算

    根据给定日期计算
    :param choice: 计算类型 有三种如下：
        1: 本周
        2: 上周
        3: 前7天
    :param is_range_needed: 是否需要计算每天的日期（默认只计算起止日期）
    :param base_date: date 不支持datetime类型, 默认为当前日期
    :param choice: int 针对以上几种情况进行选择，默认为本周（choices=1）
    """
    _choice = ['this_week', 'last_week', 'last_seven', ]
    if not base_date:
        raise NotImplementedError(u"未提供起始日期")
    if not choice:
        choice = 'this_week'
    if choice not in _choice:
        raise IndexError(u"要计算的类型选择错误")
    if choice == 'this_week':
        start_date = base_date + timedelta(days=-base_date.weekday())  # 本周一
        end_date = base_date + timedelta(days=-base_date.weekday()+7)  # 本周日
    elif choice == 'last_week':
        start_date = base_date + timedelta(days=-base_date.weekday() - 7)  # 上周一
        end_date = base_date + timedelta(days=-base_date.weekday()-1)  # 上周日
    else:
        start_date = base_date + timedelta(days=-7)  # start
        end_date = base_date

    if is_range_needed:
        return [start_date + timedelta(days=num) for num in range(0, 7)]
    else:
        return start_date, end_date


def gen_percent(numbers, digital=None):
    """计算百分比

    :param numbers a list of int
    :return result a list of percentage
    """
    # TODO 将保存的小数位数作为参数
    if len(numbers) < 1:
        return False
    s = sum(numbers)
    percent = [float(x * 100) / s for x in numbers]
    r = [int(round(x)) for x in percent]
    decimal = [(percent[x] - r[x], x) for x in range(len(r))]
    modifier = 100 - sum(r)
    if modifier > 0:
        decimal = sorted(decimal, reverse=True)
        for i in range(modifier):
            r[decimal[i][1]] += 1
    elif modifier < 0:
        decimal = sorted(decimal)
        for i in range(-1 * modifier):
            r[decimal[i][1]] -= 1
    return r

