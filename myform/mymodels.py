#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块主要是配合myforms示例用，同时作为Model的示例用法

Model有这几种方法： get_queryset(), get_object(), get_success_url()

"""

from django.db import models
from django.db.models import Manager



class ContactManager(Manager):
    """Contact的管理类"""
    pass

    def get_queryset(self):
        """Override Manager.get_queryset() method"""
        pass


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Address(models.Model):

    contact = models.ForeignKey(Contact)
    address_type = models.CharField(
        max_length=10,
    )
    address = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    state = models.CharField(
        max_length=2,
    )
    postal_code = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return "%s %s" % (self.address_type, self.address)

    class Meta:
        unique_together = ['address_type', 'contact']  # 索引
        ordering = ['state']  # 默认排序字段
