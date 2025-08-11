#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/8/8 16:42  
"""

my_dict = {'a': 1, 'b': 2, 'c': 3}
b = my_dict.keys()
# print '1---', b
# my_dict['d']= 4
# print '2---', b

# print my_dict.keys()
print("---start", b)
my_dict['d']= 4
print("---end",b)
print (my_dict.keys())