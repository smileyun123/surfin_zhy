#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/30 15:54  
"""


scores = {"code":"SUCCESS","message":"OK","data":{"score":0.8197985887527466,"features":{"GD_ZRB_20":7508.446,"GD_ZRB_515":3.0,"GD_ZRB_52":-1.0,"GD_ZRB_9999":12.5,"GD_ZRB_77":-1.0,"GD_ZRB_514":-1.0,"GD_ZRB_21":3875.014,"GD_ZRB_59":1.0,"GD_ZRB_1209":-0.055,"GD_ZRB_1214":0.044,"GD_ZRB_1201":0.007,"GD_ZRB_1178":0.003,"GD_ZRB_555":58.0,"GD_ZRB_1198":-0.011,"GD_ZRB_1164":-0.058,"GD_ZRB_553":12.0,"GD_ZRB_641":7056.481,"GD_ZRB_1162":-0.072,"GD_ZRB_551":3.0,"GD_ZRB_1170":-0.681}},"extra":None,"transactionId":"bd5fdadf4bd31929","pricingStrategy":"PAY"}

features = scores['data']['features'].keys()
print(features)
features_lows = [f.lower() for f in features]
print(len(features_lows))
