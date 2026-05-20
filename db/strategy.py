#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/8/13 13:58
"""
import pymysql

# ===========================
# 1. 数据库连接配置
# ===========================
db_host = 'localhost'  # 例如：'127.0.0.1' 或 RDS 地址
db_user = 'root'  # 例如：'root'
db_password = '12345678'  # 例如：'123456'
db_name = 'strategy'  # 数据库名
db_port = 3306  # MySQL 默认端口

# mysql -u root -p 目标数据库名 < /你的文件路径/script.sql
# # mysql -u root -p minghui < /Users/admin/Downloads/minghui/original_collection_data.sql
# ===========================
# 2. 插入参数配置
# ===========================
base_apply_no = 12  # apply_no 起始值
num_records = 6000000  # 插入条数，比如插入10条，apply_no 为 3583862 ~ 3583871
user_id = 6129377
analysis_id = 'RAID_20250807224821_1000023271'
process_no = 'surfin/credit_inner_audit/credit_inner_audit_second_inner'

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

# ===========================
# 4. 批量插入数据
# ===========================
try:
    # 使用批量插入优化性能
    insert_sql = """
                 INSERT INTO strategy.risk_analysis
                 (create_time, update_time, apply_no, risk_user_id, risk_analysis_id, risk_process_no,
                  risk_process_sub_no, risk_credit_item, risk_credit_item_ante, risk_credit_ante,
                  risk_credit_subtract, risk_credit_add, risk_credit_post, risk_credit_display,
                  risk_result_label, risk_result_reject, risk_result_reject_null, risk_result_pass,
                  risk_result_pass_null, risk_result_decision, risk_result_fee, risk_state,
                  manual_question_set, product_id)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
                 """

    # 分批处理，避免占用过多内存，每批插入10000条记录
    batch_size = 10000
    total_batches = (num_records + batch_size - 1) // batch_size

    print("开始批量插入 %d 条记录，共 %d 批次，每批 %d 条记录" % (num_records, total_batches, batch_size))

    for batch in range(total_batches):
        start_index = batch * batch_size
        end_index = min((batch + 1) * batch_size, num_records)
        batch_count = end_index - start_index

        # 构造当前批次的数据
        data_batch = []
        for i in range(start_index, end_index):
            apply_no = base_apply_no + i
            data_batch.append((
                1754624901,  # create_time
                1754624901,  # update_time
                apply_no,  # apply_no
                user_id,  # risk_user_id
                analysis_id,  # risk_analysis_id
                process_no,  # risk_process_no
                None,  # risk_process_sub_no
                None,  # risk_credit_item
                None,  # risk_credit_item_ante
                None,  # risk_credit_ante
                None,  # risk_credit_subtract
                None,  # risk_credit_add
                '0',  # risk_credit_post
                None,  # risk_credit_display
                None,  # risk_result_label
                'null,MXR_ct2_msgapp_042,MXR_ct2_msgapp_043',  # risk_result_reject
                'null,MXR_AFMACB001,MXR_AFL0ANB001,MXR_cyc13_msgapp,MXR_cyc4p_msgapp,MXR_cyc1_msgapp,MXR_ct1_msgapp_03,MXR_cyc2_4_msgapp,MXR_ct2_msgapp_041,MXR_ct36_msgapp_041,MXR_ct36_msgapp_042,MXR_ct711_msgapp_02,MXR_ct7p_msgapp_02,MXR_ct11p_msgapp,MXR_FROZEN001,MXR_cyc24_a1,MXR_cyc4p_a1,MXR_SUCC1_2_a1,MXR_SUCC1_2_a2,MXR_SUCC3_6_a1,MXR_SUCC3_6_a2,MXR_SUCC7p_a1',
                # risk_result_reject_null
                'null,reloan_test',  # risk_result_pass
                None,  # risk_result_pass_null
                '0',  # risk_result_decision
                None,  # risk_result_fee
                '0',  # risk_state
                '{}',  # manual_question_set
                0  # product_id
            ))

        # 执行批量插入
        cursor.executemany(insert_sql, data_batch)
        conn.commit()
        print("✅ 批次 %d/%d 完成，插入 %d 条记录" % (batch + 1, total_batches, batch_count))

except Exception as e:
    print("❌ 批量插入过程中发生错误: %s" % e)
    conn.rollback()
    raise

# ===========================
# 5. 提交事务并关闭连接
# ===========================
cursor.close()
conn.close()

print("🎉 批量插入完成，共插入 %d 条数据。" % num_records)