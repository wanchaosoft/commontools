# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.geos import factory
from django.forms import inlineformset_factory, forms
from .mymodels import (Contact, Address)


"""
本模块主要是form的示例用法

validate field => validate form
"""

ContactAddressFormset = inlineformset_factory(Contact, Address)
# Contact is parent-form, Address is form.


# factory import path could be error
class ContactFactory(factory.Factory):
    FACTORY_FOR = Contact
    first_name = 'John'
    last_name = 'Smith'

# here no save
contact = ContactFactory.build()
contact = ContactFactory.build(last_name='Tom')

# save here
contact = ContactFactory.create()


class AddressFactory(factory.Factory):
    FACTORY_FOR = Address

    contact = factory.SubFactory(ContactFactory)

# ############################################################################


class ContactForm(forms.Form):
    """联系方式Form表单"""

    def __init__(self, *args, **kwargs):
        # 原form中可能多一个user信息，用作其他验证使用，但是实际form并不需要
        # 可以将该信息在``__init__``方法中复制给自身属性，然后从当中删除
        self._user = kwargs.pop('user')
        super(ContactForm, self).__init__(*args, **kwargs)

    # 可以在init中先拿到该参数值，然后从Form中删除
    class Meta:
        model = Contact
