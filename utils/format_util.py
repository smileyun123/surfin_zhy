#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/4 11:25  
"""
import re


def to_unicode_list(str_list):
    """
    将列表中的字符串转换为unicode
    :param str_list:
    :return:
    """
    return [u"{}".format(s) for s in str_list]


new_mobiles_set = set()
def _process_mobile(x):
    """
     mobile预处理函数：把输入mobile统一转为小写，并删除所有非字母数字字符
    """
    x= x.encode('utf-8') if isinstance(x, unicode) else x
    if isinstance(x, str):
        x = re.sub('\W', '', x.lower())
    if x and len(x) > 2:
        return x
    else:
        return None

if __name__ == '__main__':

    mm = [[12345,555,6666, 'ad'], [12345,555,6666, 'AD']]
    for m in mm:
        new_mobile = _process_mobile(m)

        print new_mobile
        if not str(new_mobile).isdigit():
            new_mobiles_set.add(str(new_mobile))

        for i in new_mobiles_set:
            print '==', i
        print new_mobiles_set