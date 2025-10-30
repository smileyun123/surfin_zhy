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
start_date = datetime(2025, 10,29)
end_date = datetime(2025, 8, 19)

# 计算天数差
days_diff = (end_date - start_date).days

print "从 %s 到 %s 一共是 %s 天" % (start_date, end_date, days_diff)
