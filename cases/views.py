# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

def test_chinese(ch_str):
    """使用pinyin

    xpinyin插件主要是将汉字转为`拼音`
    """
    from xpinyin import Pinyin
    py = Pinyin()
    _ = py.get_pinyin(ch_str, splitter=' ')
    print(_)


def test_phone(num_str):
    """未经过验证"""
    import phonenumbers
    PhoneNumber = phonenumbers.parse(num_str, None)
    is_phone = phonenumbers.is_valid_number(PhoneNumber)
    return is_phone


def test_psutil():
    """监控系统信息"""
    import psutil
    # ############ about CPU ##############
    print(psutil.cpu_times())  # 系统时间
    print(psutil.cpu_percent())
    print(psutil.cpu_times_percent())
    print(psutil.cpu_count())
    print(psutil.cpu_stats())
    print(psutil.cpu_freq())
    # and others: memory, disk, network, sensors, Other system info, Process management

# 生成优惠码
import string
choices = string.ascii_uppercase + string.digits


if __name__ == '__main__':
    # test_chinese(u'郑王')
    # test_phone('17754913165')
    test_psutil()