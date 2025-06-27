#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/6/26 11:07  
"""
import time
import logging
import json
import requests
import traceback
from tqdm import tqdm
from db.fea_off.mx_message_mobile_label import MxMessageMobileLableModel


def _get_mobile_label_json(self, messages):
    """
    :return: mobile机构类别
    """
    mobile_label_json = {}
    try:
        rows = MxMessageMobileLableModel.get_mobile_label()
        todo_handle_mobile = set()
        for row in rows:
            if row['status'] == 1:
                mobile_label_json[row['mobile']] = row['label']
            else:
                todo_handle_mobile.add(row['mobile'].lower())
        mobile_need_label = set()
        for message in messages:
            sms_mobile = message['mobile']
            if not sms_mobile:
                continue
            message['mobile'] = sms_mobile.encode('utf-8') if isinstance(sms_mobile, unicode) else sms_mobile
            mobile_label = self._process_mobile(message['mobile'])
            if mobile_label and not mobile_label.isdigit():
                if mobile_label not in mobile_label_json and mobile_label not in todo_handle_mobile:
                    # json获取不到，则记录未获取的mobile列表，每日定时调用llm获取，更新mx_message_mobile_label
                    mobile_need_label.add(message['mobile'])
        # logging.info(
        #     "mobile_label_json , count: %s, mobile_need_label:%s" % (len(mobile_need_label), mobile_need_label))
        if mobile_need_label:
            columns = ['mobile', 'status']
            values = [(mobile, 0) for mobile in mobile_need_label]
            result = MxMessageMobileLableModel.batch_insert_data({'columns': columns, 'values': values})
            # logging.info("mobile_label_json insert result:%s" % result)
    except Exception as e:
        # logging.error("get mobile_label_json error:%s" % e)
        print "error"
    return mobile_label_json



def mobile_label_by_qwen25(all_mobiles):
    label_dic = {}
    max_retries = 3
    retry_delay = 180  # 秒
    try:
        logging.info('mobile_label_by_qwen25 start with %d mobiles' % len(all_mobiles))
        if not all_mobiles:
            logging.info("not all_mobiles")
            return label_dic
        for i in tqdm(range(1, int(len(all_mobiles) / 20) + 2)):
            strr = ','.join(all_mobiles[(i - 1) * 20:i * 20])
            prompt = """
                问题是根据在墨西哥的主要业务给出机构%s类别、可信度、备注。
                要求:
                候选类别有:电信运营商、新闻、银行、金融信贷、电子支付、电商购物、博彩、社交、政府机构、生活出行、生活娱乐、其他:
                可信度在0-1之间；
                输出json格式，例如:
                "unotvcom": {
                     "label":"新闻",
                     "prob": 0.9,
                     "description":"Unotv.com 是一个提供新闻报道的网站。"
                };
                只输出json结果。
            """ % strr
            content = json.dumps({"model": "gwen2.5:32b", "prompt": prompt, "stream": False})
            headers = {"Content-Type": "application/json"}
            for attempt in range(max_retries):
                try:
                    logging.debug('Attempt %d for batch %d' % (attempt + 1, i))
                    res = requests.post(
                        url="http://117.50.218.96:11434/api/generate",
                        data=content,
                        headers=headers,
                        timeout=120
                    )
                    res.raise_for_status()  # 检查HTTP状态码
                    response_data = res.json()
                    if 'response' not in response_data:
                        logging.error("response_data does not contain 'response' key")
                        continue
                    # 解析返回的JSON字符串
                    json_str = response_data['response']
                    parsed_labels = json.loads(json_str)
                    # 更新标签字典
                    label_dic.update(parsed_labels)
                    break  # 成功则跳出重试循环
                except Exception as e:
                    logging.error(
                        'attempt %d failed for batch %d, retrying in %d seconds...' % (attempt + 1, i, retry_delay))
                    time.sleep(retry_delay)
    except Exception as e:
        logging.error('mobile_label_by_qwen25 error: %s\n%s', e, traceback.format_exc())
    return label_dic