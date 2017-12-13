#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:56'

"""


import json

from datetime import datetime

from django import forms
from django.shortcuts import HttpResponse

from rest_framework.authtoken.models import Token as AuthtokenToken

import logging

logger = logging.getLogger(__name__)


class LoginMixin(object):
    def dispatch(self, request, *args, **kwargs):
        info = {"msg": "",
                "code": "-1",
                "data": {}}
        token = request.META.get("HTTP_AUTHORIZATION", None)
        if not token:
            logger.exception(u"token字段缺失")
            logger.error(u"token字段缺失")
            info.update(**{'msg': u'token字段缺失'})
            return HttpResponse(json.dumps(info, ensure_ascii=False), status=401,
                                content_type=" application/json")
        AUTH_TOKEN = slice(6)
        token = token.split()[-1]
        try:
            token = AuthtokenToken.objects.get(key=token)
        except AuthtokenToken.DoesNotExist:
            return HttpResponse(json.dumps({"detail": u"认证令牌失效"}, ensure_ascii=False), status=401,
                                content_type=" application/json")

        else:
            if (datetime.now() - token.created).total_seconds() < 30 * 24 * 60 * 60:
                request.user = token.user
                token = AuthtokenToken.objects.filter(key=token)
                token.update(created=datetime.now())
                return super(LoginMixin, self).dispatch(request, *args, **kwargs)
            else:
                info["msg"] = u"token已过期"
                info["code"] = "1001"
                return HttpResponse(json.dumps(info, ensure_ascii=False), content_type=" application/json")


class ValidatorsMixin(object):
    SCHEMA = None

    def get_schema(self):

        class _CustomForm(forms.Form):
            pass

        if self.SCHEMA:
            for key, value in self.SCHEMA.items():
                _value = dict()
                _value.update(**value)
                _field_type = _value.pop("type")
                _CustomForm.declared_fields.update({key: getattr(forms, self.__reflection[_field_type])(**_value)})

        return _CustomForm

    def validator(self, param):
        return self.get_schema()(param)

    __reflection = {
        "int": "IntegerField",
        "string": "CharField",
        "email": "EmailField",
        "list": "ChoiceField",
        "datetime": "DateTimeField",
        "date": "DateField",
        "decimal": "DecimalField",
        "file": "FileField",
        "img": "ImageField",
        "regex": "RegexField"
    }

