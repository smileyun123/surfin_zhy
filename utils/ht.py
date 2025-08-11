#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/18 10:54  
"""



# 测试数据
date_strings = [
    # "2019-xx-xx", "2018年", "2016-10-XX", "2019-2020", "2022-09-",
    # "2018-08-00", "2015-02-XX", "2023-08-00",
    "20xx", "20xx","20xx-05-01","20xx-xx-xx",

    # "2017-11-XX", "2014-10-", "2018年", "2012-xx-xx",
    # "2017-04-00", "2019-10-XX", "2023-04-00", "2016年", "2016-xx-xx",
    # "2019-xx-xx", "2014-06-00", "2015-12-XX", "2018-07-00", "2019-07-00",
    # "2022-03-00", "2018-02-00",  "2022-10-XX",
    # "2016-02-00", "2016-06-00", "2023-06-XX", "2024-05-XX", "2014-06-00",
    # "2016-xx-xx", "2021-10-XX", "2016-02-00", "2014年10月", "2013-04-00",
    # "2024-08-XX",
    "2024年第四季度", "2019-05-00", "2018-06-XX",
    "2024-05-xx", "2017-02-XX", "2018-12-xx", "2016-06-00",
    "2016-06-00", "2015-02-XX", "2016-xx-xx", "2017-04-xx", "2017-03-XX",
    "2019-10-XX", "2016-04-00", "2017-03-xx", "2018-06-00", "2016-11-00",
     "2017-07-00", "2018-00-00", "2015-10-xx", "2015-10-xx",
    "2013-02-00", "2017-xx-xx", "2014-xx-xx", "2022-02-xx", "2018-07-XX",
     "2015-07-00", "2015-11-00", "2018-04-00",
    "2016-11-00", "2016-11-00", "2016-xx-xx", "2016-xx-xx", "2023年第四季度",
    "2017-04-00", "2022-03-XX", "2014-07-xx", "2015-04-00",
    "2016-08-xx", "2014-04-XX", "2014-04-XX", "2013-04-00", "2017-04-00",
    "2019-09-00", "2022-02-XX", "2015-02-XX",  "2013-04-XX", "2013-04-00", "2016-08-xx",  "2022-2024", "2016年",
    "2016-xx-xx", "2019-10-XX", "2018-11-xx", "2017-xx-xx", "2017-07-00",
    "2017-10-xx",  "2022-04-xx", "2019-xx-xx",
    "2022-xx-xx", "2019-10-XX", "2019-11-00",
    "2018年", "2024-05-xx", "2016-04-00", "2019-06-XX",
    "推测为2010年前后", "2020-11-00", "2019-10-XX", "2021-xx-xx",
     "2016年", "2016年", "2017-07-00",
    "2022-03-xx"
]


import datetime
import math
import re

def _calculate_interval(release_date_str):
    """
    计算当前时间与给定日期之间的天数差。
    支持格式：
    - 完整日期（"2022-09-16"）
    - 年月（"2022-09"）
    - 模糊日期（"xx" 或 "X"）
    - 年份范围（"2019-2020"）
    - 季度表述（"2024年第四季度"）
    - 推测表述（"推测为2010年前后"）

    返回：相差天数（向上取整），无法解析返回 0
    """
    interval = 0
    if not release_date_str:
        return interval

    # 统一转为字符串处理
    release_date_str = str(release_date_str).strip()

    if '20xx' in release_date_str:
        release_date_str = release_date_str.replace('20xx', '2000')
    # 处理“推测为2010年前后”
    if "推测为2010年前后" in release_date_str:
        release_date = datetime.datetime(2010, 1, 1)
        print release_date_str, '----', release_date.strftime('%Y-%m-%d')
    # 处理年份范围
    elif re.match(r'^\d{4}-\d{4}$', release_date_str):
        year = int(release_date_str.split('-')[0])
        release_date = datetime.datetime(year, 1, 1)
        print release_date_str, '--111111--', release_date.strftime('%Y-%m-%d')
    # 处理季度表述
    elif re.search(r'(\d{4})年(第一|第二|第三|第四)季度', release_date_str):
        match = re.search(r'(\d{4})年(第一|第二|第三|第四)季度', release_date_str)
        year = int(match.group(1))
        quarter = match.group(2)
        quarter_start_month = {'第一': 1, '第二': 4, '第三': 7, '第四': 10}[quarter]
        release_date = datetime.datetime(year, quarter_start_month, 1)
        print release_date_str, '----', release_date.strftime('%Y-%m-%d')
    else:
        # 处理“xx”或“X”表示缺失部分
        parts = release_date_str.replace("年", "-").replace("月", "-").replace("日", "").split("-")
        parts = [p for p in parts if p]

        # 补全为年月日
        year = int(parts[0]) if parts[0] not in ("xx", "X", "") else 1
        month = int(parts[1]) if len(parts) > 1 and parts[1] not in ("xx", "X", "", 'XX') else 1
        day = int(parts[2]) if len(parts) > 2 and parts[2] not in ("xx", "X", "", "XX") else 1

        # 修正年份为合理范围
        if year < 1900:
            year = 1900
        if month < 1 or month > 12:
            month = 1
        if day < 1 or day > 31:
            day = 1

        try:
            release_date = datetime.datetime(year, month, day)
        except ValueError:
            # 处理非法日期（如2月30日）
            release_date = datetime.datetime(year, month, 1)
        print release_date_str, '----', release_date.strftime('%Y-%m-%d')

    # now_time = datetime.datetime.now()
    # delta = now_time - release_date
    # interval = math.ceil(delta.total_seconds() / (60 * 60 * 24))

    # return interval

for i in date_strings:
    _calculate_interval(i)

