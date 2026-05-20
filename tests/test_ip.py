#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import logging
import random
import requests


def get_random_ip():
    '''Randomly select an IP from the IP proxy pool and return'''
    ip_list = ["114.230.104.175:8089",
               "117.70.49.102:8089",
               "125.87.86.183:8089",
               "114.103.88.117:8089",
               "117.57.93.213:8089",
               "182.34.103.130:9999",
               "117.57.92.198:8089",
               "117.69.237.247:8089",
               "113.124.87.105:9999",
               "117.71.149.89:8089",
               "36.6.145.152:8089",
               "125.87.94.104:8089",
               "125.87.80.110:8089",
               "117.71.155.199:8089",
               "183.164.242.161:8089",
               "114.230.104.175:8089",
               "117.70.49.102:8089",
               "125.87.86.183:8089",
               "114.103.88.117:8089",
               "117.57.93.213:8089",
               "182.34.103.130:9999",
               "117.57.92.198:8089",
               "117.69.237.247:8089",
               "113.124.87.105:9999",
               "117.71.149.89:8089",
               "36.6.145.152:8089",
               "125.87.94.104:8089",
               "125.87.80.110:8089",
               "117.71.155.199:8089",
               "183.164.242.161:8089",
               "114.230.104.175:8089",
               "117.70.49.102:8089",
               "125.87.86.183:8089",
               "114.103.88.117:8089",
               "117.57.93.213:8089",
               "182.34.103.130:9999",
               "117.57.92.198:8089",
               "117.69.237.247:8089",
               "113.124.87.105:9999",
               "117.71.149.89:8089",
               "36.6.145.152:8089",
               "125.87.94.104:8089",
               "125.87.80.110:8089",
               "117.71.155.199:8089",
               "183.164.242.161:8089",
               "114.230.104.175:8089",
               "117.70.49.102:8089",
               "125.87.86.183:8089",
               "114.103.88.117:8089",
               "117.57.93.213:8089",
               "182.34.103.130:9999",
               "117.57.92.198:8089",
               "117.69.237.247:8089",
               "113.124.87.105:9999",
               "117.71.149.89:8089",
               "36.6.145.152:8089",
               "125.87.94.104:8089",
               "125.87.80.110:8089",
               "117.71.155.199:8089",
               "183.164.242.161:8089", ]
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def test_proxy_validity():
    """测试代理IP是否有效"""
    proxy = get_random_ip()
    test_url = "http://httpbin.org/ip"
    print 'proxy', proxy
    try:
        response = requests.get(test_url, proxies=proxy, timeout=5)
        if response.status_code == 200:
            logging.info("proxy :%s is working" % proxy)
            return True
    except Exception as e:
        print e
    return  False



def check_google_service_status():
    """检查Google Play商店服务状态"""
    test_url = "https://play.google.com"
    try:
        response = requests.get(test_url, timeout=5)
        if response.status_code == 200:
            logging.info("Google Play service is accessible")
            return True
        else:
            logging.warning("Google Play service returned status: %s" % response.status_code)
            return False
    except Exception as e:
        logging.error("Cannot access Google Play: %s" % str(e))
        return False

if __name__ == '__main__':
    # kaby_serial_to_total_term, goofin_serial_to_total_term = {}, {}
    # win_records = [{'serial_id': 'sid1', 'repayment_behavior_fea_data_source': 'kaby', 'total_term': 4}, {'serial_id': 'sid1', 'repayment_behavior_fea_data_source': 'kaby', 'total_term': 4},
    #                {'serial_id': 'sid1', 'repayment_behavior_fea_data_source': 'goofin', 'total_term': 4}, {'serial_id': 'sid1', 'repayment_behavior_fea_data_source': 'goofin', 'total_term': 4},
    #                {'serial_id': 'sid2', 'repayment_behavior_fea_data_source': 'goofin', 'total_term': 4}]
    # for record in win_records:
    #     sid = record['serial_id']
    #     source = record['repayment_behavior_fea_data_source']
    #
    #     target_dict = kaby_serial_to_total_term if source == 'kaby' else goofin_serial_to_total_term
    #     if sid not in target_dict:
    #         target_dict[sid] = {'total_term': record['total_term'], 'paid_count': 0}
    #     target_dict[sid]['paid_count'] += 1
    #
    # all_order_freq = []
    # for term_dict in [kaby_serial_to_total_term, goofin_serial_to_total_term]:
    #     for data in term_dict.values():
    #         if data['total_term'] > 0:
    #             all_order_freq.append(data['paid_count'] / data['total_term'])
    # print 'all_order_freq', all_order_freq
    # print round(sum(all_order_freq) / len(all_order_freq),2) if all_order_freq else 0


    # def merge_datas(datas1, source1, datas2, source2):
    #     all_datas = []
    #     for d1 in datas1:
    #         d1['apply_behavior_fea_data_source'] = source1
    #         all_datas.append(d1)
    #     for d2 in datas2:
    #         d2['apply_behavior_fea_data_source'] = source2
    #         all_datas.append(d2)
    #     return all_datas
    #
    # def merge_datas1(datas1, source1, datas2, source2):
    #     """使用列表推导式，一次构造完整列表"""
    #     return [
    #         dict(d, apply_behavior_fea_data_source=source1) for d in datas1
    #     ] + [
    #         dict(d, apply_behavior_fea_data_source=source2) for d in datas2
    #     ]
    # import  time
    # t1 =time.time()
    # aa = merge_datas1([{'a': 1}, {'a': 2}], 'kaby', [{'a': 3}, {'a': 4}], 'goofin')
    # print 'aa_st', time.time() - t1, '----',aa
    # t2=time.time()
    # bb = merge_datas([], 'kaby', [], 'goofin')
    # print 'bb_st', time.time() - t2, '----',bb

    def safe_percentile(data, p):
        """Python 2.7 兼容的百分位数计算"""
        if not data:
            return 0.0

        try:
            # 优先使用numpy
            import numpy as np
            return float(np.percentile(data, p))
        except ImportError:
            # numpy不可用时的回退方案
            sorted_data = sorted(data)
            n = len(sorted_data)

            if n == 1:
                return float(sorted_data[0])

            # 使用线性插值方法
            k = (n - 1) * (float(p) / 100.0)
            floor_idx = int(k)
            ceil_idx = min(floor_idx + 1, n - 1)
            frac = k - floor_idx

            if floor_idx == ceil_idx:
                return float(sorted_data[floor_idx])
            else:
                return float(sorted_data[floor_idx]) + frac * float(sorted_data[ceil_idx] - sorted_data[floor_idx])


    hist_exp_vals = [99,100,0,0,0,0]
    print safe_percentile(hist_exp_vals, 95)

    print 2/100
