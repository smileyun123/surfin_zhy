# -*- coding: utf-8 -*-
import requests
import json

# ------------------ 业务线缩写 ------------------
# 越南: vdong oivay yoloan
# 墨西哥: cc kaby
# 印度: payrupik payrupik_new
# 肯尼亚: kashbean zashloan metaloan
# 尼日利亚: ng ncash easymoni cashnet
# 印尼: pjy

# ------------------ json: type参数 ------------------
# 固定为"feature"
# ------------------ json: data参数 ------------------
# 必须参数
#   ct: [必须] 业务线缩写
#   fea_table: [必须] 需要同步的特征表，格式为"库名.特征表名"
# 可选参数
#   pg_table: 字符串类型, 默认为"feature.特征表"
#   intersection_col: 字符串类型, 根据此字段增量同步, 空或无此key时为全量同步（增量同步时只insert，全量同步时会先truncate）
#   grant_select: 字符串类型, 赋select权限,逗号分隔,如: {... 'grant_select': 'etl_user, read_user'}
#   url: 字符串类型, 钉钉机器人url，用来通知开始和完成的消息
#   sec: 字符串类型, 钉钉机器人加签，用来通知开始和完成的消息
#   index_field: 数组类型, 默认值为['id','serial_id','user_id']; 在新建表的时候, 创建索引, 如: {... 'index_field': ['id', 'user_id']}
#   full_fire: 字符类型，1的时候火力全开，慎用！
#   at_user: 艾特的人,拼音, 英文逗号间隔; at_mobiles有值时，此参数无效
#   at_mobiles: 艾特人的手机号, 英文逗号间隔


# 全量回溯使用，加字段
# data_dict = {'ct': 'vdong', 'fea_table': 'vdong_feature.burying_point_fea', 'intersection_col': ''
#     , 'grant_select': 'vnm_risk_group'}

# 注意注意注意：操作步骤：上面的python脚本，同步和异步的，都指定固定表。要同步的表。提到越南etl机器中。在etl里，注掉原同步箭头，创建新的python脚本用的文件，指定对应的python脚本路径，即可。
# face_new_fea_policy
# engine_result_fea_policy


feature_list = [
    # 'report_credit_first_v4_1_fea',
    # 'report_credit_first_v4_2_fea',
    # 'report_credit_first_v4_3_fea',
    # 'report_credit_first_v4_4_fea',
    # 'report_credit_first_v4_5_fea',
    # 'report_credit_first_v4_6_fea',
    # 'bill_v1_fea_te',
    # 'bill_v2_fea_te',

    # 'mx_credit_buro_query_fea',
    # 'mx_credit_buro_history_fea_v1_0',
    # 'mx_credit_buro_history_fea_v1_1',
    # 'mx_credit_buro_history_fea_v1_2',
    # 'mx_credit_buro_history_fea_v1_3',
    # 'mx_credit_buro_history_fea_v1_4',
    # 'mx_credit_buro_summary_fea',

    # 'rc_data_nubarium_similarly_fea',
    # 'device_attribute_fea_te'
    # 'bill_v3_fea_te',
    # 'cheat_app_fea',

    # 'app_category_fea',
    # 'app_top_fit_fea',
    # 'device_attribute_fea',
    # 'kaby_app_score_fea',
    # 'mx_app_tgi_v7_fea',
    # 'mx_app_tgi_v8_fea',
    # 'mx_message_bank_agency_v1_1_fea',
    # 'mx_message_bank_agency_v1_2_fea',
    # 'mx_message_bank_agency_v1_3_fea',
    # 'mx_message_info_competing_agency_v2_1_fea',
    # 'mx_message_info_competing_agency_v2_2_fea',
    # 'mx_message_info_competing_agency_v2_3_fea',
    # 'mx_message_mobile_type_fea',
    # 'phone_mem_fea',
    # 'cheat_app_fea',
    # 'id_apply_behavior_fea',
    # 'id_repayment_behavior_fea',
    # 'phone_apply_behavior_fea',
    # 'phone_repayment_behavior_fea',
    'model_result',
    # 'app_category_fea',
    # 'device_attribute_fea',
    # 'kaby_app_score_fea',
    # 'mx_app_tgi_v7_fea',
    # 'id_apply_behavior_fea',
    # 'mx_app_tgi_v8_fea',
    # 'app_top_fit_fea',
    # 'phone_apply_behavior_fea',
    # 'phone_mem_fea'
    # 'qa_info_fea',
    # 'transaction_monitor_fea',
    # 'authority_blacklist_fea',
    # 'app_google_play_info',
    # 'bill_v1_fea_te',
    # 'bill_v2_fea_te',
    # 'bill_v3_fea_te',
    # 'loan_movement_fea_v2_te',
    # 'loan_movement_fea_v1_te',

]

"""
朱江敏 15215179188
"""
def request_api(feature):
    data_dict = {
        'ct': 'sufinc',
        'fea_table': 'mx_feature.{}'.format(feature),
        'intersection_col': '',
        'url': 'https://oapi.dingtalk.com/robot/send?access_token=288f03a8229a24b1f6a8dd8c6b250d82671f865fbd37fcbb178cc5a294397bbc',
        'sec': 'SEC168515483ed15c1b498ddfa8a3048dd789619f6e5a965e4ffd557e1055e2fb50',
        'at_user': '15215179188',
        'full_fire': 0,
        'is_full_msg': 0,
        'level': 2,
        # 'pg_table': '',
    }

    # 增量回溯使用，比如按照serial_id增量。
    # data_dict = {'ct': 'vdong', 'fea_table': 'vdong_feature.juicy_score_fea', 'intersection_col': 'serial_id'}

    data_json = json.dumps({"type": "feature", "data": data_dict})
    rep = requests.post("http://101.200.146.156:5010/fea_extract", data=data_json, headers={"Content-Type": "application/json;charset=utf-8"})
    print(rep.text)  # 成功后返回任务id


def main():
    for f in feature_list:
        request_api(f)


if __name__ == '__main__':
    main()
