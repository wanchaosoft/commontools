#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-13 13:36:36
# @Author  : Daedrath (Daedrath@outlook.com)
# @Link    : http://www.daedrath.site
# @Version : 0.0.1

# **你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小（可以复用）

from PIL import Image


def parse_img(img_path):
    u"""解析图片的基本信息"""
    im = Image.open(img_path)
    return im, im.format, im.size


def calc_size(image, old_size, standard_size):
    u"""计算新的图片尺寸(尽可能大)"""
    old_ = list(old_size)
    new_ = list(standard_size)
    tmp1 = float(old_[0]) / new_[0]
    tmp2 = float(old_[1]) / new_[1]
    if tmp1 < 1 and tmp2 < 1:
        return old_size
    if tmp1 > tmp2:
        return new_[0], old_[1] / tmp1
    else:
        return old_[0] / tmp2, new_[1]


def resize_image(image, sizes, destination):
    u"""重新尺寸"""
    length, height = sizes
    image.thumbnail((length, height))
    image.save(destination, 'jpeg')


def main():
    u"""主函数"""
    img_path = 'static/test_img.jpg'
    image, formater, origin_size = parse_img(img_path)
    print(image, formater, origin_size)
    standard_size = (1136, 640)  # iphone5 pixel
    length, height = calc_size(image, origin_size, standard_size)
    destination = 'static/final.jpeg'
    resize_image(image, (length, height), destination)


if __name__ == '__main__':
    main()
