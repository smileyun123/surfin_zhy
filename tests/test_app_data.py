#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2026/4/27 14:29  
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2026/4/21
竟品APP特征：基于多次上报的app JSON，结合app配置表生成多维度特征。
特征命名：{scene}_{category}_{time_window}_{operator}_{stat}
字段： 760

create table `mx_competitor_app_behavior_v1_fea` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户ID',
  `serial_id` int(11) NOT NULL DEFAULT '0' COMMENT '订单号',
`history_100w_competitor_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all活跃天数max',
`history_100w_competitor_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all活跃天数mean',
`history_100w_competitor_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all活跃天数min',
`history_100w_competitor_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all活跃天数std',
`history_100w_competitor_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all安装次数',
`history_100w_competitor_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all卸载次数',
`history_100w_competitor_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all卸载天数max',
`history_100w_competitor_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all卸载天数mean',
`history_100w_competitor_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all卸载天数min',
`history_100w_competitor_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all卸载天数std',
`history_ala_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allprestamo.dinero.ala活跃天数',
`history_ala_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.alaall安装次数',
`history_ala_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.alaall卸载次数',
`history_ala_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allprestamo.dinero.ala卸载天数',
`history_banco_azteca_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.com.bancoazteca.bazdigitalmovil活跃天数',
`history_banco_azteca_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovilall安装次数',
`history_banco_azteca_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovilall卸载次数',
`history_banco_azteca_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.com.bancoazteca.bazdigitalmovil卸载天数',
`history_bank_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all活跃天数max',
`history_bank_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all活跃天数mean',
`history_bank_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all活跃天数min',
`history_bank_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all活跃天数std',
`history_bank_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类all安装次数',
`history_bank_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类all卸载次数',
`history_bank_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all卸载天数max',
`history_bank_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all卸载天数mean',
`history_bank_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all卸载天数min',
`history_bank_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '银行类all卸载天数std',
`history_baubap_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.baubap活跃天数',
`history_baubap_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubapall安装次数',
`history_baubap_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubapall卸载次数',
`history_baubap_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.baubap卸载天数',
`history_bbva_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.bancomer.mbanking活跃天数',
`history_bbva_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbankingall安装次数',
`history_bbva_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbankingall卸载次数',
`history_bbva_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.bancomer.mbanking卸载天数',
`history_billetera_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.google.android.apps.walletnfcrel活跃天数',
`history_billetera_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrelall安装次数',
`history_billetera_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrelall卸载次数',
`history_billetera_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.google.android.apps.walletnfcrel卸载天数',
`history_bnpl_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all活跃天数max',
`history_bnpl_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all活跃天数mean',
`history_bnpl_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all活跃天数min',
`history_bnpl_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all活跃天数std',
`history_bnpl_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all安装次数',
`history_bnpl_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all卸载次数',
`history_bnpl_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all卸载天数max',
`history_bnpl_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all卸载天数mean',
`history_bnpl_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all卸载天数min',
`history_bnpl_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all卸载天数std',
`history_cfe_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.com.cfe.cfecontigo活跃天数',
`history_cfe_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigoall安装次数',
`history_cfe_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigoall卸载次数',
`history_cfe_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.com.cfe.cfecontigo卸载天数',
`history_claro_pay_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.globalhitss.claro.pay活跃天数',
`history_claro_pay_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.payall安装次数',
`history_claro_pay_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.payall卸载次数',
`history_claro_pay_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.globalhitss.claro.pay卸载天数',
`history_competition_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all活跃天数max',
`history_competition_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all活跃天数mean',
`history_competition_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all活跃天数min',
`history_competition_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all活跃天数std',
`history_competition_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品all安装次数',
`history_competition_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品all卸载次数',
`history_competition_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all卸载天数max',
`history_competition_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all卸载天数mean',
`history_competition_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all卸载天数min',
`history_competition_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品all卸载天数std',
`history_coppel_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.coppel.coppelapp活跃天数',
`history_coppel_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelappall安装次数',
`history_coppel_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelappall卸载次数',
`history_coppel_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.coppel.coppelapp卸载天数',
`history_credmex_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.fintopia.mxcredmex活跃天数',
`history_credmex_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmexall安装次数',
`history_credmex_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmexall卸载次数',
`history_credmex_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.fintopia.mxcredmex卸载天数',
`history_didi_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.didiglobal.cashloan活跃天数',
`history_didi_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloanall安装次数',
`history_didi_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloanall卸载次数',
`history_didi_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.didiglobal.cashloan卸载天数',
`history_finance_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all活跃天数max',
`history_finance_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all活跃天数mean',
`history_finance_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all活跃天数min',
`history_finance_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all活跃天数std',
`history_finance_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类all安装次数',
`history_finance_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类all卸载次数',
`history_finance_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all卸载天数max',
`history_finance_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all卸载天数mean',
`history_finance_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all卸载天数min',
`history_finance_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '金融类all卸载天数std',
`history_fortaprest_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.dinero.fd.mx.loan活跃天数',
`history_fortaprest_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loanall安装次数',
`history_fortaprest_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loanall卸载次数',
`history_fortaprest_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.dinero.fd.mx.loan卸载天数',
`history_good_competitor_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all活跃天数max',
`history_good_competitor_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all活跃天数mean',
`history_good_competitor_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all活跃天数min',
`history_good_competitor_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all活跃天数std',
`history_good_competitor_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all安装次数',
`history_good_competitor_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all卸载次数',
`history_good_competitor_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all卸载天数max',
`history_good_competitor_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all卸载天数mean',
`history_good_competitor_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all卸载天数min',
`history_good_competitor_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all卸载天数std',
`history_klar_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.klar.app活跃天数',
`history_klar_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.appall安装次数',
`history_klar_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.appall卸载次数',
`history_klar_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.klar.app卸载天数',
`history_kueski_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.kueski.os活跃天数',
`history_kueski_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.osall安装次数',
`history_kueski_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.osall卸载次数',
`history_kueski_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.kueski.os卸载天数',
`history_mercado_pago_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.mercadopago.wallet活跃天数',
`history_mercado_pago_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.walletall安装次数',
`history_mercado_pago_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.walletall卸载次数',
`history_mercado_pago_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.mercadopago.wallet卸载天数',
`history_mexdin_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.elaworld.mexloan活跃天数',
`history_mexdin_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloanall安装次数',
`history_mexdin_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloanall卸载次数',
`history_mexdin_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.elaworld.mexloan卸载天数',
`history_mexicash._all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.mexicash.app活跃天数',
`history_mexicash._all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.appall安装次数',
`history_mexicash._all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.appall卸载次数',
`history_mexicash._all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.mexicash.app卸载天数',
`history_new_competitor_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all活跃天数max',
`history_new_competitor_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all活跃天数mean',
`history_new_competitor_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all活跃天数min',
`history_new_competitor_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all活跃天数std',
`history_new_competitor_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all安装次数',
`history_new_competitor_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all卸载次数',
`history_new_competitor_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all卸载天数max',
`history_new_competitor_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all卸载天数mean',
`history_new_competitor_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all卸载天数min',
`history_new_competitor_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all卸载天数std',
`history_nu_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.nu.production活跃天数',
`history_nu_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.productionall安装次数',
`history_nu_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.productionall卸载次数',
`history_nu_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.nu.production卸载天数',
`history_other_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all活跃天数max',
`history_other_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all活跃天数mean',
`history_other_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all活跃天数min',
`history_other_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all活跃天数std',
`history_other_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all安装次数',
`history_other_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all卸载次数',
`history_other_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all卸载天数max',
`history_other_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all卸载天数mean',
`history_other_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all卸载天数min',
`history_other_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all卸载天数std',
`history_oxxo_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.pagopopmobile活跃天数',
`history_oxxo_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobileall安装次数',
`history_oxxo_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobileall卸载次数',
`history_oxxo_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.pagopopmobile卸载天数',
`history_stori_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allai.powerup.stori活跃天数',
`history_stori_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.storiall安装次数',
`history_stori_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.storiall卸载次数',
`history_stori_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allai.powerup.stori卸载天数',
`history_supermovil_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.bancosantander.supermovil活跃天数',
`history_supermovil_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovilall安装次数',
`history_supermovil_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovilall卸载次数',
`history_supermovil_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.bancosantander.supermovil卸载天数',
`history_tala_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.com.tala活跃天数',
`history_tala_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.talaall安装次数',
`history_tala_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.talaall卸载次数',
`history_tala_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allmx.com.tala卸载天数',
`history_tilt_empower_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allfinance.empower.mx活跃天数',
`history_tilt_empower_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mxall安装次数',
`history_tilt_empower_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mxall卸载次数',
`history_tilt_empower_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allfinance.empower.mx卸载天数',
`history_wallet_all_activedays_max` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all活跃天数max',
`history_wallet_all_activedays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all活跃天数mean',
`history_wallet_all_activedays_min` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all活跃天数min',
`history_wallet_all_activedays_std` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all活跃天数std',
`history_wallet_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all安装次数',
`history_wallet_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all卸载次数',
`history_wallet_all_unloaddays_max` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all卸载天数max',
`history_wallet_all_unloaddays_mean` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all卸载天数mean',
`history_wallet_all_unloaddays_min` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all卸载天数min',
`history_wallet_all_unloaddays_std` double NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all卸载天数std',
`history_whatsapp_all_activedays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.whatsapp活跃天数',
`history_whatsapp_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsappall安装次数',
`history_whatsapp_all_unload_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsappall卸载次数',
`history_whatsapp_all_unloaddays_value` double NOT NULL DEFAULT '-9999999' COMMENT 'allcom.whatsapp卸载天数',
`recent_100w_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品180d安装次数',
`recent_100w_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30d安装次数',
`recent_100w_competitor_30d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dcoverage_max',
`recent_100w_competitor_30d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dcoverage_mean',
`recent_100w_competitor_30d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dcoverage_min',
`recent_100w_competitor_30d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dcoverage_std',
`recent_100w_competitor_30d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dltv_max',
`recent_100w_competitor_30d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dltv_mean',
`recent_100w_competitor_30d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dltv_min',
`recent_100w_competitor_30d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dltv_std',
`recent_100w_competitor_30d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dtgi_max',
`recent_100w_competitor_30d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dtgi_mean',
`recent_100w_competitor_30d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dtgi_min',
`recent_100w_competitor_30d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30dtgi_std',
`recent_100w_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品7d安装次数',
`recent_100w_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90d安装次数',
`recent_100w_competitor_90d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dcoverage_max',
`recent_100w_competitor_90d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dcoverage_mean',
`recent_100w_competitor_90d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dcoverage_min',
`recent_100w_competitor_90d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dcoverage_std',
`recent_100w_competitor_90d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dltv_max',
`recent_100w_competitor_90d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dltv_mean',
`recent_100w_competitor_90d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dltv_min',
`recent_100w_competitor_90d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dltv_std',
`recent_100w_competitor_90d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dtgi_max',
`recent_100w_competitor_90d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dtgi_mean',
`recent_100w_competitor_90d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dtgi_min',
`recent_100w_competitor_90d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90dtgi_std',
`recent_100w_competitor_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品all安装次数',
`recent_100w_competitor_all_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allcoverage_max',
`recent_100w_competitor_all_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allcoverage_mean',
`recent_100w_competitor_all_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allcoverage_min',
`recent_100w_competitor_all_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allcoverage_std',
`recent_100w_competitor_all_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allltv_max',
`recent_100w_competitor_all_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allltv_mean',
`recent_100w_competitor_all_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allltv_min',
`recent_100w_competitor_all_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品allltv_std',
`recent_100w_competitor_all_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品alltgi_max',
`recent_100w_competitor_all_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品alltgi_mean',
`recent_100w_competitor_all_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品alltgi_min',
`recent_100w_competitor_all_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品alltgi_std',
`recent_100w_competitor_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30安装次数',
`recent_100w_competitor_d30_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30coverage_max',
`recent_100w_competitor_d30_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30coverage_mean',
`recent_100w_competitor_d30_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30coverage_min',
`recent_100w_competitor_d30_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30coverage_std',
`recent_100w_competitor_d30_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30ltv_max',
`recent_100w_competitor_d30_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30ltv_mean',
`recent_100w_competitor_d30_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30ltv_min',
`recent_100w_competitor_d30_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30ltv_std',
`recent_100w_competitor_d30_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30tgi_max',
`recent_100w_competitor_d30_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30tgi_mean',
`recent_100w_competitor_d30_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30tgi_min',
`recent_100w_competitor_d30_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d30tgi_std',
`recent_100w_competitor_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d60安装次数',
`recent_100w_competitor_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90安装次数',
`recent_100w_competitor_d90_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90coverage_max',
`recent_100w_competitor_d90_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90coverage_mean',
`recent_100w_competitor_d90_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90coverage_min',
`recent_100w_competitor_d90_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90coverage_std',
`recent_100w_competitor_d90_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90ltv_max',
`recent_100w_competitor_d90_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90ltv_mean',
`recent_100w_competitor_d90_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90ltv_min',
`recent_100w_competitor_d90_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90ltv_std',
`recent_100w_competitor_d90_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90tgi_max',
`recent_100w_competitor_d90_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90tgi_mean',
`recent_100w_competitor_d90_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90tgi_min',
`recent_100w_competitor_d90_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品d90tgi_std',
`recent_all_app_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app180d安装次数',
`recent_all_app_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app30d安装次数',
`recent_all_app_30d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dcoverage_max',
`recent_all_app_30d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dcoverage_mean',
`recent_all_app_30d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dcoverage_min',
`recent_all_app_30d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dcoverage_std',
`recent_all_app_30d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dltv_max',
`recent_all_app_30d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dltv_mean',
`recent_all_app_30d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dltv_min',
`recent_all_app_30d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dltv_std',
`recent_all_app_30d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dtgi_max',
`recent_all_app_30d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dtgi_mean',
`recent_all_app_30d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dtgi_min',
`recent_all_app_30d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部app30dtgi_std',
`recent_all_app_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app7d安装次数',
`recent_all_app_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app90d安装次数',
`recent_all_app_90d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dcoverage_max',
`recent_all_app_90d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dcoverage_mean',
`recent_all_app_90d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dcoverage_min',
`recent_all_app_90d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dcoverage_std',
`recent_all_app_90d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dltv_max',
`recent_all_app_90d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dltv_mean',
`recent_all_app_90d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dltv_min',
`recent_all_app_90d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dltv_std',
`recent_all_app_90d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dtgi_max',
`recent_all_app_90d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dtgi_mean',
`recent_all_app_90d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dtgi_min',
`recent_all_app_90d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部app90dtgi_std',
`recent_all_app_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部appall安装次数',
`recent_all_app_all_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallcoverage_max',
`recent_all_app_all_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallcoverage_mean',
`recent_all_app_all_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallcoverage_min',
`recent_all_app_all_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallcoverage_std',
`recent_all_app_all_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallltv_max',
`recent_all_app_all_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallltv_mean',
`recent_all_app_all_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallltv_min',
`recent_all_app_all_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appallltv_std',
`recent_all_app_all_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appalltgi_max',
`recent_all_app_all_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appalltgi_mean',
`recent_all_app_all_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appalltgi_min',
`recent_all_app_all_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appalltgi_std',
`recent_all_app_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部appd30安装次数',
`recent_all_app_d30_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30coverage_max',
`recent_all_app_d30_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30coverage_mean',
`recent_all_app_d30_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30coverage_min',
`recent_all_app_d30_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30coverage_std',
`recent_all_app_d30_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30ltv_max',
`recent_all_app_d30_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30ltv_mean',
`recent_all_app_d30_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30ltv_min',
`recent_all_app_d30_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30ltv_std',
`recent_all_app_d30_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30tgi_max',
`recent_all_app_d30_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30tgi_mean',
`recent_all_app_d30_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30tgi_min',
`recent_all_app_d30_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd30tgi_std',
`recent_all_app_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部appd60安装次数',
`recent_all_app_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部appd90安装次数',
`recent_all_app_d90_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90coverage_max',
`recent_all_app_d90_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90coverage_mean',
`recent_all_app_d90_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90coverage_min',
`recent_all_app_d90_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90coverage_std',
`recent_all_app_d90_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90ltv_max',
`recent_all_app_d90_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90ltv_mean',
`recent_all_app_d90_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90ltv_min',
`recent_all_app_d90_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90ltv_std',
`recent_all_app_d90_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90tgi_max',
`recent_all_app_d90_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90tgi_mean',
`recent_all_app_d90_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90tgi_min',
`recent_all_app_d90_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '全部appd90tgi_std',
`recent_bank_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类180d安装次数',
`recent_bank_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类30d安装次数',
`recent_bank_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类7d安装次数',
`recent_bank_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类90d安装次数',
`recent_bank_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类all安装次数',
`recent_bank_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类d30安装次数',
`recent_bank_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类d60安装次数',
`recent_bank_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类d90安装次数',
`recent_bnpl_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类180d安装次数',
`recent_bnpl_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类30d安装次数',
`recent_bnpl_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类7d安装次数',
`recent_bnpl_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类90d安装次数',
`recent_bnpl_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类all安装次数',
`recent_bnpl_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类d30安装次数',
`recent_bnpl_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类d60安装次数',
`recent_bnpl_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类d90安装次数',
`recent_competition_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品180d安装次数',
`recent_competition_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品30d安装次数',
`recent_competition_30d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dcoverage_max',
`recent_competition_30d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dcoverage_mean',
`recent_competition_30d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dcoverage_min',
`recent_competition_30d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dcoverage_std',
`recent_competition_30d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dltv_max',
`recent_competition_30d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dltv_mean',
`recent_competition_30d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dltv_min',
`recent_competition_30d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dltv_std',
`recent_competition_30d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dtgi_max',
`recent_competition_30d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dtgi_mean',
`recent_competition_30d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dtgi_min',
`recent_competition_30d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品30dtgi_std',
`recent_competition_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品7d安装次数',
`recent_competition_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品90d安装次数',
`recent_competition_90d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dcoverage_max',
`recent_competition_90d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dcoverage_mean',
`recent_competition_90d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dcoverage_min',
`recent_competition_90d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dcoverage_std',
`recent_competition_90d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dltv_max',
`recent_competition_90d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dltv_mean',
`recent_competition_90d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dltv_min',
`recent_competition_90d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dltv_std',
`recent_competition_90d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dtgi_max',
`recent_competition_90d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dtgi_mean',
`recent_competition_90d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dtgi_min',
`recent_competition_90d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品90dtgi_std',
`recent_competition_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品all安装次数',
`recent_competition_all_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allcoverage_max',
`recent_competition_all_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allcoverage_mean',
`recent_competition_all_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allcoverage_min',
`recent_competition_all_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allcoverage_std',
`recent_competition_all_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allltv_max',
`recent_competition_all_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allltv_mean',
`recent_competition_all_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allltv_min',
`recent_competition_all_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品allltv_std',
`recent_competition_all_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品alltgi_max',
`recent_competition_all_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品alltgi_mean',
`recent_competition_all_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品alltgi_min',
`recent_competition_all_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品alltgi_std',
`recent_competition_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品d30安装次数',
`recent_competition_d30_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30coverage_max',
`recent_competition_d30_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30coverage_mean',
`recent_competition_d30_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30coverage_min',
`recent_competition_d30_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30coverage_std',
`recent_competition_d30_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30ltv_max',
`recent_competition_d30_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30ltv_mean',
`recent_competition_d30_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30ltv_min',
`recent_competition_d30_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30ltv_std',
`recent_competition_d30_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30tgi_max',
`recent_competition_d30_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30tgi_mean',
`recent_competition_d30_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30tgi_min',
`recent_competition_d30_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d30tgi_std',
`recent_competition_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品d60安装次数',
`recent_competition_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品d90安装次数',
`recent_competition_d90_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90coverage_max',
`recent_competition_d90_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90coverage_mean',
`recent_competition_d90_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90coverage_min',
`recent_competition_d90_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90coverage_std',
`recent_competition_d90_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90ltv_max',
`recent_competition_d90_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90ltv_mean',
`recent_competition_d90_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90ltv_min',
`recent_competition_d90_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90ltv_std',
`recent_competition_d90_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90tgi_max',
`recent_competition_d90_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90tgi_mean',
`recent_competition_d90_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90tgi_min',
`recent_competition_d90_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '竞品d90tgi_std',
`recent_finance_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类180d安装次数',
`recent_finance_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类30d安装次数',
`recent_finance_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类7d安装次数',
`recent_finance_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类90d安装次数',
`recent_finance_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类all安装次数',
`recent_finance_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类d30安装次数',
`recent_finance_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类d60安装次数',
`recent_finance_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类d90安装次数',
`recent_good_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品180d安装次数',
`recent_good_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30d安装次数',
`recent_good_competitor_30d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dcoverage_max',
`recent_good_competitor_30d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dcoverage_mean',
`recent_good_competitor_30d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dcoverage_min',
`recent_good_competitor_30d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dcoverage_std',
`recent_good_competitor_30d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dltv_max',
`recent_good_competitor_30d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dltv_mean',
`recent_good_competitor_30d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dltv_min',
`recent_good_competitor_30d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dltv_std',
`recent_good_competitor_30d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dtgi_max',
`recent_good_competitor_30d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dtgi_mean',
`recent_good_competitor_30d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dtgi_min',
`recent_good_competitor_30d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30dtgi_std',
`recent_good_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品7d安装次数',
`recent_good_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90d安装次数',
`recent_good_competitor_90d_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dcoverage_max',
`recent_good_competitor_90d_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dcoverage_mean',
`recent_good_competitor_90d_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dcoverage_min',
`recent_good_competitor_90d_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dcoverage_std',
`recent_good_competitor_90d_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dltv_max',
`recent_good_competitor_90d_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dltv_mean',
`recent_good_competitor_90d_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dltv_min',
`recent_good_competitor_90d_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dltv_std',
`recent_good_competitor_90d_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dtgi_max',
`recent_good_competitor_90d_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dtgi_mean',
`recent_good_competitor_90d_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dtgi_min',
`recent_good_competitor_90d_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90dtgi_std',
`recent_good_competitor_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品all安装次数',
`recent_good_competitor_all_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allcoverage_max',
`recent_good_competitor_all_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allcoverage_mean',
`recent_good_competitor_all_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allcoverage_min',
`recent_good_competitor_all_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allcoverage_std',
`recent_good_competitor_all_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allltv_max',
`recent_good_competitor_all_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allltv_mean',
`recent_good_competitor_all_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allltv_min',
`recent_good_competitor_all_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品allltv_std',
`recent_good_competitor_all_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品alltgi_max',
`recent_good_competitor_all_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品alltgi_mean',
`recent_good_competitor_all_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品alltgi_min',
`recent_good_competitor_all_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品alltgi_std',
`recent_good_competitor_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30安装次数',
`recent_good_competitor_d30_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30coverage_max',
`recent_good_competitor_d30_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30coverage_mean',
`recent_good_competitor_d30_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30coverage_min',
`recent_good_competitor_d30_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30coverage_std',
`recent_good_competitor_d30_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30ltv_max',
`recent_good_competitor_d30_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30ltv_mean',
`recent_good_competitor_d30_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30ltv_min',
`recent_good_competitor_d30_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30ltv_std',
`recent_good_competitor_d30_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30tgi_max',
`recent_good_competitor_d30_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30tgi_mean',
`recent_good_competitor_d30_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30tgi_min',
`recent_good_competitor_d30_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d30tgi_std',
`recent_good_competitor_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d60安装次数',
`recent_good_competitor_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90安装次数',
`recent_good_competitor_d90_coverage_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90coverage_max',
`recent_good_competitor_d90_coverage_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90coverage_mean',
`recent_good_competitor_d90_coverage_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90coverage_min',
`recent_good_competitor_d90_coverage_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90coverage_std',
`recent_good_competitor_d90_ltv_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90ltv_max',
`recent_good_competitor_d90_ltv_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90ltv_mean',
`recent_good_competitor_d90_ltv_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90ltv_min',
`recent_good_competitor_d90_ltv_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90ltv_std',
`recent_good_competitor_d90_tgi_max` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90tgi_max',
`recent_good_competitor_d90_tgi_mean` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90tgi_mean',
`recent_good_competitor_d90_tgi_min` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90tgi_min',
`recent_good_competitor_d90_tgi_std` double NOT NULL DEFAULT '-9999999' COMMENT '优质竞品d90tgi_std',
`recent_new_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品180d安装次数',
`recent_new_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品30d安装次数',
`recent_new_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品7d安装次数',
`recent_new_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品90d安装次数',
`recent_new_competitor_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品all安装次数',
`recent_new_competitor_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品d30安装次数',
`recent_new_competitor_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品d60安装次数',
`recent_new_competitor_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品d90安装次数',
`recent_other_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类180d安装次数',
`recent_other_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类30d安装次数',
`recent_other_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类7d安装次数',
`recent_other_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类90d安装次数',
`recent_other_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类all安装次数',
`recent_other_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类d30安装次数',
`recent_other_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类d60安装次数',
`recent_other_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类d90安装次数',
`recent_wallet_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类180d安装次数',
`recent_wallet_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类30d安装次数',
`recent_wallet_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类7d安装次数',
`recent_wallet_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类90d安装次数',
`recent_wallet_all_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类all安装次数',
`recent_wallet_d30_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类d30安装次数',
`recent_wallet_d60_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类d60安装次数',
`recent_wallet_d90_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类d90安装次数',
`reinst_100w_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品180d重安装次数',
`reinst_100w_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30d重安装次数',
`reinst_100w_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品7d重安装次数',
`reinst_100w_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90d重安装次数',
`reinst_ala_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.ala30d重安装次数',
`reinst_ala_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.ala90d重安装次数',
`reinst_all_app_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app180d重安装次数',
`reinst_all_app_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app30d重安装次数',
`reinst_all_app_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app7d重安装次数',
`reinst_all_app_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app90d重安装次数',
`reinst_banco_azteca_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovil30d重安装次数',
`reinst_banco_azteca_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovil90d重安装次数',
`reinst_bank_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类180d重安装次数',
`reinst_bank_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类30d重安装次数',
`reinst_bank_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类7d重安装次数',
`reinst_bank_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类90d重安装次数',
`reinst_baubap_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubap30d重安装次数',
`reinst_baubap_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubap90d重安装次数',
`reinst_bbva_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbanking30d重安装次数',
`reinst_bbva_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbanking90d重安装次数',
`reinst_billetera_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrel30d重安装次数',
`reinst_billetera_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrel90d重安装次数',
`reinst_bnpl_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类180d重安装次数',
`reinst_bnpl_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类30d重安装次数',
`reinst_bnpl_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类7d重安装次数',
`reinst_bnpl_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类90d重安装次数',
`reinst_cfe_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigo30d重安装次数',
`reinst_cfe_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigo90d重安装次数',
`reinst_claro_pay_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.pay30d重安装次数',
`reinst_claro_pay_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.pay90d重安装次数',
`reinst_competition_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品180d重安装次数',
`reinst_competition_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品30d重安装次数',
`reinst_competition_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品7d重安装次数',
`reinst_competition_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品90d重安装次数',
`reinst_coppel_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelapp30d重安装次数',
`reinst_coppel_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelapp90d重安装次数',
`reinst_credmex_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmex30d重安装次数',
`reinst_credmex_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmex90d重安装次数',
`reinst_didi_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloan30d重安装次数',
`reinst_didi_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloan90d重安装次数',
`reinst_finance_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类180d重安装次数',
`reinst_finance_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类30d重安装次数',
`reinst_finance_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类7d重安装次数',
`reinst_finance_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类90d重安装次数',
`reinst_fortaprest_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loan30d重安装次数',
`reinst_fortaprest_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loan90d重安装次数',
`reinst_good_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品180d重安装次数',
`reinst_good_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30d重安装次数',
`reinst_good_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品7d重安装次数',
`reinst_good_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90d重安装次数',
`reinst_klar_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.app30d重安装次数',
`reinst_klar_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.app90d重安装次数',
`reinst_kueski_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.os30d重安装次数',
`reinst_kueski_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.os90d重安装次数',
`reinst_mercado_pago_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.wallet30d重安装次数',
`reinst_mercado_pago_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.wallet90d重安装次数',
`reinst_mexdin_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloan30d重安装次数',
`reinst_mexdin_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloan90d重安装次数',
`reinst_mexicash._30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.app30d重安装次数',
`reinst_mexicash._90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.app90d重安装次数',
`reinst_new_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品180d重安装次数',
`reinst_new_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品30d重安装次数',
`reinst_new_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品7d重安装次数',
`reinst_new_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品90d重安装次数',
`reinst_nu_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.production30d重安装次数',
`reinst_nu_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.production90d重安装次数',
`reinst_other_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类180d重安装次数',
`reinst_other_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类30d重安装次数',
`reinst_other_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类7d重安装次数',
`reinst_other_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类90d重安装次数',
`reinst_oxxo_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobile30d重安装次数',
`reinst_oxxo_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobile90d重安装次数',
`reinst_stori_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.stori30d重安装次数',
`reinst_stori_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.stori90d重安装次数',
`reinst_supermovil_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovil30d重安装次数',
`reinst_supermovil_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovil90d重安装次数',
`reinst_tala_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.tala30d重安装次数',
`reinst_tala_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.tala90d重安装次数',
`reinst_tilt_empower_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mx30d重安装次数',
`reinst_tilt_empower_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mx90d重安装次数',
`reinst_wallet_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类180d重安装次数',
`reinst_wallet_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类30d重安装次数',
`reinst_wallet_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类7d重安装次数',
`reinst_wallet_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类90d重安装次数',
`reinst_whatsapp_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsapp30d重安装次数',
`reinst_whatsapp_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsapp90d重安装次数',
`unload_100w_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品180d卸载次数',
`unload_100w_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30d卸载次数',
`unload_100w_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品7d卸载次数',
`unload_100w_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90d卸载次数',
`unload_ala_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.ala30d卸载次数',
`unload_ala_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.ala90d卸载次数',
`unload_all_app_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app180d卸载次数',
`unload_all_app_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app30d卸载次数',
`unload_all_app_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app7d卸载次数',
`unload_all_app_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app90d卸载次数',
`unload_banco_azteca_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovil30d卸载次数',
`unload_banco_azteca_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovil90d卸载次数',
`unload_bank_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类180d卸载次数',
`unload_bank_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类30d卸载次数',
`unload_bank_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类7d卸载次数',
`unload_bank_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类90d卸载次数',
`unload_baubap_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubap30d卸载次数',
`unload_baubap_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubap90d卸载次数',
`unload_bbva_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbanking30d卸载次数',
`unload_bbva_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbanking90d卸载次数',
`unload_billetera_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrel30d卸载次数',
`unload_billetera_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrel90d卸载次数',
`unload_bnpl_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类180d卸载次数',
`unload_bnpl_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类30d卸载次数',
`unload_bnpl_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类7d卸载次数',
`unload_bnpl_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类90d卸载次数',
`unload_cfe_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigo30d卸载次数',
`unload_cfe_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigo90d卸载次数',
`unload_claro_pay_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.pay30d卸载次数',
`unload_claro_pay_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.pay90d卸载次数',
`unload_competition_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品180d卸载次数',
`unload_competition_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品30d卸载次数',
`unload_competition_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品7d卸载次数',
`unload_competition_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品90d卸载次数',
`unload_coppel_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelapp30d卸载次数',
`unload_coppel_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelapp90d卸载次数',
`unload_credmex_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmex30d卸载次数',
`unload_credmex_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmex90d卸载次数',
`unload_didi_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloan30d卸载次数',
`unload_didi_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloan90d卸载次数',
`unload_finance_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类180d卸载次数',
`unload_finance_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类30d卸载次数',
`unload_finance_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类7d卸载次数',
`unload_finance_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类90d卸载次数',
`unload_fortaprest_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loan30d卸载次数',
`unload_fortaprest_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loan90d卸载次数',
`unload_good_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品180d卸载次数',
`unload_good_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30d卸载次数',
`unload_good_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品7d卸载次数',
`unload_good_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90d卸载次数',
`unload_klar_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.app30d卸载次数',
`unload_klar_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.app90d卸载次数',
`unload_kueski_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.os30d卸载次数',
`unload_kueski_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.os90d卸载次数',
`unload_mercado_pago_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.wallet30d卸载次数',
`unload_mercado_pago_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.wallet90d卸载次数',
`unload_mexdin_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloan30d卸载次数',
`unload_mexdin_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloan90d卸载次数',
`unload_mexicash._30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.app30d卸载次数',
`unload_mexicash._90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.app90d卸载次数',
`unload_new_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品180d卸载次数',
`unload_new_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品30d卸载次数',
`unload_new_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品7d卸载次数',
`unload_new_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品90d卸载次数',
`unload_nu_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.production30d卸载次数',
`unload_nu_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.production90d卸载次数',
`unload_other_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类180d卸载次数',
`unload_other_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类30d卸载次数',
`unload_other_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类7d卸载次数',
`unload_other_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类90d卸载次数',
`unload_oxxo_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobile30d卸载次数',
`unload_oxxo_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobile90d卸载次数',
`unload_stori_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.stori30d卸载次数',
`unload_stori_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.stori90d卸载次数',
`unload_supermovil_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovil30d卸载次数',
`unload_supermovil_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovil90d卸载次数',
`unload_tala_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.tala30d卸载次数',
`unload_tala_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.tala90d卸载次数',
`unload_tilt_empower_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mx30d卸载次数',
`unload_tilt_empower_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mx90d卸载次数',
`unload_wallet_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类180d卸载次数',
`unload_wallet_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类30d卸载次数',
`unload_wallet_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类7d卸载次数',
`unload_wallet_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类90d卸载次数',
`unload_whatsapp_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsapp30d卸载次数',
`unload_whatsapp_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsapp90d卸载次数',
`update_100w_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品180d更新次数',
`update_100w_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品30d更新次数',
`update_100w_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品7d更新次数',
`update_100w_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '百万级竞品90d更新次数',
`update_ala_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.ala30d更新次数',
`update_ala_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'prestamo.dinero.ala90d更新次数',
`update_all_app_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app180d更新次数',
`update_all_app_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app30d更新次数',
`update_all_app_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app7d更新次数',
`update_all_app_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '全部app90d更新次数',
`update_banco_azteca_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovil30d更新次数',
`update_banco_azteca_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.bancoazteca.bazdigitalmovil90d更新次数',
`update_bank_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类180d更新次数',
`update_bank_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类30d更新次数',
`update_bank_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类7d更新次数',
`update_bank_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '银行类90d更新次数',
`update_baubap_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubap30d更新次数',
`update_baubap_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.baubap90d更新次数',
`update_bbva_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbanking30d更新次数',
`update_bbva_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.bancomer.mbanking90d更新次数',
`update_billetera_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrel30d更新次数',
`update_billetera_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.google.android.apps.walletnfcrel90d更新次数',
`update_bnpl_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类180d更新次数',
`update_bnpl_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类30d更新次数',
`update_bnpl_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类7d更新次数',
`update_bnpl_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'bnpl类90d更新次数',
`update_cfe_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigo30d更新次数',
`update_cfe_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.cfe.cfecontigo90d更新次数',
`update_claro_pay_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.pay30d更新次数',
`update_claro_pay_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.globalhitss.claro.pay90d更新次数',
`update_competition_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品180d更新次数',
`update_competition_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品30d更新次数',
`update_competition_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品7d更新次数',
`update_competition_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '竞品90d更新次数',
`update_coppel_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelapp30d更新次数',
`update_coppel_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.coppel.coppelapp90d更新次数',
`update_credmex_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmex30d更新次数',
`update_credmex_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.fintopia.mxcredmex90d更新次数',
`update_didi_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloan30d更新次数',
`update_didi_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.didiglobal.cashloan90d更新次数',
`update_finance_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类180d更新次数',
`update_finance_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类30d更新次数',
`update_finance_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类7d更新次数',
`update_finance_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融类90d更新次数',
`update_fortaprest_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loan30d更新次数',
`update_fortaprest_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.dinero.fd.mx.loan90d更新次数',
`update_good_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品180d更新次数',
`update_good_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品30d更新次数',
`update_good_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品7d更新次数',
`update_good_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '优质竞品90d更新次数',
`update_klar_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.app30d更新次数',
`update_klar_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.klar.app90d更新次数',
`update_kueski_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.os30d更新次数',
`update_kueski_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.kueski.os90d更新次数',
`update_mercado_pago_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.wallet30d更新次数',
`update_mercado_pago_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mercadopago.wallet90d更新次数',
`update_mexdin_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloan30d更新次数',
`update_mexdin_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.elaworld.mexloan90d更新次数',
`update_mexicash._30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.app30d更新次数',
`update_mexicash._90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.mexicash.app90d更新次数',
`update_new_competitor_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品180d更新次数',
`update_new_competitor_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品30d更新次数',
`update_new_competitor_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品7d更新次数',
`update_new_competitor_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '新上架竞品90d更新次数',
`update_nu_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.production30d更新次数',
`update_nu_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.nu.production90d更新次数',
`update_other_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类180d更新次数',
`update_other_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类30d更新次数',
`update_other_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类7d更新次数',
`update_other_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '金融工具类90d更新次数',
`update_oxxo_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobile30d更新次数',
`update_oxxo_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.pagopopmobile90d更新次数',
`update_stori_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.stori30d更新次数',
`update_stori_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'ai.powerup.stori90d更新次数',
`update_supermovil_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovil30d更新次数',
`update_supermovil_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.bancosantander.supermovil90d更新次数',
`update_tala_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.tala30d更新次数',
`update_tala_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'mx.com.tala90d更新次数',
`update_tilt_empower_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mx30d更新次数',
`update_tilt_empower_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'finance.empower.mx90d更新次数',
`update_wallet_180d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类180d更新次数',
`update_wallet_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类30d更新次数',
`update_wallet_7d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类7d更新次数',
`update_wallet_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT '电子钱包类90d更新次数',
`update_whatsapp_30d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsapp30d更新次数',
`update_whatsapp_90d_app_count` int(11) NOT NULL DEFAULT '-9999999' COMMENT 'com.whatsapp90d更新次数',
`feature_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_idx_serial_id` (`serial_id`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_feature_time` (`feature_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='';
"""

import os
import json
import logging
import math

import json
import decimal
import logging
import csv
# import numpy as np
# import pandas as pd



def load_competitor_app_config():
    """加载离线竞品配置"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'files', 'mx_competitor_app_behavior_v1_fea.json')
    with open(file_path, "r") as f:
        return json.load(f)


def load_app_info():
    """加载离线app数据"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'files', 'app.json')
    with open(file_path, "r") as f:
        return json.load(f)

def _mean(v):
    return round(sum(v) / float(len(v)), 4) if v else DEFAULT_VALUE


def _max(v):
    return round(max(v), 4) if v else DEFAULT_VALUE


def _min(v):
    return round(min(v), 4) if v else DEFAULT_VALUE


def _std(v):
    if not v:
        return DEFAULT_VALUE
    n = len(v)
    if n == 1:
        return 0.0
    mu = sum(v) / float(n)
    return round(math.sqrt(sum((x - mu) ** 2 for x in v) / float(n)), 4)


_STAT = {'mean': _mean, 'max': _max, 'min': _min, 'std': _std}

DAY_SEC = 86400.0
DEFAULT_VALUE = -9999999


class SubFeature:
    # _READ_ONLINE_PRODUCTS = CONST_READ_ONLINE_PRODUCTS
    _READ_ONLINE_PRODUCTS = []
    APP_CONFIG_DICT = load_competitor_app_config()

    SINGLE_APP = {
        "stori": "ai.powerup.stori",
        "ala": "prestamo.dinero.ala",
        "coppel": "com.coppel.coppelapp",
        "claro_pay": "com.globalhitss.claro.pay",
        "klar": "mx.klar.app",
        "cfe": "mx.com.cfe.cfecontigo",
        "kueski": "com.kueski.os",
        "didi": "com.didiglobal.cashloan",
        "credmex": "com.fintopia.mxcredmex",
        "nu": "com.nu.production",
        "billetera": "com.google.android.apps.walletnfcrel",
        "mexicash.": "com.mexicash.app",
        "mercado_pago": "com.mercadopago.wallet",
        "banco_azteca": "mx.com.bancoazteca.bazdigitalmovil",
        "mexdin": "com.elaworld.mexloan",
        "supermovil": "mx.bancosantander.supermovil",
        "tala": "mx.com.tala",
        "bbva": "com.bancomer.mbanking",
        "oxxo": "com.pagopopmobile",
        "baubap": "com.baubap",
        "fortaprest": "com.dinero.fd.mx.loan",
        "tilt_empower": "finance.empower.mx",
        "whatsapp": "com.whatsapp"
    }

    NUMERIC_COLS = ('ltv', 'tgi', 'coverage')
    STATS = ('mean', 'max', 'min', 'std')
    ALL_CATS = [
        'competition', 'good_competitor', '100w_competitor', 'new_competitor',
        'all_app', 'finance', 'bank', 'wallet', 'bnpl', 'other',
    ]
    NUMERIC_CATS = ('competition', 'good_competitor', '100w_competitor', 'all_app')
    HISTORY_SKIP = frozenset(['all_app'])
    RECENT_TW = ('all', '180d', '90d', '30d', '7d', 'd30', 'd60', 'd90')
    RECENT_NUMERIC_TW = ('all', '90d', '30d', 'd30', 'd90')
    BEHAVIOR_TW = ('180d', '90d', '30d', '7d')
    SINGLE_TW = ('90d', '30d')

    _RECENT_CNT_PREFIX = 'recent_{}_{}_app_count'
    _RECENT_NUM_PREFIX = 'recent_{}_{}_{}_{}'
    _HISTORY_APP_COUNT = 'history_{}_all_app_count'
    _HISTORY_UNLOAD_COUNT = 'history_{}_all_unload_count'
    _HISTORY_ACTIVE_DAYS = 'history_{}_all_activedays_{}'
    _HISTORY_UNLOAD_DAYS = 'history_{}_all_unloaddays_{}'
    _BEHAVIOR_PREFIX = '{}_{}_{}_app_count'
    _HISTORY_SINGLE_APP_COUNT = 'history_{}_all_app_count'
    _HISTORY_SINGLE_UNLOAD_COUNT = 'history_{}_all_unload_count'
    _HISTORY_SINGLE_ACTIVE_DAYS = 'history_{}_all_activedays_value'
    _HISTORY_SINGLE_UNLOAD_DAYS = 'history_{}_all_unloaddays_value'

    def _parse_and_flatten(self, app_json, serial_id, vir_unix):
        """
        解析多次上报的app JSON，拍平为记录列表，并与配置表left join。
        输入JSON格式：
          app_json : {"<ts>": [{app_name, install_time, update_time, flags}
        输出字段：serial_id, vir_unix, create_unix, packageName, install_time, update_time,
                  genre, finance, good_competitor, 100w_competitor, released_unix, ltv, tgi, coverage
        处理流程：
          1) 按 (create_unix, install_time, update_time, app_name) 升序排序
          2) 按 (create_unix, packageName) 去重，保留最后一条
          3) left join 配置表
        """
        raw = []
        for ts_str, app_list in app_json.items():
            try:
                create_unix = int(ts_str)
            except (ValueError, TypeError):
                continue
            for app in app_list:
                pkg = (app.get('app_name') or '').strip()
                if not pkg:
                    continue
                raw.append((
                    create_unix,
                    app.get('install_time') or 0,
                    app.get('update_time') or 0,
                    pkg,
                ))

        raw.sort()  # 按 (create_unix, install_time, update_time, pkg) 升序
        dedup = {}  # 去重：(create_unix, packageName) 保留最后一条（sort后最后写入的即最大值）
        for create_unix, install_time, update_time, pkg in raw:
            dedup[(create_unix, pkg)] = (install_time, update_time)

        flat = []
        for (create_unix, pkg), (install_time, update_time) in dedup.items():
            cfg = self.APP_CONFIG_DICT.get(pkg, {})
            if cfg:
                flat.append({
                    'serial_id': serial_id,
                    'vir_unix': vir_unix,
                    'create_unix': create_unix,
                    'packageName': pkg,
                    'install_time': install_time,
                    'update_time': update_time,
                    'genre': cfg['genre'],
                    'finance': cfg['finance'],
                    'good_competitor': cfg['good_competitor'],
                    '100w_competitor': cfg['100w_competitor'],
                    'released_unix': cfg['released_unix'],
                    'ltv': cfg['ltv'],
                    'tgi': cfg['tgi'],
                    'coverage': cfg['coverage'],
                })
            else:
                flat.append({
                    'serial_id': serial_id,
                    'vir_unix': vir_unix,
                    'create_unix': create_unix,
                    'packageName': pkg,
                    'install_time': install_time,
                    'update_time': update_time,
                    'genre': None,
                    'finance': None,
                    'good_competitor': None,
                    '100w_competitor': None,
                    'released_unix': None,
                    'ltv': None,
                    'tgi': None,
                    'coverage': None,
                })
        return flat

    def _build_recent(self, flat):
        """最近上报数据集：保留 create_unix 最大的上报记录"""
        if not flat:
            return []
        max_t = max(r['create_unix'] for r in flat)
        return [r for r in flat if r['create_unix'] == max_t]

    def _build_history(self, flat):
        """历史集：按 packageName 去重，保留 (install_time, update_time) 最大的记录"""
        best = {}
        for r in flat:
            pkg = r['packageName']
            if pkg not in best:
                best[pkg] = r
            else:
                prev = best[pkg]
                if (r['install_time'], r['update_time']) > (prev['install_time'], prev['update_time']):
                    best[pkg] = r
        return list(best.values())

    def _build_unload(self, flat, serial_id, vir_unix):
        """
        卸载数据集:找出相比上次上报本次不存在的app。
        每次相邻对比发现app消失就记录,同一个app可以多次卸载(卸载后又重装,再卸载)。

        输出字段:serial_id, vir_unix, packageName, unload_unix, + 配置列
        """
        if not flat:
            return []

        by_time = {}
        for r in flat:
            t = r['create_unix']
            if t not in by_time:
                by_time[t] = set()
            by_time[t].add(r['packageName'])

        times = sorted(by_time.keys())
        if len(times) < 2:
            return []

        result = []

        # 依次对比相邻两次上报,每次发现消失就记录
        for i in range(1, len(times)):
            prev_t = times[i - 1]
            curr_t = times[i]
            # 找出在上一次存在但在当前次不存在的app
            disappeared = by_time[prev_t] - by_time[curr_t]

            for pkg in disappeared:
                cfg = self.APP_CONFIG_DICT.get(pkg, {})
                if cfg:
                    result.append({
                        'serial_id': serial_id,
                        'vir_unix': vir_unix,
                        'packageName': pkg,
                        'unload_unix': curr_t,
                        'genre': cfg['genre'],
                        'finance': cfg['finance'],
                        'good_competitor': cfg['good_competitor'],
                        '100w_competitor': cfg['100w_competitor'],
                        'released_unix': cfg['released_unix'],
                        'ltv': cfg['ltv'],
                        'tgi': cfg['tgi'],
                        'coverage': cfg['coverage'],
                    })
                else:
                    result.append({
                        'serial_id': serial_id,
                        'vir_unix': vir_unix,
                        'packageName': pkg,
                        'unload_unix': curr_t,
                        'genre': None,
                        'finance': None,
                        'good_competitor': None,
                        '100w_competitor': None,
                        'released_unix': None,
                        'ltv': None,
                        'tgi': None,
                        'coverage': None,
                    })

        return result

    # def _build_unload(self, flat, serial_id, vir_unix):
    #     """
    #     卸载数据集：找出相比上次上报本次不存在的app（首次消失）。
    #     unload_unix = 首次未发现该app的上报时间戳。
    #
    #     输出字段：serial_id, vir_unix, packageName, unload_unix, + 配置列
    #     """
    #     if not flat:
    #         return []
    #
    #     by_time = {}
    #     for r in flat:
    #         t = r['create_unix']
    #         if t not in by_time:
    #             by_time[t] = set()
    #         by_time[t].add(r['packageName'])
    #
    #     times = sorted(by_time.keys())
    #     if len(times) < 2:
    #         return []
    #
    #     first_gone = {}  # packageName -> 首次消失的 create_unix
    #     for i in range(1, len(times)):
    #         curr_t = times[i]
    #         disappeared = by_time[times[i - 1]] - by_time[curr_t]
    #         for pkg in disappeared:
    #             if pkg not in first_gone:
    #                 first_gone[pkg] = curr_t
    #
    #     result = []
    #     for pkg, unload_unix in first_gone.items():
    #         cfg = self.APP_CONFIG_DICT.get(pkg, {})
    #         if cfg:
    #             result.append({
    #                 'serial_id': serial_id,
    #                 'vir_unix': vir_unix,
    #                 'packageName': pkg,
    #                 'unload_unix': unload_unix,
    #                 'genre': cfg['genre'],
    #                 'finance': cfg['finance'],
    #                 'good_competitor': cfg['good_competitor'],
    #                 '100w_competitor': cfg['100w_competitor'],
    #                 'released_unix': cfg['released_unix'],
    #                 'ltv': cfg['ltv'],
    #                 'tgi': cfg['tgi'],
    #                 'coverage': cfg['coverage'],
    #             })
    #         else:
    #             result.append({
    #                 'serial_id': serial_id,
    #                 'vir_unix': vir_unix,
    #                 'packageName': pkg,
    #                 'unload_unix': unload_unix,
    #                 'genre': None,
    #                 'finance': None,
    #                 'good_competitor': None,
    #                 '100w_competitor': None,
    #                 'released_unix': None,
    #                 'ltv': None,
    #                 'tgi': None,
    #                 'coverage': None,
    #             })
    #     # print 'result=', result
    #     return result

    def _build_reinstall(self, flat):
        """
        重安装数据集：
          1) 按 (packageName, install_time) 去重，保留最后一条
          2) 去除每个 packageName 中 install_time 最小的记录（首次安装）
          剩余 = 有过重安装行为的记录
        """
        if not flat:
            return []

        dedup = {}
        for r in flat:
            key = (r['packageName'], r['install_time'])
            dedup[key] = r  # flat已升序排序，last write = 最大值记录

        records = list(dedup.values())

        min_inst = {}
        for r in records:
            pkg = r['packageName']
            if pkg not in min_inst or r['install_time'] < min_inst[pkg]:
                min_inst[pkg] = r['install_time']

        return [r for r in records if r['install_time'] != min_inst[r['packageName']]]

    def _build_update(self, flat):
        """
        更新数据集：
          1) 按 (packageName, update_time) 去重，保留最后一条
          2) 去除每个 packageName 中 update_time 最小的记录（首次记录）
          剩余 = 有过非首次更新的记录
        """
        if not flat:
            return []

        dedup = {}
        for r in flat:
            key = (r['packageName'], r['update_time'])
            dedup[key] = r

        records = list(dedup.values())

        min_upd = {}
        for r in records:
            pkg = r['packageName']
            if pkg not in min_upd or r['update_time'] < min_upd[pkg]:
                min_upd[pkg] = r['update_time']

        return [r for r in records if r['update_time'] != min_upd[r['packageName']]]

    def compute_features(self, serial_id, vir_unix, app_json):
        """
        从原始app JSON和配置字典计算全部特征。

        :param app_json:  dict {ts: [...], ...}

        特征命名规则：{场景}_{类别}_{时间窗口}_{算子}_{统计量}
          场景: recent / history / unload / reinstall / update
          类别: finance / bank / wallet / other / bnpl / competition / good_competitor / 100w_competitor / new_competitor
          时间窗口: all / 30d / 60d / 90d / 180d / 360d / d30 / d90 / d180
          算子_统计量: app_count / ltv_mean,max,min,std / tgi_* / coverage_*
          history额外: unload_count / activedays_* / unloaddays_*
        """
        fea = {}

        flat = self._parse_and_flatten(app_json, serial_id, vir_unix)
        if not flat:
            return fea

        # 各场景数据集
        recent = self._build_recent(flat)
        history = self._build_history(flat)
        unload = self._build_unload(flat, serial_id, vir_unix)
        reinstall = self._build_reinstall(flat)
        update = self._build_update(flat)

        def passes_tw(delta, tw):
            """delta（天数）是否落在时间窗口内"""
            if tw == 'all':
                return True
            if tw[0] == 'd':  # d30 / d60 / d90 → 超过N天
                return delta > int(tw[1:])
            return delta <= int(tw[:-1])  # 30d / 7d / 90d → N天以内

        def safe_delta(t):
            """计算 (vir_unix - t) / DAY_SEC，时间戳无效时返回 None"""
            t = t or 0
            if t > 0 and vir_unix > t:
                return (vir_unix - t) / DAY_SEC
            return None

        def get_cats(r):
            """返回记录所属类别列表（一条记录可属于多个类别）"""
            cats = []
            if r.get('genre') == 'Finance':
                cats.append('finance')

            ft = r.get('finance') or ''
            if ft == 'bank':
                cats.append('bank')
            elif ft == 'e-wallet':
                cats.append('wallet')
            elif ft == 'tool':
                cats.append('other')
            elif ft == 'bnpl':
                cats.append('bnpl')
            elif ft == 'loan':
                cats.append('competition')

            if r.get('good_competitor') == 1:
                cats.append('good_competitor')
            if r.get('100w_competitor') == 1:
                cats.append('100w_competitor')
            rel = r.get('released_unix') or 0
            if rel and abs(vir_unix - rel) / DAY_SEC <= 360:
                cats.append('new_competitor')

            cats.append('all_app')
            return cats

        recent_cnt = {}
        recent_num = {}
        numeric_cats = self.NUMERIC_CATS
        for cat in numeric_cats:
            for tw in self.RECENT_NUMERIC_TW:
                for col in self.NUMERIC_COLS:
                    recent_num[(cat, tw, col)] = []

        for r in recent:
            cats = get_cats(r)
            delta = safe_delta(r.get('install_time'))
            for cat in cats:
                for tw in self.RECENT_TW:
                    if tw == 'all' or (delta is not None and passes_tw(delta, tw)):
                        key = (cat, tw)
                        recent_cnt[key] = recent_cnt.get(key, 0) + 1
                if cat in self.NUMERIC_CATS:
                    for tw in self.RECENT_NUMERIC_TW:
                        if tw == 'all' or (delta is not None and passes_tw(delta, tw)):
                            for col in self.NUMERIC_COLS:
                                v = r[col]
                                if v is not None:
                                    recent_num[(cat, tw, col)].append(v)

        all_cats = self.ALL_CATS
        for cat in all_cats:
            for tw in self.RECENT_TW:
                fea[self._RECENT_CNT_PREFIX.format(cat, tw)] = recent_cnt.get((cat, tw), 0)
            if cat in numeric_cats:
                for tw in self.RECENT_NUMERIC_TW:
                    for col in self.NUMERIC_COLS:
                        vals = recent_num.get((cat, tw, col), [])
                        for stat in self.STATS:
                            fea[self._RECENT_NUM_PREFIX.format(cat, tw, col, stat)] = _STAT[stat](vals)

        def accumulate_behavior(records, time_key, scene):
            cnt = {}
            for r in records:
                delta = safe_delta(r.get(time_key))
                if delta is None:
                    continue
                for cat in get_cats(r):
                    for tw in self.BEHAVIOR_TW:
                        if passes_tw(delta, tw):
                            key = (cat, tw)
                            cnt[key] = cnt.get(key, 0) + 1
            behavior_prefix = self._BEHAVIOR_PREFIX
            for cat in all_cats:
                if cat == 'all_app':
                    continue
                for tw in self.BEHAVIOR_TW:
                    fea[behavior_prefix.format(scene, cat, tw)] = cnt.get((cat, tw), 0)

        accumulate_behavior(unload, 'unload_unix', 'unload')
        accumulate_behavior(reinstall, 'install_time', 'reinst')
        accumulate_behavior(update, 'update_time', 'update')

        # ==================== history 场景 ====================
        # 预先按类别分组，避免重复遍历
        hist_by_cat, unld_by_cat = {}, {}

        recent_pkg_by_cat = {}
        for r in recent:
            cats = get_cats(r)
            for cat in cats:
                if cat not in recent_pkg_by_cat:
                    recent_pkg_by_cat[cat] = set()
                recent_pkg_by_cat[cat].add(r['packageName'])

        for cat in self.ALL_CATS:
            if cat in self.HISTORY_SKIP:
                continue
            hist_by_cat[cat] = [r for r in history if cat in get_cats(r)]
            # 卸载数据集：历史中有但 recent 中没有的 app（按 packageName 去重）
            hist_pkgs = {r['packageName'] for r in hist_by_cat[cat]}
            recent_pkgs = recent_pkg_by_cat.get(cat, set())
            unloaded_pkgs = hist_pkgs - recent_pkgs
            unld_by_cat[cat] = [r for r in history if r['packageName'] in unloaded_pkgs]

        stats = self.STATS
        for cat in all_cats:
            if cat in self.HISTORY_SKIP:
                continue
            h_recs = hist_by_cat[cat]
            u_recs = unld_by_cat[cat]

            fea[self._HISTORY_APP_COUNT.format(cat)] = len(h_recs)
            fea[self._HISTORY_UNLOAD_COUNT.format(cat)] = len(u_recs)

            ad_vals = []
            for r in h_recs:
                d = safe_delta(r.get('install_time'))
                if d is not None:
                    ad_vals.append(d)
            for stat in stats:
                fea[self._HISTORY_ACTIVE_DAYS.format(cat, stat)] = _STAT[stat](ad_vals)

            ud_vals = []
            for r in u_recs:
                d = safe_delta(r.get('unload_unix'))
                if d is not None:
                    ud_vals.append(d)
            for stat in stats:
                fea[self._HISTORY_UNLOAD_DAYS.format(cat, stat)] = _STAT[stat](ud_vals)

        history_by_pkg = {r['packageName']: r for r in history}
        unload_by_pkg = {}
        for r in unload:
            pkg = r['packageName']
            if pkg not in unload_by_pkg:
                unload_by_pkg[pkg] = r

        def count_pkg_tw(records, time_key, pkg_name, tws):
            by_tw = {tw: 0 for tw in tws}
            for r in records:
                if r.get('packageName') != pkg_name:
                    continue
                d = safe_delta(r.get(time_key))
                if d is None:
                    continue
                for tw in tws:
                    if passes_tw(d, tw):
                        by_tw[tw] += 1
            return by_tw

        single_app = self.SINGLE_APP
        single_tw = self.SINGLE_TW
        behavior_prefix = self._BEHAVIOR_PREFIX

        for app_key, pkg_name in single_app.items():
            for scene, records, time_key in [
                ('unload', unload, 'unload_unix'),
                ('reinst', reinstall, 'install_time'),
                ('update', update, 'update_time'),
            ]:
                counts = count_pkg_tw(records, time_key, pkg_name, single_tw)
                for tw in single_tw:
                    fea[behavior_prefix.format(scene, app_key, tw)] = counts[tw]

            hist_r = history_by_pkg.get(pkg_name)
            unld_r = unload_by_pkg.get(pkg_name)

            fea[self._HISTORY_SINGLE_APP_COUNT.format(app_key)] = 1 if hist_r else 0
            fea[self._HISTORY_SINGLE_UNLOAD_COUNT.format(app_key)] = 1 if unld_r else 0

            if hist_r:
                d = safe_delta(hist_r.get('install_time'))
                fea[self._HISTORY_SINGLE_ACTIVE_DAYS.format(app_key)] = round(d, 4) if d is not None else DEFAULT_VALUE

            if unld_r:
                d = safe_delta(unld_r.get('unload_unix'))
                fea[self._HISTORY_SINGLE_UNLOAD_DAYS.format(app_key)] = round(d, 4) if d is not None else DEFAULT_VALUE

        return fea

    def _get_fea(self, serial_id, user_id, apply_time):

        app_json = load_app_info()
        # lll =app_json.keys()
        # print 'kkkkkk',lll
        # lll = [int(x) for x in lll]
        # lll.sort()
        # print 'kkkkkk', lll

        fea = self.compute_features(serial_id, apply_time, app_json)
        return fea

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        # elif isinstance(obj, np.bool_):
        #     return bool(obj)
        return super(DecimalEncoder, self).default(obj)

if __name__ == '__main__':
    serial_id = 4926801
    user_id = 1
    apply_time = 1768578215
    fea_ret = SubFeature()._get_fea(serial_id, user_id, apply_time)
    # print fea_ret
    ret = json.dumps(fea_ret, cls=DecimalEncoder)
    print ret
