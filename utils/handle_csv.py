#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/6/26 15:18  
"""

import csv
import json
from turtle import mainloop


def readcsv(file_path):
    # 打开CSV文件
    mobiles = set()
    with open(file_path, mode='r') as file:
        # 创建CSV读取器
        csv_reader = csv.reader(file)

        # 逐行读取数据
        for row in csv_reader:
            # print(row)  # 每行是一个列表，如 ['13800138000']
            mobiles.add(row[0])
    print json.dumps(list(mobiles), encoding='utf-8', ensure_ascii=False)
if __name__ == '__main__':
    readcsv('/Users/admin/Downloads/todo_mobiles.csv')