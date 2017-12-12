#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/12 16:28'
__description__ = '使用 Python 生成字母验证码图片'
参考资料: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
https://github.com/JiYouMCC/python-show-me-the-code

文件重命名
xml 和 excel互相转换
"""
# todo 每日一练 25题
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255,255,255)
Image_Font = 'arial.ttf'
text = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ',4))

def colorRandom():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))


#change 噪点频率（%）
def create_identifying_code(strs, width=400, height=200, chance=2):
    im = Image.new(IMAGE_MODE, (width, height), IMAGE_BG_COLOR)
    draw = ImageDraw.Draw(im)
    #绘制背景噪点
    for w in xrange(width):
        for h in xrange(height):
            if chance < random.randint(1, 100):
                draw.point((w, h), fill=colorRandom())

    font = ImageFont.truetype(Image_Font, 80)
    font_width, font_height = font.getsize(strs)
    strs_len = len(strs)
    x = (width - font_width)/2
    y = (height - font_height)/2
    #逐个绘制文字
    for i in strs:
        draw.text((x,y), i, colorRandom(), font)
        x += font_width/strs_len
    #模糊
    im = im.filter(ImageFilter.BLUR)
    im.save('identifying_code_pic.jpg')


if __name__ == '__main__':
    create_identifying_code(text)



