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
    # 'live_detection_fea_policy',
    # 'self_ocr_id_card_information_fea_policy'
    # 'kaby_data_walla_high_risk_fea_third',
    # 'kaby_data_walla_mbrank_fea_third',
    # 'mx_message_mobile_type_keyword_filter2_fea',
    # 'kaby_message_read_keyword_filter2_fea',
    # 'device_price_fea',
    'device_attribute_fea',
    # 'advance_score_v6_fea',
    # 'icekcredit_multiplat_fea',
    # 'apply_behavior_fea',
    # 'model_result'
]


def request_api(feature):
    data_dict = {
        'ct': 'kaby',
        'fea_table': 'mx_feature.{}'.format(feature),
        'intersection_col': '',
        'url': 'https://oapi.dingtalk.com/robot/send?access_token=288f03a8229a24b1f6a8dd8c6b250d82671f865fbd37fcbb178cc5a294397bbc',
        'sec': 'SEC168515483ed15c1b498ddfa8a3048dd789619f6e5a965e4ffd557e1055e2fb50',
        'at_user': 'zhanghaiyun',
        'full_fire': 0,
        'is_full_msg': 0,
        'level': 2,
        # 'pg_table': '',
    }

    # 增量回溯使用，比如按照serial_id增量。
    # data_dict = {'ct': 'vdong', 'fea_table': 'vdong_feature.juicy_score_fea', 'intersection_col': 'id'}

    data_json = json.dumps({"type": "feature", "data": data_dict})
    rep = requests.post("http://101.200.146.156:5010/fea_extract", data=data_json, headers={"Content-Type": "application/json;charset=utf-8"})
    print(rep.text)  # 成功后返回任务id


def main():
    for f in feature_list:
        request_api(f)


if __name__ == '__main__':
    main()
