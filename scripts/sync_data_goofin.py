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

    # 'advance_score_v6_fea',
    # 'icekcredit_multiplat_fea',
    # 'mx_app_tgi_v6_fea',
    # 'mx_message_info_competing_agency_v1_1_keyword_filter2_fea',

    # "india_app_tgi_v3_fea",
    # "applist_update_attention_score_fea",
    # 'rc_data_nubarium_history_fea',
    # "message_nlp_fea",
    # "mx_message_all_record_v3_fea",
    # "mx_message_all_record_v2_fea",
    # "mx_message_all_record_v1_1_fea",
    #2
    # 'app_category_fea',
    # 'app_nlp_v2_fea',
    # 'message_nlp_keyword_filter2_fea',
    # 'mx_app_tgi_v5_fea',
    # 'mx_app_tgi_v6_fea',
    # 'mx_app_tgi_v8_fea',
    # 'mx_message_all_record_v1_1_keyword_filter2_fea',
    # 'mx_message_all_record_v2_keyword_filter2_fea',
    # 'mx_message_all_record_v3_keyword_filter2_fea',
    # 'mx_message_bank_agency_v1_1_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v1_1_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v1_2_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v2_1_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v2_2_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v2_3_keyword_filter2_fea',
    # 'mx_message_mobile_type_keyword_filter2_fea',
    # "origin_repayment_flow_v1_2_fea",
    # 'tongdun_reloan_v2_1_fea',
    # 'tongdun_reloan_v2_2_fea',
    # 'tongdun_reloan_v2_3_fea',
    # 'rule_full_installment_repay_fea',
    # 'mx_app_tgi_v7_fea',
    # "origin_repayment_flow_v1_1_fea",
    # 'rule_installment_repay_fea',
    # 'cep_record_v1_fea',
    # 'apply_behavior_fea',
    # "rule_policy_v2_fea",

    # "icekcredit_multiplat_fea",
    #
    # 'mx_message_info_competing_agency_v1_1_fea',
    # 'mx_message_info_competing_agency_v1_2_fea',
    # 'mx_message_info_competing_agency_v2_1_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v2_3_keyword_filter2_fea',
    # 'mx_message_info_competing_agency_v2_2_keyword_filter2_fea',

    # 'app_install_v1_fea',

    # 3
    # "rule_credit_fea",
    # "person_info_credit",
    # "phone_contact_fea_credit",
    # "phone_location_fea_credit",
    # "phone_basic_loan_fea_credit",
    # "env_info_record_credit",
    # "wifi_info_record_fea_credit",
    # "wifi_all_record_v1_fea_credit",
    # "location_info_record_v1_fea_credit",
    # "location_info_record_v2_fea_credit",
    # "contact_info_record_fea_v2_credit",
    # "contact_info_record_fea_credit",
    # "app_list_fea_credit",
    # "rule_history_loan_performance_credit",
    # "rule_history_loan_performance_v2_fea_credit",
    # "rule_history_loan_performance_v3_fea_credit",
    # "rule_login_operate_fea_credit",
    # "tsfresh_fea_credit",


    #
    # "credit_rule_fea",  # 规则决策特征, done 2
    # "loan_info_fea",  # 规则决策特征, done
    # "rule_loding_info_fea",  # done
    # "phone_basic_data",  # 手机基本信息, done
    # "work_info",  # 工作信息 done
    # "phone_location_fea",  # 位置信息 done
    # "phone_basic_loan_fea",  # 手机基本信息提单 done todo
    # "manual_result_fea",  # 人工审核结果 done
    # "pdl_loan_fea",  # 提单 done
    # "person_info",  # 个人信息, done
    # "phone_contact_fea",  # 通讯录 done
    # "rule_apply_loan_fea",  # 申请 done
    # "rule_login_operate_fea",  # 操作类特征 done
    # "rule_repayment_fea",  # 还款特征 done
    # "rule_history_loan_performance",  # done
    # "rule_loan_basic_fea",  # done
    # "rule_fea_guess",  # 猜想特征, done
    # "anti_fraud_fea",  # 通讯录相关特征, done
    # "contact_like_fea",  # 通讯录相似 done
    # "question_record_fea",
    # "report_credit_fea2",
    # "rule_model_after_fea",
    # "contact_info_record_fea",
    # "contact_info_record_fea_v2",
    # "wifi_info_record_fea",
    # "env_info_record",
    # "manual_audit_result_fea",
    # "fraud_analyse_fea",
    # "wifi_all_record_v1_fea",
    # "location_info_record_v1_fea",
    # "location_info_record_v2_fea",
    # "rule_policy_fea",
    # "rule_cutoff_fea",
    # "neo4j_relation_fea",
    # "neo4j_relation_fea_ext",
    # "face_new_fea",
    # "app_list_fea",
    # "whatsup_third_fea",
    # "app_overdue_v2_fea",
    # "rule_history_loan_performance_v2_fea",
    # "rule_history_loan_performance_v3_fea",
    # "credit_info_change_fea",
    # "login_fea",
    # "neo4j_relation_fea_alpha",
    # 'app_list_fea_v3',
    # 'audit_cheat_fea',
    # 'chinese_item_fea',
    # 'mx_contact_list_fea',
    # 'bank_verify_v1_fea',
    # 'india_app_tgi_v4_fea',
    # 'india_app_bayes_fea',
    # 'rule_overdue_loan_fea',
    # 'rule_history_loan_performance_v4_fea',
    # 'salary_flow_v1_fea',
    # 'phone_num_verify_v1_fea',
    # 'neo4j_relation_fea_device',
    # 'fraud_analyse_split_fea',
    # 'graph_bak_fea',
    # 'recall_user_fea',
    # 'app_nlp_fea',
    # "message_nlp_v2_fea",
    # "repayment_performance_fea",
    # 'mx_app_tgi_v3_fea',
    # 'mx_app_tgi_v4_fea',
    # 'reloan_index_repaid_behaviour_v1_fea',
    # 'idcard_reproduce_fea',
    #
    # 'recycle_loan_info_fea',
    #
    # "rule_face_compare_fea",
    # "advance_black_list_fea",
    # 'rule_ocr_id_card_information_fea',
    # 'izi_ocr_id_card_information_fea',
    # 'machine_first_result_fea',
    # 'advance_score_v1_fea',
    # 'rc_data_nubarium_similarly_fea',
    # 'mexico_credit_report_fea',
    # # 'compare_face_fea_policy',
    # 'credit_report_cluster_fea',
    # 'advance_score_v2_fea',
    # 'real_photo_recognition_fea',
    #
    # 'mx_advance_multi_platform_fea_third',
    # "mx_credit_query_fea",
    # "mx_credit_history_fea_v1_0",
    # "mx_credit_history_fea_v1_1",
    # "mx_credit_history_fea_v1_2",
    # "mx_credit_history_fea_v1_3",
    # "mx_credit_history_fea_v1_4",
    # 'report_first_credit_v3_fea',
    # 'advance_score_v5_fea',
    # 'ocr_v1_fea',
    # "circulo_information_match_v1_fea",
    # "advance_score_v6_fea",
    #


    # "advance_id_forgery_detection_v1_fea",
    # 'face_new_fea_policy',
    # 'engine_result_fea_policy',
    # 'recycle_loan_info_fea_policy',
    # 'customer_service_v1_fea',
    # 'compare_face_fea_policy',
    # 'mx_message_bert_keyword_filter2_fea',
    # 'kaby_app_score_fea',
    # 'mx_message_bank_agency_v1_3_keyword_filter2_fea',
    # 'app_top_fit_fea',
    # 'device_attribute_fea',
    # 'phone_mem_fea',
    # 'mx_message_bank_agency_v1_2_keyword_filter2_fea'
    # 'idcard_classify_fea_policy',
    # 'ocr_back_diff_v1_fea',
    # 'id_apply_behavior_fea',
    # 'id_repayment_behavior_fea',
    # 'phone_apply_behavior_fea',
    # 'phone_repayment_behavior_fea',
    # 'user_apply_loan_fea'
    # 'mx_credit_query_fea',
    # 'mx_credit_history_fea_v1_0',
    # 'mx_credit_history_fea_v1_1',
    # 'mx_credit_history_fea_v1_2',
    # 'mx_credit_history_fea_v1_3',
    # 'mx_credit_history_fea_v1_4',
    # 'report_credit_first_v4_1_fea',
    # 'report_credit_first_v4_2_fea',
    # 'report_credit_first_v4_3_fea',
    # 'report_credit_first_v4_4_fea',
    # 'report_credit_first_v4_5_fea',
    # 'report_credit_first_v4_6_fea'
    # 'rule_installment_repay_fea',
    # 'surfin_info_v1_fea',
    # 'origin_repayment_flow_v1_1_fea',
    # 'login_fea',
    # 'origin_repayment_flow_v1_2_fea',
    # 'rule_full_installment_repay_fea',
    # 'repayment_performance_fea',
    'model_result',
    # 'rc_data_unico_id_verify_fea',
    # 'mx_competitor_app_v1_fea',
    # 'icekredit_mex_postloan_behavior_fea',
    # 'mx_competitor_app_behavior_v1_fea'
    # 'rule_history_loan_performance_v10_fea',
    # 'credit_v3_fea'
]



"""
"task_id": "176949853400035489784697"}
{"task_id": "176949853400097472186538"}
{"task_id": "176949853400089325766926"}

我： 15049246515
沈威宇： 15026941139
高佩雯 18382327260
王大伟 18613710632
王尚程 wangshangcheng
郑琴 19232167728
谭瑞：13611923194 

"""

def request_api(feature):
    for ct in ['goofin']:
        data_dict = {
            'ct': ct,
            'fea_table': 'mx_feature.{}'.format(feature),
            'intersection_col': '',
            'url': 'https://oapi.dingtalk.com/robot/send?access_token=288f03a8229a24b1f6a8dd8c6b250d82671f865fbd37fcbb178cc5a294397bbc',
            'sec': 'SEC168515483ed15c1b498ddfa8a3048dd789619f6e5a965e4ffd557e1055e2fb50',
            'at_user': '18382327260',
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