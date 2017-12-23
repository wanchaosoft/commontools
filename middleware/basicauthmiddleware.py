#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/18 17:03'

MiddleWare 继承自object
generally hooks:
request
response
session
view
template_response
exception

used to:
Sessions
Authentication
CSRF Protection
GZipping Content

"""

# request中间件会按顺序执行
# 1.返回`None`,继续执行


# response中间件会逆序执行
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


class BasicAuthMiddleware(object):
    """
    中间件继承`object`而不是`view`
    """
    def process_request(self, request):
        authentication = request.META.get('HTTP_AUTHORIZATION')
        if authentication:
            (authmeth, auth) = authentication.split(' ', 1)
            if 'basic' == authmeth.lower():
                auth = auth.strip().decode('base64')
                username, password = auth.split(':', 1)
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)


class LocaleMiddleware(object):

    def process_request(self, request):

        if 'locale' in request.cookies:
            request.locale = request.cookies.locale
        else:
            request.locale = None

    def process_response(self, request, response):

        if getattr(request, 'locale', False):
            response.cookies['locale'] = request.locale


