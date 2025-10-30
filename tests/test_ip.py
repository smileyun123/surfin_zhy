#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    print(test_proxy_validity())