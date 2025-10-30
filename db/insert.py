#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/8/13 23:09
"""
import pymysql
import random
import time

# ===========================
# 1. 数据库连接配置
# ===========================
db_host = 'localhost'  # 例如：'127.0.0.1' 或 RDS 地址
db_user = 'root'  # 例如：'root'
db_password = '12345678'  # 例如：'123456'
db_name = 'fea_on'  # 数据库名
db_port = 3306  # MySQL 默认端口

# ===========================
# 2. 插入参数配置
# ===========================
# num_records = 40000000  # 插入条数，10万条
num_records = 40000000  # 插入条数，40000万条
# num_records = 40000000  # 插入条数，10万条
base_serial_id = 1000000  # serial_id 起始值
base_task_id = 500000   # task_id 起始值

# 可能的表名列表
table_names = [
    'user_profile_features', 'transaction_history_features', 'device_info_features',
    'credit_score_features', 'behavioral_analysis_features', 'risk_assessment_features',
    'demographic_data_features', 'financial_stability_features', 'payment_history_features',
    'social_media_features', 'geolocation_features', 'purchase_pattern_features', "apply_behavior_fea"
]

# 可能的阶段列表
# 136个阶段列表
stages = [
    'model',
    'data_extraction_1', 'data_extraction_2', 'data_extraction_3', 'data_extraction_4', 'data_extraction_5',
    'data_cleaning_1', 'data_cleaning_2', 'data_cleaning_3', 'data_cleaning_4', 'data_cleaning_5',
    'data_cleaning_6', 'data_cleaning_7', 'data_cleaning_8', 'data_cleaning_9', 'data_cleaning_10',
    'feature_engineering_1', 'feature_engineering_2', 'feature_engineering_3', 'feature_engineering_4', 'feature_engineering_5',
    'feature_engineering_6', 'feature_engineering_7', 'feature_engineering_8', 'feature_engineering_9', 'feature_engineering_10',
    'feature_engineering_11', 'feature_engineering_12', 'feature_engineering_13', 'feature_engineering_14', 'feature_engineering_15',
    'feature_selection_1', 'feature_selection_2', 'feature_selection_3', 'feature_selection_4', 'feature_selection_5',
    'feature_selection_6', 'feature_selection_7', 'feature_selection_8', 'feature_selection_9', 'feature_selection_10',
    'model_training_1', 'model_training_2', 'model_training_3', 'model_training_4', 'model_training_5',
    'model_training_6', 'model_training_7', 'model_training_8', 'model_training_9', 'model_training_10',
    'model_validation_1', 'model_validation_2', 'model_validation_3', 'model_validation_4', 'model_validation_5',
    'model_validation_6', 'model_validation_7', 'model_validation_8', 'model_validation_9', 'model_validation_10',
    'model_deployment_1', 'model_deployment_2', 'model_deployment_3', 'model_deployment_4', 'model_deployment_5',
    'model_monitoring_1', 'model_monitoring_2', 'model_monitoring_3', 'model_monitoring_4', 'model_monitoring_5',
    'data_analysis_1', 'data_analysis_2', 'data_analysis_3', 'data_analysis_4', 'data_analysis_5',
    'data_analysis_6', 'data_analysis_7', 'data_analysis_8', 'data_analysis_9', 'data_analysis_10',
    'report_generation_1', 'report_generation_2', 'report_generation_3', 'report_generation_4', 'report_generation_5',
    'report_generation_6', 'report_generation_7', 'report_generation_8', 'report_generation_9', 'report_generation_10',
    'quality_control_1', 'quality_control_2', 'quality_control_3', 'quality_control_4', 'quality_control_5',
    'quality_control_6', 'quality_control_7', 'quality_control_8', 'quality_control_9', 'quality_control_10',
    'data_integration_1', 'data_integration_2', 'data_integration_3', 'data_integration_4', 'data_integration_5',
    'data_integration_6', 'data_integration_7', 'data_integration_8', 'data_integration_9', 'data_integration_10',
    'first_stage', 'second_stage', 'third_stage', 'fourth_stage', 'fifth_stage',
    'final_stage', 'preprocessing_stage', 'processing_stage', 'postprocessing_stage', 'evaluation_stage',
    'testing_stage', 'validation_stage', 'production_stage', 'development_stage', 'research_stage'
]

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


def insert_single_record(conn, cursor):
    """
    插入单条记录到feature_compute_stat表

    Args:
        conn: 数据库连接
        cursor: 数据库游标
        serial_id: 序列ID
        tab_name: 表名
        status: 状态
        time_value: 时间戳
        task_id: 任务ID
        update_time: 更新时间
        stage: 阶段
    """
    try:
        # 随机生成参数
        serial_id = base_serial_id + random.randint(0, 1000000)
        tab_name = random.choice(table_names)
        task_id = base_task_id + random.randint(0, 100000)
        status = random.randint(0, 1)
        time_value = int(time.time()) - random.randint(0, 3600 * 24 * 30)  # 过去30天内的随机时间戳
        update_time = int(time.time()) - random.randint(0, 3600 * 24 * 7)  # 过去7天内的随机时间戳
        stage = random.choice(stages)

        insert_sql = """
                     INSERT INTO feature_compute_stat
                         (serial_id, tab_name, status, `time`, task_id, update_time, stage)
                     VALUES (%s, %s, %s, %s, %s, %s, %s) \
                     """

        cursor.execute(insert_sql, (serial_id, tab_name, status, time_value, task_id, update_time, stage))
        conn.commit()
        print("成功插入记录")

    except Exception as e:
        print("插入记录时发生错误: ", e)
        conn.rollback()
        raise


def insert_single_data_example():
    """
    示例函数：插入单条数据的使用示例
    """
    conn, cursor = conn_db()
    try:
        # 插入单条记录示例
        insert_single_record(
            conn,
            cursor,
            serial_id=3630116,
            tab_name="apply_behavior_fea",
            status=0,
            time_value=int(time.time()),
            task_id=203969850,
            update_time=int(time.time()),
            stage="model"
        )
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    conn, cursor = conn_db()
    for i in range(100000):
        time.sleep(0.1)
        insert_single_record(conn, cursor)
    # 示例：插入单条记录
    # insert_single_data_example()
