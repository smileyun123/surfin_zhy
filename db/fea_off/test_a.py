#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/16 19:07  
"""
# import json
# def read_json():
#     print 1
#     with open("files/device_attribute.json", "r") as f:
#         return json.load(f)
#
#
# class Sub(object):
#     datas = read_json()
#
#     def run(self):
#         print "子类方法"
#         # print self.datas
#
# if __name__ == '__main__':
#     for i in range(10):
#         Sub().run()



import datetime
import math

def _calculate_interval(release_date_str):
    """
    计算时间差（支持 "2016-12-31" 和 "2016-12" 格式）
    """
    interval = 0
    if release_date_str:
        try:
            # 尝试解析完整日期 "%Y-%m-%d"
            release_date = datetime.datetime.strptime(release_date_str, '%Y-%m-%d')
        except ValueError:
            try:
                # 尝试解析不完整日期 "%Y-%m"
                year_month = release_date_str.split('-')
                if len(year_month) == 2:
                    year = int(year_month[0])
                    month = int(year_month[1])
                    # 获取该月最后一天
                    if month == 12:
                        next_month = 1
                        next_year = year + 1
                    else:
                        next_month = month + 1
                        next_year = year
                    last_day = datetime.datetime(next_year, next_month, 1) - datetime.timedelta(days=1)
                    release_date = datetime.datetime(year, month, last_day.day)
                else:
                    # 如果格式完全不符合，返回默认值 0
                    return interval
            except (ValueError, IndexError):
                # 如果仍然解析失败，返回默认值 0
                return interval

        now_time = datetime.datetime.now()
        delta = now_time - release_date
        interval = math.ceil(delta.total_seconds() / (60 * 60 * 24))
    return interval


print _calculate_interval("2024-12-31")
print _calculate_interval("2024-12")