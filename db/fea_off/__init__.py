#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/6/26 11:08  
"""



def main():
    # 连接到数据库
    conn = connect_to_database()
    if conn is None:
        return
    try:
        fea = {}
        # 创建游标对象
        cursor = conn.cursor()

        # 演示fetchone()
        result = fetch_all(cursor)
        for key in ['failed_liveness_cnt_all', 'failed_liveness_cnt', 'failed_face_cnt',
                    'the_last_liveness_result_all', 'the_last_liveness_result', 'the_last_face_result']:
            # print result
            val = result.get(key, None)
            if val is not None:
                fea[key] = val
        print 'fea=', fea

        # 演示fetchall()
        # fetchall_example(cursor)
    finally:
        # 关闭游标和连接
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print "数据库连接已关闭"  # Python 2.7 的 print 语句