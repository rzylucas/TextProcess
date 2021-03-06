#!/usr/bin/python3
# -*-coding:utf-8 -*-
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import
#Reference:**********************************************
# @Time     : 2019-09-30 12:48
# @Author   : 病虎
# @E-mail   : victor.xsyang@gmail.com
# @File     : test.py
# @User     : ora
# @Software: PyCharm
# @Description: 
#Reference:**********************************************

import TextProcess.TextProcess as tp


if __name__ == '__main__':
    test_string = '我😍愛你中華https://<a></a>,,,,,, Hello Word 121233124234213 [sdfsd]{}【】'
    test = tp.TextProcess()
    # 英文字母大写转小写
    print(test.strLower(test_string))
    # '我😍你中华<http://><a></a>, hello word。'

    # 中文繁体转简体
    print(test.Tra2Sim(test_string, 'zh-hans'))

    # 中文简体转繁体
    print(test.Tra2Sim(test_string, 'zh-hant'))

    # 全角转半角
    print(test.strQ2B(test_string))

    # 去除emotion表情
    print(test.replace_emotion(test_string,""))

    # 将emotion表情替换成文字描述
    print(test.convert_emotion(test_string))

    # 去除控制字符
    print(test.replace_control_character(test_string, ''))

    # 去除超链接tag，href
    print(test.remove_ahref(test_string, ''))

    # 去除http超链接
    print(test.remove_http(test_string, ''))

    # 将长数字转换成特殊字符
    print(test.replace_long_num(test_string, 'LONG_NUM'))

    # 过滤括号及括号内的内容【xxxxx】/（xxxxxxx）/ [xxxx] 【.*】|（.*）|\[.*\]
    print(test.replace_brackets(test_string, ''))

    # 过滤连续标点和空格
    print(test.remove_commas(test_string))

    # 只保留中文字符
    print(test.remove_not_che(test_string))

    # 保留中文和英文
    print(test.keep_chi_eng(test_string, ''))

    # 保留中文和英文及数字
    print(test.keep_chi_eng_num(test_string, ''))

    # 一条龙服务 基本过滤
    print(test.evaluate(test_string, 'OnlinePipe'))

    #一条龙服务 强过滤
    print(test.evaluate(test_string, 'OnlinePipeStrictMore'))

    #一条龙服务 极强过滤
    print(test.evaluate('', 'OnlinePipeStrictMost'))

