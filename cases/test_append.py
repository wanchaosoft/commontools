#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import (datetime, date, timedelta)


curr = datetime.now()


def log_time(msg):
    global curr
    tmp = datetime.now() - curr
    print(msg + " cost: %s" % tmp.seconds)
    curr = datetime.now()


def test_plus():
    first = ''
    log_time("start")
    for i in range(10000000):
        first += '1'
    log_time("end")
    # print first


def test_join():
    first = ''
    log_time("start join")
    for i in range(10000000):
        first = ''.join([first, '1'])
    log_time("end join")
    # print first



if __name__ == "__main__":
    # test_plus()
    test_join()
