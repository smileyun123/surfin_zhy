#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/21 10:38  
"""
import logging
import re
import time
import requests
import json
import math
import traceback
import time
from tqdm import tqdm
def mobile_label_by_qwen25(all_mobiles):
    label_dic = {}
    try:
        t1 = time.time()
        # logging.info('mobile_label_by_qwen25 start' % all_mobiles)
        for i in tqdm(range(1, int(len(all_mobiles) / 20) + 2)):
            strr = ','.join(all_mobiles[(i - 1) * 20:i * 20])
            prompt = """
                       问题是根据在墨西哥的主要业务给出机构%s类别、可信度、备注。
                       要求:
                       候选类别有:电信运营商、新闻、银行、金融信贷、电子支付、电商购物、博彩、社交、政府机构、生活出行、生活娱乐、其他:
                       可信度在0-1之间；
                       输出json格式，例如:
                       "unotvcom": {
                            "label":"新闻”
                            "prob": 0.9,
                            "description":"Unotv.com 是一个提供新闻报道的网站。"
                       };
                       只输出json结果。
                   """ % strr
            content = json.dumps({"model": "qwen2.5:32b", "prompt": prompt, "stream": False})
            print'prompt', prompt
            headers = {"Content-Type": "application/json"}
            res = requests.post(url="http://117.50.218.96:11434/api/generate", data=content, headers=headers)
            label_dic.update(json.loads(json.loads(res.text).get('response')))
            print time.time() - t1
    except Exception as e:
        # logging.error("mobile_label_by_qwen25 error: %s\n%s", e, traceback.format_exc())
        pass
    return label_dic

print mobile_label_by_qwen25(["moneyman.es", "Moneyman.es"])