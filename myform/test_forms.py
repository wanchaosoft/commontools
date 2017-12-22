#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from myform.myforms import ContactForm

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/22 16:09'

"""


class ContactFormTest(unittest.TestCase):
    """ContactForm 单元测试"""
    def test_validation(self):
        form_data = {
            'name': 'x' * 11,
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.instance.name, 'x' * 11)


    def test_validation2(self):

        from rebar.testing import flatten_to_dict

        form_data = flatten_to_dict(ContactForm())  # 将form表单转换为dict{}
        form_data.update({
                    'name': 'x' * 11,
                })
        form = ContactForm(data=form_data)
        assert(not form.is_valid())


from django.forms.utils import ErrorList


class ParagraphErrorList(ErrorList):
    """Not clear"""

    def __str__(self):
        return self.as_paragraphs()

    def as_paragraphs(self):
        return "<p>%s</p>" % (",".join((e for e in self.errors)))
