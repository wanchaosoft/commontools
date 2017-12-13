from __future__ import unicode_literals

"""
By apps.py's Config class's ready method,
you can execute some code once startup.

At the time, `__init__.py` need to place some code for init your code.

"""
from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = 'utils'
    verbose_name = 'Utils'

    def ready(self):
        pass  # startup code here.


