# -*- coding: utf-8 -*-
import pymysql

import json


_rank_dict = {
        'A1': [1, 11],
        'A2': [1, 12],
        'A3': [1, 13],
        'A4': [1, 14],
        'A5': [1, 15],
        'B1': [2, 21],
        'B2': [2, 22],
        'B3': [2, 23],
        'B4': [2, 24],
        'B5': [2, 25],
        'C1': [3, 31],
        'C2': [3, 32],
        'C3': [3, 33],
        'C4': [3, 34],
        'C5': [3, 35]
    }

def connect_to_database():
    """
    连接到MySQL数据库
    返回: 数据库连接对象
    """
    try:
        # 替换以下参数为你的数据库连接信息
        conn = pymysql.connect(
            host='localhost',  # 数据库服务器地址
            user='root',  # 数据库用户名
            password='12345678',  # 数据库密码
            db='mx_loan',  # 数据库名
            charset='utf8mb4',  # 推荐使用utf8mb4支持更多字符
            cursorclass=pymysql.cursors.DictCursor  # 可选：返回字典格式的结果
        )
        print "成功连接到数据库"  # Python 2.7 的 print 语句
        return conn
    except pymysql.Error as e:
        print "连接数据库失败: {}".format(e)  # format() 在 Python 2.7 和 3 都可用
        return None


def fetchone_example(cursor):
    """
    使用fetchone()函数查询数据
    参数: cursor - 数据库游标对象
    """
    try:
        a_sql ="""
SELECT 
    CASE 
        WHEN COUNT(CASE WHEN type = 1 AND status = 0 THEN 1 END) = 0 THEN NULL
        ELSE SUM(CASE WHEN type = 1 AND status = 0 THEN 1 ELSE 0 END)
    END AS failed_liveness_cnt,
    
    CASE 
        WHEN COUNT(CASE WHEN type = 2 AND status = 0 THEN 1 END) = 0 THEN NULL
        ELSE SUM(CASE WHEN type = 2 AND status = 0 THEN 1 ELSE 0 END)
    END AS failed_face_cnt,
    
    CASE 
        WHEN COUNT(CASE WHEN status = 0 THEN 1 END) = 0 THEN NULL
        ELSE SUM(CASE WHEN status = 0 THEN 1 ELSE 0 END)
    END AS failed_liveness_cnt_all,
    
    (SELECT status 
     FROM alive_photo_record 
     WHERE serial_id = 3032864 AND type = 1 
     ORDER BY create_time DESC LIMIT 1) AS the_last_liveness_result,
    
    (SELECT status 
     FROM alive_photo_record 
     WHERE serial_id = 3032864 AND type = 2 
     ORDER BY create_time DESC LIMIT 1) AS the_last_face_result,
    
    (SELECT status 
     FROM alive_photo_record 
     WHERE serial_id = 3032864
     ORDER BY create_time DESC LIMIT 1) AS the_last_liveness_result_all
FROM 
    alive_photo_record
WHERE 
    serial_id = 3032864;"""
        b_sql = """
                    
SELECT 
    -- 获取code值
    (SELECT result FROM rc3.rc_data_walla_high_risk WHERE user_id = 6541000 AND create_time >= 1749554964 ORDER BY id DESC LIMIT 1) AS kaby_mw_highrisk_status,
    -- 获取hit值，仅当status=6且code=0时
    
    (SELECT result FROM rc3.rc_data_walla_high_risk 
                WHERE user_id = 6541000 
                AND create_time >= 1749554964 
                AND status = 6 
                AND result IS not NULL and  JSON_VALID(result) =1 and JSON_UNQUOTE(JSON_EXTRACT(result, '$.code')) = '0' ORDER BY id DESC LIMIT 1)
    AS kaby_mw_highrisk_flag;

            """

        serial_id = 3071463
        c_sql = """   
        SELECT 
    (SELECT result FROM rc3.rc_data_walla_mbrank WHERE serial_id = 2988463 ORDER BY id DESC LIMIT 1) AS status_result,
    (SELECT result FROM rc3.rc_data_walla_mbrank 
     WHERE 
         serial_id = 2988463 
         AND status=6 
         AND result IS NOT NULL 
         AND JSON_VALID(result)=1 
         AND JSON_UNQUOTE(JSON_EXTRACT(result, '$.code')) = '0'
     ORDER BY id DESC LIMIT 1) AS rank_result,
    EXISTS(SELECT 1 FROM rc3.rc_data_walla_mbrank WHERE serial_id = 2988463) AS has_record;

                """
        c2_sql ="""SELECT 
                    -- 获取code值
                    (SELECT result FROM rc3.rc_data_walla_mbrank WHERE user_id = 6205109 AND create_time <= 1748193775 ORDER BY id DESC LIMIT 1) AS status_result,
                    -- 仅当status=6且code=0时
                    (SELECT result FROM rc3.rc_data_walla_mbrank 
                                WHERE user_id = 6205109 
                                AND create_time <= 1748193775
                                AND status = 6 
                                AND result IS not NULL 
                                AND  JSON_VALID(result) =1 
                                AND JSON_UNQUOTE(JSON_EXTRACT(result, '$.code')) = '0' 
                            ORDER BY id DESC LIMIT 1) AS rank_result;"""
        c_sql ="""              
                    
 SELECT                    
(SELECT result FROM rc3.rc_data_walla_mbrank WHERE serial_id = 2426716  ORDER BY id DESC LIMIT 1) AS status_result,
                -- 仅当status=6且code=0时
                (SELECT result FROM rc3.rc_data_walla_mbrank 
                            WHERE 
                                serial_id = 2426716 
                                AND status=6 
                                AND result IS not NULL 
                                AND  JSON_VALID(result) =1 
                                AND JSON_UNQUOTE(JSON_EXTRACT(result, '$.code')) = '0'
                            ORDER BY id DESC LIMIT 1) AS rank_result, 
                            EXISTS(SELECT 1 FROM rc3.rc_data_walla_mbrank WHERE serial_id = 2426716) AS has_record;
"""
        # 执行SQL查询
        # cursor.execute(a_sql)  # 替换为你的表名
        # cursor.execute(b_sql)  # 替换为你的表名
        cursor.execute(c_sql)  # 替换为你的表名


        # 获取一条记录
        row = cursor.fetchone()
        print 'row ---------------', row

        if row:
            if not row['has_record']:
            # if row.get('status_result', None) is  None and row.get('rank_result', None) is None:
                cursor.execute(c2_sql)  # 替换为你的表名
                row = cursor.fetchone()
                print ";c2========"
            print "fetchone()结果:"  # Python 2.7 的 print 语句
            print "查询到一条记录:", row
            return row
        else:
            print "没有查询到记录"
    except pymysql.Error as e:
        print "查询失败: {}".format(e)
    return None


def fetchall_example(cursor):
    """
    使用fetchall()函数查询数据
    参数: cursor - 数据库游标对象
    """
    try:
        # 执行SQL查询
        cursor.execute("SELECT * FROM your_table LIMIT 5")  # 替换为你的表名，限制查询5条记录

        # 获取所有记录
        rows = cursor.fetchall()

        if rows:
            print "fetchall()结果:"  # Python 2.7 的 print 语句
            print "查询到 {} 条记录:".format(len(rows))
            for i, row in enumerate(rows, 1):
                print "记录 {}: {}".format(i, row)
        else:
            print "没有查询到记录"
    except pymysql.Error as e:
        print "查询失败: {}".format(e)


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
        result = fetchone_example(cursor)
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


def rc_data_walla_high_risk():
    # 连接到数据库
    conn = connect_to_database()
    if conn is None:
        return

    try:
        fea = {}
        # 创建游标对象
        cursor = conn.cursor()

        # 演示fetchone()
        row = fetchone_example(cursor)
        if  row is None:
            print 'rc_data_walla_high_risk serial_id is None'
            return
        # for key in ['kaby_mw_highrisk_status', 'kaby_mw_highrisk_flag']:
        #     # print result
        #     val = result.get(key, None)
        #     if val is not None:
        #         fea[key] = val
        # print 'fea=', fea
        if row:
            status_result = row.get('status_result', None)
            print 'status_result=',status_result
            if status_result:
                try:
                    status_result = json.loads(status_result)
                    print 'status_result',status_result
                    if 'code' in status_result:
                        print 'code'
                        fea['kaby_mw_mobile_rank_status'] = status_result.get('code')
                except:
                    print 'error1'
            rank_result = row.get('rank_result', None)
            if rank_result:
                try:
                    rank_result = json.loads(rank_result)
                    if 'data' in rank_result and 'rank' in rank_result.get('data', {}):
                        rank = rank_result['data']['rank']
                        if rank is None:
                            fea['kaby_mw_mobile_rank_rough'] = 0
                            fea['kaby_mw_mobile_rank_detail'] = 0
                        else:
                            rank_value = _rank_dict.get(rank, [])
                            if rank_value:
                                fea['kaby_mw_mobile_rank_rough'] = rank_value[0]
                                fea['kaby_mw_mobile_rank_detail'] = rank_value[1]
                except:
                    print 'error'
        print 'fea', fea
        # 演示fetchall()
        # fetchall_example(cursor)
    finally:
        # 关闭游标和连接
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print "数据库连接已关闭"  # Python 2.7 的 print 语句
if __name__ == "__main__":
    # main()
    import time

    t1 = time.time()
    rc_data_walla_high_risk()
    print 'spend_time:', time.time() - t1


    print 1747934575 + 3 *86400

