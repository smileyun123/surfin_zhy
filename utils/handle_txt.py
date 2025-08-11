#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/17 14:14  
"""



def read_txt_by_line(file_path):
    """
    读取本地 txt 文件，并以换行符分割每一行内容。

    :param file_path: str, 文件路径
    :return: list, 每个元素为文件中的一行内容
    """
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines


lines = read_txt_by_line('../db/fea_off/files/all_odi_output.txt')
print(lines)

