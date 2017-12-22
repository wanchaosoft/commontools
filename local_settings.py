#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 17:09'
__description__ = 'Django项目的本地设置，当同步代码后，在本地开发无需手动更改设置，需要在实际项目中，'
                  '将该文件加入`.gitignore`文件中'
"""
import os
from settings import LOG_DIR

# more info reference: https://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django#

DEBUG = True

# logging level: CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
LOGGING = {
    'version': '1.0.0',
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(relativeCreated)d %(created)f %(filename)s '
                      '%(levelno)s %(module)s %(funcName)s %(lineno)d %(msecs)d %(name)s %(message)s'
        },
        'simple': {
            'format': '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
        },
        'filehandler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, "service.log")
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console', 'filehandler'],
            'level': 'DEBUG',
        },
        'common': {
            'handlers': ['console', 'filehandler'],
            'level': 'WARNING',
        },
    }
}

