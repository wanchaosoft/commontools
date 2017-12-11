#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:45'
__description__ = '上传文件'
"""


import uuid
import os
from django.conf import settings


def upload_file(location=None, _file=None):

    # store
    file_uuid = uuid.uuid1()

    tmp = _file.name.split('.')
    tmp.reverse()
    file_name = str(file_uuid) + '.' + tmp[0]

    str_origin = ''
    for i in location:
        if str_origin == '':
            str_origin = i
            _base_url = i
        else:
            _base_url = os.path.join(_base_url, i)

    if os.path.exists(_base_url):
        pass
    else:
        os.makedirs(_base_url)

    des_url = os.path.join(_base_url, file_name)

    with open(des_url, 'wb+') as f:
        # default 2.5 Mb
        for chunk in _file.chunks():
            f.write(chunk)
    res = des_url.split('static')
    tmp = res[1].replace('\\', '/')
    final = 'static' + tmp
    return final


def get_file_dir(location_list=None, file_suffix=None):
    """获取指定目录下的文件完整路径

    :param location_list: 文件绝对路径（列表形式）
    :param file_suffix: 文件后缀名
    :return:
    """

    try:
        for location in location_list:
            try:
                _base_dir = os.path.join(_base_dir, location)
            except:
                _base_dir = location

        if os.path.exists(_base_dir):
            pass
        else:

            raise BaseException
        _file_name = os.listdir(_base_dir)

        for single in _file_name:
            if file_suffix in single:
                file_name = single
            else:
                file_name = ''

        path_comp = os.path.join(_base_dir, file_name)

        res = path_comp.split('static')[1].replace('\\', '/')

        path_final = 'static' + res
        return path_final
    except Exception:
        raise BaseException


def handler_upload_image_list(location=None, multiple_file=None, separator='|'):
    """

    :param location: absolute location wanting upload file
    :param multiple_file: file body
    :param separator: for example: ',', '|', '.', etc.
    :return: string（include multiple location separated by separator）
    """

    picture_location_list = []
    for picture in multiple_file:
        if picture:
            temp_location = upload_file(location, picture)
            picture_location_list.append(temp_location)

    res = separator.join(picture_location_list)

    return res


def _is_file(path):
    """

    :param path: str 文件服务器路径
    :return: True if is File else False
    """
    _base = settings.STATICFILES_DIRS[0]
    if 'static' not in path:
        raise Exception('The destination path is not exists.')

    res = _base + path.split('static')[1]

    if os.path.exists(res):
        return res
    return ''


def _del_file(absolute_path):
    os.remove(absolute_path)


def del_file(paths=None):
    """
    删除文件

    :param paths: where file in
    :return: None
    """
    if isinstance(paths, list):
        for path in paths:
            tmp = _is_file(path)
            if tmp:
                _del_file(tmp)
    else:
        is_file = _is_file(paths)
        if is_file:
            _del_file(is_file)
    return True


