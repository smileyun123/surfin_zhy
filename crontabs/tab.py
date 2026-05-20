# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# @Author: zhanghaiyun
# @Time: 2025/12/12 11:45
# """
# # 墨西哥特征计算每日例行
# 0 0 * * * cd /data1/work/puhui_data/Global && git pull origin mx_master
# 10 0 * * * cd /data1/work/puhui_data/Global && sh bin/run_offline_job.sh > logs/log.run_offline_job 2>&1
# 00 01 * * * cd /data1/work/puhui_data/Global && sh bin/run_offline_cmodel.sh > logs/log.run_offline_cmodel 2>&1
# #1 */2 * * * cd /data1/work/puhui_data/Global && sh bin/run_2hour_job.sh > logs/log.run_2hour_job 2>&1
#
# 15 * * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/scripts/data_lack_monitor.py > logs/out.data_lack_monitor 2>&1
#
# #10 8 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/model_auc_monitor.py >> logs/log.model_auc_monitor 2>&1
#
# #10 10 * * * cd /data1/work/puhui_data/Global && sh bin/check_offline_data.sh >> logs/log.check_offine_data 2>&1
# #00 10-21/2 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/off_features_missing_check.py
#
# #0 2 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/biz_black_list_comm.py
#
# # 日志删除
# 1 2 * * *  find /data1/work/puhui_data/Global/logs   -type f -ctime +2 -exec rm -f {} \;
#
# # 清理个人目录日志
# #30 10 * * * cd /data1/work/dry/Global && find logs -type f -mtime +15 -exec rm {} \;
#
# # 服务器监控
# #*/1 * * * *  cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/scripts/server_monitor.py >>logs/log.server_monitor 2>&1
#
#
# # 每日生成特征监控指标
# 10 1 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_ml_features_monitor.py 1
# 20 1 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_ml_features_monitor.py 7
# 30 1 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_ml_features_monitor.py 30
# 40 1 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_ml_features_monitor.py 90
# # 45 1 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_ml_score_avg.py
#
# 40 15 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_ml_features_monitor_v2.py  > logs/log.feature_ml_features_monitor_v2 2>&1
#
# # 肯尼亚短信数据源监控报警
# 0 0 * * 6 cd /data1/work/puhui_data/Global && ~/anaconda2/bin/python bin/msg_features/message_monitor.py >> logs/out.message_monitor 2>&1
#
# # [数仓报表组][2021-12-10]解密打款流水表disburse_record 到 数仓feature.etl_disburse_record
# #50 0 * * * cd /data1/work/etl && /home/work/anaconda2/bin/python run_mysql2pg.py > logs/out.run_mysql2pg.log 2>&1
#
# # 决策流规则监控
# #01 18 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/scripts/rule_xml_to_csv2.py >> logs/out.rule_xml_to_csv2
#
# # 墨西哥流量特征psi监控
# #58 23 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/mx_customer_flow_fea_psi_monitor.py
# # # 线上线下特征不一致监控
# #00 05 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/fea_compare_monitor.py > logs/out.fea_compare_monitor 2>&1
#
#
# # 获取市场数据
# #3 */1 * * *  cd /home/work/get_adjust_info && /home/work/tool/jdk1.8.0_191/bin/java -jar get_adjust_info_mx_cashcash.jar 1>/dev/null 2>/dev/null &
#
# # surfin-lab黑名单
# 30 00 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/surfin_lab_blacklist_v1.py v2 5
# 00 01 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/surfin_lab_blacklist_v1.py v3 5
#
# # 定时静默Prometheus告警
# 30 0 * * * sh /data1/work/monitor/alertmanager_silences.sh
#
#
#
# # 实时数据处理脚本监控 实时报表用
# #*/3 * * * * cd /data1/work/puhui_data/data_decrypt && /home/work/anaconda2/bin/python data_process.py >> logs/data_decrypt.log 2>&1 &
#
# # 数据上报监控
# 1 0 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/scripts/data_upload_monitor_v1.py
# # 墨西哥短信未知mobile处理
# 0 2 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/scripts/handle_kaby_mobile_label.py  >> logs/handle_kaby_mobile_label.log 2>&1 &
# # 墨西哥线下每日定时任务
# 0 2 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/scripts/offline_daily_scheduled_tasks.py  >> logs/offline_daily_scheduled_tasks.log 2>&1 &
#
# # 0 * * * * rm /data1/work/wyx/Global/logs/log.starmap_v*
#
# 10 0 * * * cd /data1/work/puhui_data/Global && /home/work/anaconda2/bin/python bin/feature_basics/feature_data_source_monitor_dingding.py