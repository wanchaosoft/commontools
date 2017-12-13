#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:58'

"""

# 下面是Jpush(极光推送的使用示例)：

# import jpush as jpush
# import requests
# APPKEY = "123"
# MASTERSECRET = "123"
# HOST = 'http://sdk.open.api.igexin.com/apiex.htm'
#
#
# def send_push(tagname, msg):
#     _jpush = jpush.JPush(APPKEY, MASTERSECRET)
#     push = _jpush.create_push()
#     push.audience = jpush.audience(jpush.tag(tagname))
#     ios = jpush.ios(alert=str(msg), sound='default')
#     android = jpush.android(alert=str(msg))
#     push.notification = jpush.notification(alert=str(msg), android=android, ios=ios)
#     push.options = {"time_to_live": 86400, "apns_production": True}
#     push.platform = jpush.all_
#     try:
#         response = push.send()
#     except Exception as e:
#         print(e)
#
#     # except common.Unauthorized:
#     #    raise common.Unauthorized("Unauthorized")
#     # except common.APIConnectionException:
#     #    raise common.APIConnectionException("conn error")
#     # except common.JPushFailure:
#     #    print ("JPushFailure")
#     # except:
#     #    print ("Exception")
# sendpush('owner_id_3502030002', 'hello world')


# def send_code(phone, code, code_type=1):
#     """云片网发送短信代码示例"""
#     if code_type == 1:
#         payload = {
#             'mobile': phone,
#             'apikey': '123***',
#             'text': '【***】您的登陆密码为%s，请使用您的手机号作为用户名登陆APP。' % code,
#             }
#     elif code_type == 2:
#         payload = {
#             'mobile': phone,
#             'apikey': '123***',
#             'text': '【***】您的验证码为%s，该验证码30分钟内有效。' % code,
#             }
#
#     res = requests.post('https://sms.yunpian.com/v1/sms/send.json', payload)
#     return res

