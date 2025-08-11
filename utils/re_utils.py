#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/1 15:45  
"""
import re



# 预编译正则表达式
pattern = re.compile(r'[^a-zA-Z0-9]')  # 匹配非字母数字字符

def clean_text(text):
    return pattern.sub('', text)  # 删除非字母数字字符

# 使用示例
print('==', clean_text("@#").lower())  # 输出: Hello123

