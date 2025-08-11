#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/17 14:17
"""
import logging
import json
import datetime
import math
import traceback
import re
import io

def read_txt_by_line(file_path):
    """
    读取本地 txt 文件，并以换行符分割每一行内容。

    :param file_path: str, 文件路径
    :return: list, 每个元素为文件中的一行内容
    """
    # with open(file_path, 'r') as file:
    #     lines = file.read().splitlines()
    # return lines
    with io.open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
serial_id = ''
# all_envs = read_txt_by_line('files/all_odi_output.txt')
all_envs = read_txt_by_line('files/device_attribute.json')
# all_envs = read_txt_by_line('files/a.json')
# print(all_envs)

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
        return ''

    # 统一转为字符串处理
    release_date_str = str(release_date_str).strip()

    if '20xx' in release_date_str:
        return release_date_str
    if "至" in release_date_str:
        release_date_str = release_date_str.split('至')[0]
    if " / " in release_date_str:
        release_date_str = release_date_str.split(' / ')[0]
    if ", " in release_date_str:
        release_date_str = release_date_str.split(", " )[0]

    # 处理“推测为2010年前后”
    if "推测为2010年前后" in release_date_str:
        release_date = datetime.datetime(2010, 1, 1)
        return release_date.strftime('%Y-%m-%d')
    # 处理年份范围
    elif re.match(r'^\d{4}-\d{4}$', release_date_str):
        year = int(release_date_str.split('-')[0])
        release_date = datetime.datetime(year, 1, 1)
        return release_date.strftime('%Y-%m-%d')

    # 处理季度表述
    elif re.search(r'(\d{4})年(第一|第二|第三|第四)季度', release_date_str):
        match = re.search(r'(\d{4})年(第一|第二|第三|第四)季度', release_date_str)
        year = int(match.group(1))
        quarter = match.group(2)
        quarter_start_month = {'第一': 1, '第二': 4, '第三': 7, '第四': 10}[quarter]
        release_date = datetime.datetime(year, quarter_start_month, 1)
        # print release_date_str, '----', release_date.strftime('%Y-%m-%d')
        return release_date.strftime('%Y-%m-%d')

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
            # release_date = datetime.datetime(year, month, 1)
            return release_date_str
        # print release_date_str, '----', release_date.strftime('%Y-%m-%d')
        return release_date.strftime('%Y-%m-%d')


    # now_time = datetime.datetime.now()
    # delta = now_time - release_date
    # interval = math.ceil(delta.total_seconds() / (60 * 60 * 24))

# def unicode_to_str(input):
#     if isinstance(input, dict):
#         return {unicode_to_str(key): unicode_to_str(value) for key, value in input.iteritems()}
#     elif isinstance(input, list):
#         return [unicode_to_str(element) for element in input]
#     elif isinstance(input, unicode):
#         return input.encode('utf-8')
#     else:
#         return input

def write_json_file(file_path, data):
    # print data
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
def process_json_data(data):
    print(len(data))
    for key, item in data.items():
        ss = ['release_price', 'release_date', 'storage_size', 'current_price', 'battery_size']
        for s in ss:
            if s not in item:
                print (s, key)
        # create_date = item.get("release_date")
        # try:
        #     new_release_date = _calculate_interval(create_date)
        #     item["release_date"] = new_release_date
        # except Exception as e:
        #     print("Error processing date:", create_date)

    # 预处理数据，确保类型正确和默认值设置
    for model_key, model_attr in data.items():
        # 确保价格是float类型
        try:
            model_attr['release_price'] = float(model_attr.get('release_price', 0))
        except (ValueError, TypeError):
            model_attr['release_price'] = 0.0

        try:
            model_attr['current_price'] = float(model_attr.get('current_price', 0))
        except (ValueError, TypeError):
            model_attr['current_price'] = 0.0

        # 确保存储和电池容量有默认值0
        model_attr.setdefault('storage_size', 0)
        model_attr.setdefault('battery_size', 0)

        # 确保发布日期有默认值空字符串
        model_attr.setdefault('release_date', "")

    print(len(data))
    # print json.dumps(data, ensure_ascii=False)

    write_json_file("files/device_attribute_processed.json",  data)

process_json_data(all_envs)
