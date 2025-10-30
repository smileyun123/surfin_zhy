#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/8/14 10:25  
"""

import pymysql
import time


 # ===========================
db_host = 'localhost'  # 例如：'127.0.0.1' 或 RDS 地址
db_user = 'root'  # 例如：'root'
db_password = '12345678'  # 例如：'123456'
db_name = 'fea_on'  # 数据库名
db_port = 3306  # MySQL 默认端口

def update_feature_compute_stat():
    # 数据库连接配置
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        charset='utf8mb4'
    )

    try:
        with connection.cursor() as cursor:
            # 第一步：执行查询 SQL
            t1 = time.time()
            select_sql = """
                         SELECT id
                         FROM feature_compute_stat
                         WHERE serial_id = 3630116
                           AND task_id = 203969850
                           AND tab_name = 'apply_behavior_fea'
                           AND stage = 'model'; \
                         """

            cursor.execute(select_sql)
            result = cursor.fetchone()
            t2 = time.time()
            if not result:
                print("未找到符合条件的记录")
                return
            print "查询ID: ", t2 - t1
            # 获取查询到的 record_id（假设只有一条记录）
            record_id = result[0]

            # 第二步：根据查询结果执行更新
            update_sql = """
                         UPDATE feature_compute_stat
                         SET status      = 1, \
                             update_time = unix_timestamp(now())
                         WHERE id = %s
                         """

            cursor.execute(update_sql, (record_id,))
            connection.commit()
            t3 = time.time()
            print "更新: ", t3 - t2
            print "查+更: ", t3 - t1
            # print("成功更新 id 为 %s 的记录" % record_id)

            tt =time.time()
            up_sql = """UPDATE feature_compute_stat
                    SET status = 1, update_time = unix_timestamp(now())
                    WHERE serial_id = 3630116.  and task_id=203969850  and  tab_name = "apply_behavior_fea"   and stage = "model ";

                """
            up_sql= """
UPDATE fea_on.feature_compute_stat
SET status = 1, update_time = unix_timestamp(now())
WHERE serial_id = 3101000   and task_id=500606  and  tab_name = "transaction_history_features"   and stage = "feature_selection_4";
"""
            cursor.execute(up_sql)
            connection.commit()
            print "直接更新: ", time.time() - tt
    except Exception as e:
        connection.rollback()
        print("发生错误: ", e)
    finally:
        connection.close()

if __name__ == '__main__':
    update_feature_compute_stat()