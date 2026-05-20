#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/12/16 13:36  
"""

import pymysql
import random
import time
import csv

# 1. 数据库连接配置
# ===========================
db_host = 'localhost'  # 例如：'127.0.0.1' 或 RDS 地址
db_user = 'root'  # 例如：'root'
db_password = '12345678'  # 例如：'123456'
db_name = 'fea_on'  # 数据库名
db_port = 3306  # MySQL 默认端口


def conn_db():
    # ===========================
    # 3. 连接数据库
    # ===========================
    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name,
        port=db_port,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # 可选，返回字典格式结果，调试用
    )

    cursor = conn.cursor()
    return conn, cursor


def write_to_csv(records, filename, ignore_fields=None):
    """
    将记录写入CSV文件
    :param records: 记录列表
    :param filename: 输出文件名
    :param ignore_fields: 要忽略的字段列表
    """
    if not records:
        return

    if ignore_fields is None:
        ignore_fields = []

    # 获取所有字段名并排除忽略字段
    fieldnames = set()
    for record in records:
        fieldnames.update(record.keys())

    # 移除忽略字段
    fieldnames = [field for field in fieldnames if field not in ignore_fields]
    fieldnames = sorted(fieldnames)

    # 创建新记录列表，移除忽略字段
    filtered_records = []
    for record in records:
        filtered_record = {k: records[0][k] for k in fieldnames}
        filtered_records.extend([filtered_record])

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_records)

    print('ok')


def compare_tables(cursor, ignore_fields=None):
    """
    对比两个表中的数据
    :param cursor: 数据库游标对象
    :param ignore_fields: 要忽略对比的字段列表
    """
    if ignore_fields is None:
        ignore_fields = []

    matched_records = []  # 存储匹配记录
    mismatched_records = []  # 存储不匹配记录

    try:
        # 获取表1最新50条数据 (数据集1)
        cursor.execute("SELECT * FROM id_apply_behavior_fea_kaby ORDER BY id DESC LIMIT 50")
        dataset1 = cursor.fetchall()

        if not dataset1:
            print("数据集1为空")
            return

        # 提取 serial_id 列表
        serial_ids = [row['serial_id'] for row in dataset1]
        serial_ids_str = ','.join(["'{}'".format(sid) for sid in serial_ids])

        # 查询表2中对应的记录 (数据集2)
        query2 = "SELECT * FROM id_apply_behavior_fea_kaby WHERE serial_id IN ({})".format(serial_ids_str)
        cursor.execute(query2)
        dataset2 = cursor.fetchall()

        if not dataset2:
            print("数据集2为空")
            return

        # 构建以 serial_id 为键的字典方便查找
        dict1 = {row['serial_id']: row for row in dataset1}
        dict2 = {row['serial_id']: row for row in dataset2}

        # 对比数据
        print("开始对比数据...")
        for serial_id in serial_ids:
            row1 = dict1.get(serial_id)
            row2 = dict2.get(serial_id)

            if not row1 or not row2:
                continue

            # 忽略指定字段后比较其余字段
            mismatched_fields = []
            for key in row1.keys():
                if key in ignore_fields or key not in row2:
                    continue
                if row1[key] != row2[key]:
                    mismatched_fields.append(key)

            # 添加来源标识
            row1_with_source = dict(row1)
            row1_with_source['_source'] = 'id_apply_behavior_fea'
            row1_with_source['_status'] = 'mismatch' if mismatched_fields else 'match'

            row2_with_source = dict(row2)
            row2_with_source['_source'] = 'id_apply_behavior_fea_kaby'
            row2_with_source['_status'] = 'mismatch' if mismatched_fields else 'match'

            if mismatched_fields:
                print("不匹配 serial_id={}: 字段 {}".format(serial_id, ', '.join(mismatched_fields)))
                mismatched_records.extend([row1_with_source, row2_with_source])
            else:
                print("匹配 serial_id={}".format(serial_id))
                matched_records.extend([row1_with_source, row2_with_source])
        # 写入CSV文件
        write_to_csv(matched_records, 'matched_records.csv', ignore_fields)
        write_to_csv(mismatched_records, 'mismatched_records.csv', ignore_fields)

    except Exception as e:
        print("对比过程中发生错误: {}".format(e))

if __name__ == '__main__':
    # conn, cursor = conn_db()
    # # 示例：忽略字段 ['create_time', 'update_time']
    # compare_tables(cursor, ignore_fields=['id','feature_time'])
    #
    # cursor.close()
    # conn.close()

    # a = [2]
    # b=[0]
    # if all([a,b]):
    #     print('ok')
    # else:
    #     print('no')
    content = None
    contents = []
    if content and content not in contents:
        contents.append(content)
    else:
        print(time.time())

