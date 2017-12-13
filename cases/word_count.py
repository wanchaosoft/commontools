#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-13 11:03:08
# @Author  : Daedrath (Daedrath@outlook.com)
# @Link    : http://www.daedrath.site
# @Version : $Id$

# **任一个英文的纯文本文件，统计其中的单词出现的个数


def read_txt():
    u"""将文本文件中的单词分组"""
    with open('static/test_word_count.txt', 'rt') as rf:
        strings = rf.read()
    return strings

def group_word(txt_str):
    u"""将文本文件中的单词分组"""
    import string
    single_letter = string.letters
    others = []
    for txt in txt_str:
        if txt not in single_letter:
            others.append(txt)
    others = list(set(others))

    others.extend(['\r', '\r\n', '\n'])
    for other in others:
        txt_str.replace(other, ' ')
    result = txt_str.split(' ')
    return result


def count_word(word_list):
    u"""按分组统计次数，并返回数据"""
    result = {}
    for word in list(set(word_list)):
        _count = word_list.count(word)
        result[word] = _count
    return result

def write_result(count_result):
    u"""将统计结果写入文本文档"""
    result = '================== count result ================\n'
    for k, v in count_result.iteritems():
        result += ''.join(['"', str(k), '" ','happen: ', str(v), ' times.\n'])

    with open('static/test_word_count.txt', 'a+') as aw:
        aw.write(result)
    return result

def main():
    u"""测试主函数"""
    strings = read_txt()
    group_words = group_word(strings)
    count_result = count_word(group_words)
    write_result(count_result)


if __name__ == '__main__':
    main()
