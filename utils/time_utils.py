#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/1 15:44  
"""
from __future__ import division

from datetime import datetime
import re



"""
                        20250719--31032024 --475
                        20250719--31012025 --169
                        20250719--31082024 --
                        20250719--30092024 --
                        20250719--30042025 --

    """

# 起始日期和结束日期
# start_date = datetime(2020, 05, 21)
# start_date = datetime(2022, 03, 04)
end_date = datetime(2026, 05, 8)
start_date = datetime(2023, 03, 15)

# 计算天数差
days_diff = (end_date - start_date).days

print "从 %s 到 %s 一共是 %s 天" % (start_date, end_date, days_diff)

import datetime

import datetime

import datetime

def split_date_range_to_date(start_date, end_date):
    """
    将日期范围按天分割，返回 date 对象

    Args:
        start_date: 开始日期 (字符串格式: 'YYYY-MM-DD' 或 date/datetime对象)
        end_date: 结束日期 (字符串格式: 'YYYY-MM-DD' 或 date/datetime对象)

    Returns:
        list: 日期区间列表，每个元素为 [date对象, date对象]
    """
    # 转换输入为 date 对象
    start_dt = convert_to_date(start_date)
    end_dt = convert_to_date(end_date)

    # 确保结束日期大于等于开始日期
    if end_dt < start_dt:
        raise ValueError("结束日期必须大于等于开始日期")

    date_ranges = []
    current_end = end_dt

    # 按天递减直到开始日期
    while current_end > start_dt:  # 修改为严格大于，避免处理 start_dt 自身
        next_start = current_end - datetime.timedelta(days=1)

        # 如果下一天小于开始日期，则用 start_dt 作为终点
        if next_start < start_dt:
            date_ranges.append([current_end, start_dt])
            break
        else:
            date_ranges.append([current_end, next_start])
        current_end = next_start

    return date_ranges


def convert_to_date(date_input):
    """统一转换为 date 对象"""
    if isinstance(date_input, datetime.date):
        return date_input
    elif isinstance(date_input, datetime.datetime):
        return date_input.date()
    elif isinstance(date_input, str):
        return datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
    else:
        raise TypeError("不支持的日期类型，请使用字符串、date或datetime对象")

def get_date_ranges_as_strings(start_date, end_date):
    """
    直接获取字符串格式的日期区间（基于 date 对象）
    """
    date_ranges = split_date_range_to_date(start_date, end_date)
    # return [[d1.strftime('%Y-%m-%d'), d2.strftime('%Y-%m-%d')] for d1, d2 in date_ranges]
    return [[d1, d2] for d1, d2 in date_ranges]

# 使用示例
result = get_date_ranges_as_strings("2026-02-01", "2026-02-03")
print 'result=', result


print type(datetime.datetime.now().date()),datetime.datetime.now().date()
#
# num = 120
# days = 0
# for i in range(87, num):
#     days += 1
# print 'days', days