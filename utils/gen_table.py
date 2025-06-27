#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/6/19 19:27  
"""

def make_sql(table_name, features, feature_type_map=None, comment_map=None):
    if not feature_type_map:
        feature_type_map = {}
    if not comment_map:
        comment_map = {}
    out = """create table `%s` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户ID',
  `serial_id` int(11) NOT NULL DEFAULT '0' COMMENT '订单号',\n""" % table_name
    lines = []
    for f in features:
        if f in ['id', 'serial_id', 'user_id']:
            continue
        t = feature_type_map.get(f, 'int(11)')
        # 暂不实现类型逻辑
        lines.append("`%s` %s NOT NULL DEFAULT '-9999999' COMMENT '%s',\n" % (f, t, comment_map.get(f, '')))
    lines = sorted(lines)
    for l in lines:
        out += l
    out += """`feature_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_idx_serial_id` (`serial_id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='';"""
    print out