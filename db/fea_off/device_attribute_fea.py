#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/25 13:39  
"""
from __future__ import division

import json
import re
import math
import traceback

content = [
    {
        "content": {
            "lan_ip": "192.168.1.6",
            "other_device_info": "{\"memory_info\":\"\nMemTotal:        2781436 kB\nMemFree:           75744 kB\nMemAvailable:     588160 kB\nBuffers:            1600 kB\nCached:           655384 kB\nSwapCached:         9008 kB\nActive:           590472 kB\nInactive:         571288 kB\nActive(anon):     268156 kB\nInactive(anon):   246964 kB\nActive(file):     322316 kB\nInactive(file):   324324 kB\nUnevictable:        2560 kB\nMlocked:            2560 kB\nSwapTotal:       1572860 kB\nSwapFree:          64200 kB\nDirty:              1392 kB\nWriteback:             0 kB\nAnonPages:        506044 kB\nMapped:           195144 kB\nShmem:              8620 kB\nSlab:             240412 kB\nSReclaimable:      69200 kB\nSUnreclaim:       171212 kB\nKernelStack:       51456 kB\nPageTables:        66072 kB\nNFS_Unstable:          0 kB\nBounce:                0 kB\nWritebackTmp:          0 kB\nCommitLimit:     2963576 kB\nCommitted_AS:   75942160 kB\nVmallocTotal:   263061440 kB\nVmallocUsed:           0 kB\nVmallocChunk:          0 kB\nCmaTotal:         589824 kB\nCmaFree:              52 kB\nIonTotalCache:     36388 kB\nIonTotalUsed:     220768 kB\nPActive(anon):         0 kB\nPInactive(anon):       0 kB\nPActive(file):     64208 kB\nPInactive(file):       0 kB\nIsolate1Free:      31416 kB\nIsolate2Free:       1520 kB\nRsvTotalUsed:     264196 kB\",\"system_info\":\"_______  system message  2025-07-18 00:10:00 ______________\nID                 :HUAWEIJKM-L03\nBRAND              :HUAWEI\nMODEL              :JKM-LX3\nRELEASE            :9\nSDK                :28\n_______ OTHER _______\nBOARD              :JKM-L03\nPRODUCT            :JKM-LX3\nDEVICE             :HWJKM-H\nFINGERPRINT        :HUAWEI/JKM-LX3/HWJKM-H:9/HUAWEIJKM-L03/9.1.0.309C212:user/release-keys\nHOST               :cn-central-1b-68138391e1596248870596-1515878770-3j0jz\nTAGS               :release-keys\nTYPE               :user\nTIME               :1596252213000\nINCREMENTAL        :9.1.0.309C212\n_______ CUPCAKE-3 _______\nDISPLAY            :JKM-LX3 9.1.0.309(C212E4R1P1)\n_______ DONUT-4 _______\nSDK_INT            :28\nMANUFACTURER       :HUAWEI\nBOOTLOADER         :unknown\nCPU_ABI            :arm64-v8a\nCPU_ABI2           :\nHARDWARE           :kirin710\nUNKNOWN            :unknown\nCODENAME           :REL\n_______ GINGERBREAD-9 _______\nSERIAL             :7MLNW19924000812\",\"cpu_info\":\"\nProcessor\t: AArch64 Processor rev 4 (aarch64)\nprocessor\t: 0\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 1\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 2\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 3\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 4\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd09\nCPU revision\t: 2\n\nprocessor\t: 5\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd09\nCPU revision\t: 2\n\nprocessor\t: 6\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd09\nCPU revision\t: 2\n\nprocessor\t: 7\nBogoMIPS\t: 3.84\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd09\nCPU revision\t: 2\n\",\"telephone_info\":\"_______ Phone info  2025-07-18 00:10:00 ______________null  Phone number：+525625811995 IMSI is：334050172497788\nDeviceID(IMEI)       :865365047349759\nDeviceSoftwareVersion:90\ngetLine1Number       :+525625811995\nNetworkCountryIso    :mx\nNetworkOperator      :334050\nNetworkOperatorName  :UNEFON\nNetworkType          :13\nPhoneType            :1\nSimCountryIso        :mx\nSimOperator          :334050\nSimOperatorName      :\nSimSerialNumber      :8952050011917683781F\ngetSimState          :5\nSubscriberId         :334050172497788\nVoiceMailNumber      :*86\",\"user_agent\":\"Kaby;1.4.5;Android;9;JKM-LX3 9.1.0.309(C212E4R1P1);HUAWEI;JKM-LX3;1080*2137;ca5170d4a6ef9e1c897387041e0a2133;WIFI;\"}",
            "base_station_3g": "",
            "is_emulator": "0",
            "is_vm": "0",
            "app_list": "com.amazon.mp3:Amazon Music,com.google.android.apps.youtube.music:YouTube Music,com.spotify.music:Spotify,com.truecaller:Truecaller,ar.com.bancar.uala:Ualá,com.att.miunefonmx:Mi Unefon,com.casual.tile.riddle.tactics.ceramic:Casual Tile,com.didiglobal.passenger:DiDi,com.dreamgames.royalkingdom:Royal Kingdom,com.facebook.katana:Facebook,com.facebook.orca:Messenger,com.game.suf_android:Screw Up Family,com.gmatch3d.tgoods:Goods Match 3D,com.kaby:Kaby,com.kiwi.merchant:KiWi,com.mercadopago.wallet:Mercado Pago,com.netflix.mediaclient:Netflix,com.rook.browser.magical:Rook Browser,com.univision.prendetv:ViX,com.vitastudio.mahjong:Vita Mahjong,com.whatsapp:WhatsApp,com.zhiliaoapp.musically.go:TikTok Lite,mx.aos.clicredito:CliCredito,mx.com.bancoazteca.bazdigitalmovil:Banco Azteca,mx.loaney.app:Loaney",
            "phone_sim_info": "{\"phones\":\"+525625811995\",\"phoneCount\":\"1\",\"phoneMaxCount\":\"1\"}",
            "is_lock_screen": "1",
            "local_mobile": "+525625811995",
            "is_root": "0",
            "webview_kernel": "Mozilla/5.0 (Linux; Android 9; JKM-LX3 Build/HUAWEIJKM-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.63 Mobile Safari/537.36",
            "dual_sim_info": "{\"isDualSIM\":\"1\",\"imeiSIM1\":\"865365047349759\",\"imeiSIM2\":\"865365047349759\",\"imsiSIM1\":\"null\n\",\"imsiSIM2\":\"null\n\",\"isSIM2Ready\":\"0\",\"isSIM1Ready\":\"1\"}",
            "boot_time": "137:21",
            "is_mod": "1",
            "permission": "{\"CAMERA\":false,\"READ_SMS\":true,\"READ_PHONE_STATE\":true,\"ACCESS_COARSE_LOCATION\":false,\"NOTIFICATIONS\":true}",
            "a_space": "56461623296",
            "r_space": "27418902528",
            "wifi_mac": "04:4A:6C:4F:00:BB",
            "wifi_ssid": "<unknown ssid>",
            "battery": "{\"invalid_charger\":\"0\",\"level\":\"21\",\"health\":\"good\",\"scale\":\"100\",\"icon_small\":\"17303484\",\"technology\":\"Li-poly\",\"charge_counter\":\"581000\",\"current_now\":\"0\",\"voltage\":\"3599\",\"capacity\":\"0\",\"temperature\":\"340\",\"present\":\"true\",\"battery_low\":\"false\",\"is_power_save\":\"true\",\"plugged\":\"\",\"status\":\"discharging\"}"
        },
        "create_time": 1752819002
    },
    {
        "content": {
            "lan_ip": "192.168.1.9",
            "other_device_info": "{\"memory_info\":\"\nMemTotal:        3860612 kB\nMemFree:          323856 kB\nMemAvailable:    1386100 kB\nBuffers:            2000 kB\nCached:          1323696 kB\nSwapCached:        33968 kB\nActive:           847644 kB\nInactive:        1166276 kB\nActive(anon):     430932 kB\nInactive(anon):   442336 kB\nActive(file):     416712 kB\nInactive(file):   723940 kB\nUnevictable:      172696 kB\nMlocked:          172696 kB\nSwapTotal:       2122872 kB\nSwapFree:         638632 kB\nDirty:               540 kB\nWriteback:             4 kB\nAnonPages:        853024 kB\nMapped:           852952 kB\nShmem:             15264 kB\nKReclaimable:     107380 kB\nSlab:             287176 kB\nSReclaimable:      81684 kB\nSUnreclaim:       205492 kB\nKernelStack:       58184 kB\nPageTables:        98708 kB\nNFS_Unstable:          0 kB\nBounce:                0 kB\nWritebackTmp:          0 kB\nCommitLimit:     4053176 kB\nCommitted_AS:   73851532 kB\nVmallocTotal:   263061440 kB\nVmallocUsed:      108080 kB\nVmallocChunk:          0 kB\nPercpu:             8800 kB\nCmaTotal:         540672 kB\nCmaFree:          245628 kB\",\"system_info\":\"_______  system message  2024-04-10 07:54:47 ______________\nID                 :STAS32.79-77-28-55-13\nBRAND              :motorola\nMODEL              :moto g22\nRELEASE            :12\nSDK                :31\n_______ OTHER _______\nBOARD              :p410ae\nPRODUCT            :hawaiip_g\nDEVICE             :hawaiip\nFINGERPRINT        :motorola/hawaiip_g/hawaiip:12/STAS32.79-77-28-55-13/77-28-55-13:user/release-keys\nHOST               :HTSVR18\nTAGS               :release-keys\nTYPE               :user\nTIME               :1708222089000\nINCREMENTAL        :77-28-55-13\n_______ CUPCAKE-3 _______\nDISPLAY            :STAS32.79-77-28-55-13\n_______ DONUT-4 _______\nSDK_INT            :31\nMANUFACTURER       :motorola\nBOOTLOADER         :0x0218\nCPU_ABI            :arm64-v8a\nCPU_ABI2           :\nHARDWARE           :mt6765\nUNKNOWN            :unknown\nCODENAME           :REL\n_______ GINGERBREAD-9 _______\nSERIAL             :\",\"cpu_info\":\"\nprocessor\t: 0\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 1\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 2\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 3\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 4\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 5\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 6\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nprocessor\t: 7\nBogoMIPS\t: 26.00\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x0\nCPU part\t: 0xd03\nCPU revision\t: 4\n\nHardware\t: MT6765H\nHardware\t: MT6765H\",\"telephone_info\":\"_______ Phone info  2024-04-10 07:54:47 ______________null  Phone number：+525625811995 IMSI is：\nDeviceID(IMEI)       :\nDeviceSoftwareVersion:05\ngetLine1Number       :+525625811995\nNetworkCountryIso    :mx\nNetworkOperator      :334050\nNetworkOperatorName  :UNEFON\nNetworkType          :13\nPhoneType            :1\nSimCountryIso        :mx\nSimOperator          :334050\nSimOperatorName      :UNEFON\nSimSerialNumber      :\ngetSimState          :5\nSubscriberId         :\nVoiceMailNumber      :*86\",\"user_agent\":\"Kaby;1.3.9;Android;12;STAS32.79-77-28-55-13;motorola;moto g22;720*1440;d41d8cd98f00b204e9800998ecf8427e;WIFI;\"}",
            "base_station_3g": "",
            "is_emulator": "0",
            "is_vm": "0",
            "app_list": "com.bancomer.mbanking:BBVA México,com.google.android.apps.docs.editors.docs:Documentos,com.king.candycrushsodasaga:Candy Crush Soda,com.whatsapp:WhatsApp,com.google.android.apps.docs.editors.sheets:Hojas de cálculo,com.google.android.apps.docs.editors.slides:Diapositivas,com.amazon.mp3:Amazon Music,com.kaby:Kaby,brain.blow.quest:Brain Blow,com.block.juggle:Block Blast!,com.tripledot.solitaire:Solitaire,com.n3twork.tetris:Tetris,com.netflix.mediaclient:Netflix,com.zhiliaoapp.musically:TikTok,com.spotify.music:Spotify,com.amazon.avod.thirdpartyclient:Prime Video,com.didiglobal.passenger:DiDi,com.supercell.brawlstars:Brawl Stars,com.facebook.orca:Messenger,com.playrix.homescapes:Homescapes,com.blackout.word:Sopas de letras,com.opera.app.news:Opera News,com.univision.prendetv:ViX,com.dreamgames.royalmatch:Royal Match,games.spearmint.triplecrush:Tiledom,com.bastion.archers:Archery Bastions,com.fugo.wow:WoW",
            "phone_sim_info": "{\"phones\":\"+525625811995\",\"phoneCount\":\"1\",\"phoneMaxCount\":\"1\"}",
            "permission": "{\"CAMERA\":true,\"READ_PHONE_STATE\":true,\"READ_CALL_LOG\":true,\"READ_SMS\":true,\"READ_CONTACTS\":false,\"READ_EXTERNAL_STORAGE\":false,\"WRITE_EXTERNAL_STORAGE\":false,\"READ_HISTORY_BOOKMARKS\":false,\"READ_CALENDAR\":true,\"WRITE_CALENDAR\":true,\"ACCESS_FINE_LOCATION\":false,\"ACCESS_COARSE_LOCATION\":true,\"NOTIFICATIONS\":true}",
            "local_mobile": "+525625811995",
            "is_root": "0",
            "webview_kernel": "Mozilla/5.0 (Linux; Android 12; moto g22 Build/STAS32.79-77-28-55-13; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.99 Mobile Safari/537.36",
            "dual_sim_info": "{\"isDualSIM\":\"1\",\"imeiSIM1\":\"\",\"imeiSIM2\":\"\",\"imsiSIM1\":\"\",\"imsiSIM2\":\"\",\"isSIM2Ready\":\"0\",\"isSIM1Ready\":\"0\"}",
            "boot_time": "72:42",
            "is_mod": "1",
            "a_space": "117351350272",
            "r_space": "92098179072",
            "wifi_mac": "",
            "wifi_ssid": "<unknown ssid>",
            "battery": "{\"invalid_charger\":\"0\",\"level\":\"20\",\"health\":\"good\",\"scale\":\"100\",\"icon_small\":\"17303567\",\"technology\":\"Li-ion\",\"charge_counter\":\"970000\",\"current_now\":\"0\",\"voltage\":\"3666\",\"capacity\":\"0\",\"temperature\":\"312\",\"present\":\"true\",\"battery_low\":\"false\",\"is_power_save\":\"false\",\"plugged\":\"\",\"status\":\"discharging\"}"
        },
        "create_time": 1712757288
    }
]
DEFALUT_VALUE = "-9999999"
VIRTUAL_OPERATOR_NAME = ['izzi mvno', 'tracfone', 'unefon', 'mvno']



def _calc_battery_fea( content, battery_size):
    """
    计算battery特征
    """
    fea = {}
    battery = json.loads(content.get('battery', '{}'))
    if not battery:
        return fea
    cols = ['level', 'temperature', 'voltage', 'status', 'health']
    for c in cols:
        if c == 'temperature':
            fea['battery_temperature'] = float(battery.get('temperature', 0)) / 10
        if c == 'voltage':
            fea['battery_voltage'] = float(battery.get('voltage', 0)) / 1000
        else:
            fea['battery_%s' % c] = battery.get(c)
    if battery_size:
        fea['charged_cycle_cnts'] = int(battery['charge_counter']) / battery_size
        score1 = 0 if fea['battery_health'] == 'good' else 5
        calculate_score2 = lambda charged_cycle_cnts: (
            1 if charged_cycle_cnts > 500 else
            3 if charged_cycle_cnts > 200 else
            2 if charged_cycle_cnts > 100 else
            0
        )
        fea['battery_risky_index'] = score1 + calculate_score2(fea['charged_cycle_cnts'])
    return fea


def _is_invalid_imei(imei):
    if not imei:
        return 1
    if len(imei) != 15 or not imei.isdigit():
        return 1
    total = 0
    for i, char in enumerate(imei):
        digit = int(char)
        if (i + 1) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit = digit // 10 + digit % 10
        total += digit
    return 1 if total % 10 != 0 else 0


def _parse_cpuinfo( content):
    """
    把 /proc/cpuinfo 文本解析成 dict。
    返回值形如：
    {
      "Processor": "AArch64 Processor rev 4 (aarch64)",
      "processors": [
        {...},
        ...
      ]
    }
    """
    lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
    kv_pattern = re.compile(r'^([^:]+?)\t*:\s*(.+)$')

    global_kv = {}
    processors = []
    current = {}

    for line in lines:
        m = kv_pattern.match(line)
        if not m:
            continue
        key, val = m.group(1).strip(), m.group(2).strip()

        # 如果 key 是 processor 且不是第一次出现，就把上一段存进去
        if key == "processor":
            if current:
                processors.append(current)
            current = {key: val}
        else:
            # 如果还没遇到 processor，则认为是全局字段
            if not current:
                global_kv[key] = val
            else:
                current[key] = val

    # 最后一段
    if current:
        processors.append(current)
    # result = global_kv.copy()
    # result["processors"] = processors
    return processors


def _check_virtualization(processors):
    """
    检查所有核心BogoMIPS值是否完全相同
    真实设备应有0.1-0.3的浮动差异
    """
    bogomips_values = [p["BogoMIPS"] for p in processors]
    return len(set(bogomips_values))


def _check_forged_device(processors):
    """
    检查不同架构核心是否报告相同特性集
    真实设备中A55和A76应有不同特性
    """
    # 按核心架构分组
    core_groups = {}
    for p in processors:
        core_type = p["CPU part"]
        if core_type not in core_groups:
            core_groups[core_type] = set(p["Features"])

    # 比较不同组的特性集
    features_sets = core_groups.values()
    for i in range(1, len(features_sets)):
        if features_sets[i] != features_sets[0]:
            return 0  # 特性不同，正常设备
    return 1  # 所有核心特性相同，风险高


def _check_security_flaw( processors):
    """
    检查是否缺少关键安全扩展
    """
    all_features = set()
    for p in processors:
        all_features.update(p["Features"])

    required_extensions = {"vm", "hvc", "vhe", "sve", "sve2"}
    missing_extensions = required_extensions - all_features
    return len(missing_extensions)  # 缺少3项以上为高风险


def _check_engineering_sample( processors):
    """
    检查是否为工程测试芯片
    """
    first_core = processors[0]
    return 1 if (
            first_core["CPU implementer"] == "0x41" and  # ARM原始标识
            first_core["CPU variant"] == "0x0" and  # 未商业化版本
            all(int(p["CPU revision"]) < 3 for p in processors)  # 修订版本过低
    ) else 0


def _check_virtualization_flaw(processors):
    """
    检查是否缺少虚拟化扩展
    """
    all_features = set()
    for p in processors:
        all_features.update(p["Features"])

    virt_extensions = {"vm", "hvc", "vhe"}
    return 1 if virt_extensions.isdisjoint(all_features) else 0  # 完全缺失返回True

def _round_func(value, num=2):
    return round(value, num)

def _calc_cpu_fea(content):
    """
        计算cpu_info特征
    """
    fea = {}
    cpu_info = content.get('cpu_info', '')
    cpu_dict = _parse_cpuinfo(cpu_info)
    # print "cpu_dict", json.dumps(cpu_dict)
    # fea['cpu_info'] = cpu_info
    fea['risk_virtualization'] = _check_virtualization(cpu_dict)
    fea['risk_forged_device'] = _check_forged_device(cpu_dict)
    fea['risk_security_flaw'] = _check_security_flaw(cpu_dict)
    fea['risk_engineering_sample'] = _check_engineering_sample(cpu_dict)
    fea['risk_virtualization_flaw'] = _check_virtualization_flaw(cpu_dict)
    calculate_score = lambda rv, fd, sf, es, vf: \
        (2 if rv == 1 else 0) + \
        (2 if fd else 0) + \
        (1 if sf <= 2 else 3 if sf >= 1 else 0) + \
        (2 if es else 0) + \
        (2 if vf else 0)
    fea['cpu_risky_index'] = calculate_score(fea['risk_virtualization'], fea['risk_forged_device'] , fea['risk_security_flaw'], fea['risk_engineering_sample'], fea['risk_virtualization_flaw'])
    # fea['cpu_risky_index'] = calculate_score(fea['risk_virtualization'], fea['risk_forged_device'], fea['risk_security_flaw'], fea['risk_engineering_sample'], fea['risk_virtualization_flaw'])
    return fea


def _calc_memory_fea(content):
    """
            计算memory特征
            """
    fea, mem_data = {}, {}
    memory_usage_rate, memory_pressure_index, exchangespace_usage_rate, ion_usage_rate, reserve_memory_rate, memory_health_index, memory_leak_risk_index = 0, 0, 0, 0, 0, 0, 0
    key_list = ['MemTotal', 'SwapTotal', 'SwapFree', 'IonTotalUsed', 'IonTotalCache', 'SUnreclaim', 'Slab',
                'CmaFree', 'CmaTotal', 'MemAvailable', 'RsvTotalUsed', 'Active', 'Inactive']
    lists = filter(None, content.get('memory_info', '').split('\n'))
    if lists:
        infos = {
            x.split(':')[0].strip().replace('(', '_').replace(')', ''): x.split(':')[1].replace('kB', '').strip()
            for x in lists if x != ''}
        fea['memory_info'] = infos
        for i in key_list:
            temp = infos.get(i, '')
            mem_data[i] = int(temp) if temp and temp.isdigit() else None
        memtotal_latest = mem_data['MemTotal']
        iontoalused = mem_data['IonTotalUsed']
        iontotalcache = mem_data['IonTotalCache']
        if memtotal_latest:
            fea['memory'] = math.ceil(memtotal_latest / 1000)
            if mem_data['MemAvailable'] is not None:
                memory_usage_rate = (1 - mem_data['MemAvailable'] / memtotal_latest) * 100
                memory_pressure_index = (mem_data['Active'] + mem_data['Inactive']) / memtotal_latest * 100
            if mem_data['RsvTotalUsed'] is not None:
                reserve_memory_rate = mem_data['RsvTotalUsed'] / memtotal_latest
        fea['memory_usage_rate'] = _round_func(memory_usage_rate)
        fea['memory_pressure_index'] = _round_func(memory_pressure_index)
        fea['reserve_memory_rate'] = _round_func(reserve_memory_rate)
        if mem_data['SwapFree'] is not None and mem_data['SwapTotal']:
            exchangespace_usage_rate = (1 - mem_data['SwapFree'] / mem_data['SwapTotal']) * 100
        fea['exchangespace_usage_rate'] = _round_func(exchangespace_usage_rate)
        if iontoalused is not None and iontotalcache is not None:
            ion_usage_rate = iontoalused / (
                    iontoalused + iontotalcache) * 100 if iontoalused + iontotalcache != 0 else 0
        fea['ion_usage_rate'] = _round_func(ion_usage_rate)
        memory_leak_risk_index = mem_data['SUnreclaim'] / mem_data['Slab'] if mem_data['Slab'] else 0
        fea['memory_leak_risk_index'] = _round_func(memory_leak_risk_index)
        cma_usage_rate = mem_data['CmaFree'] / mem_data['CmaTotal'] if mem_data['CmaTotal'] else 0
        fea['cma_usage_rate'] = _round_func(cma_usage_rate)
        memory_health_index = 0.4 * (1 - memory_usage_rate) + 0.3 * (1 - exchangespace_usage_rate) + 0.1 * (
                1 - memory_leak_risk_index) + 0.1 * (1 - reserve_memory_rate) + 0.1 * (1 - cma_usage_rate)
        fea['memory_health_index'] = _round_func(memory_health_index)
    fea = json.dumps(fea)
    return fea


def _calc_telephone_fea(content):
    fea, data = {}, {}
    fea_ = ['NetworkOperatorName', 'SimOperatorName', 'getSimState', 'DeviceID(IMEI)',
            'DeviceSoftwareVersion', 'SimSerialNumber', 'SimOperator', 'PhoneType',
            'NetworkType']

    # 处理逻辑
    lists = filter(None, content.get('telephone_info', '').split('\n'))
    if lists:
        infos = {x.split(':')[0].strip().replace('(', '_').replace(')', ''): x.split(':')[1].strip() for x in lists
                 if '__' not in x and ':' in x}
        fea['telephone_info'] = infos
        print json.dumps(infos)
        for i in fea_:
            if i not in infos:
                value = None
            else:
                value = infos[i] if infos[i] != 'null' else ''
            # if not value_ or 'null' in value_:
            #     continue
            data[i] = value

        icc_id = data['SimSerialNumber']
        sim_operator = data['SimOperator']

        fea['is_virtual_operator'] = 1 if data['NetworkOperatorName'] in VIRTUAL_OPERATOR_NAME else 0
        fea['is_null_simOperatorName'] = (
            1 if not data['NetworkOperatorName'] else 0) if data['NetworkOperatorName'] is not None else DEFALUT_VALUE
        fea['simState'] = data['getSimState']

        fea['is_invalid_imei'] =  _is_invalid_imei(data['DeviceID(IMEI)'])
        print data['DeviceSoftwareVersion']
        fea['deviceSoftwareVersion'] = data['DeviceSoftwareVersion']
        fea['is_digital_iccid'] = 1 if icc_id and icc_id.isdigit() else 0
        fea['is_mx_iccid'] = (1 if icc_id[2:4] == 52 else 0) if icc_id else DEFALUT_VALUE
        fea['is_mx_simOperator'] = (
            1 if sim_operator[:3] == '334' else 0) if sim_operator else DEFALUT_VALUE
        fea['is_network_spoof_risk'] = 1 if data['PhoneType'] == '1' and int(data['NetworkType']) > 10 else 0
        calculate_score = lambda v1, v2, v3, v4, v5, v6: (2 if v1 else 0) + (2 if v2 else 0) + (
            2 if v3 else 0) + (2 if v4 else 0) + (2 if v5 else 0) + (2 if v6 else 0)
        fea['telephone_risky_index'] = calculate_score(fea['is_virtual_operator'],
                                                       fea['is_null_simOperatorName'], fea['is_invalid_imei'],
                                                       fea['is_digital_iccid'], fea['is_mx_simOperator'],
                                                       fea['is_network_spoof_risk'])
    fea = json.dumps(fea)
    return fea

def _get_basic_info(content, memory_health_index, battery_risky_index, cpu_risky_index, telephone_risky_index):
    fea = {}
    is_emulator = content.get('is_emulator', '0')
    is_vm = content.get('is_vm', '0')
    is_root = content.get('is_root', '0')
    is_mod = content.get('is_mod', '0')
    app_list = content.get('app_list', {})
    boot_time = content.get('boot_time')

    # 计算风险指标
    fea['is_emulator_risky'] = 1 if (int(is_emulator) | int(is_vm)) else 0
    fea['is_root_risk'] = 1 if (int(is_root) | int(is_mod)) else 0
    fea['is_tamper_risky'] = 1 if ('com.sollyu.xposed.hook.model' in app_list or 'com.topjohnwu.magisk' in app_list) else 0
    fea['total_storage_space'] = int(content.get('a_space', 0))
    fea['free_storage_space'] = int(content.get('r_space', 0))
    fea['spce_usage_rate'] = _round_func(1 - (float(fea['free_storage_space']) / fea['total_storage_space'])) if fea['total_storage_space'] != 0 else 0
    fea['is_proxy_risky'] = 1 if ('proxy' in content.get('webview_kernel', '').lower() or
                                  'vpn' in app_list.lower()) else 0
    if boot_time:
        boot_time_parts = boot_time.split(':')
        fea['boot_hours'] = int(boot_time_parts[0]) + int(boot_time_parts[1]) / 60
    calculate_score = lambda er, rr, tr, pr: \
        (2 if er else 0) + \
        (2 if rr else 0) + \
        (2 if tr else 0) + \
        (2 if pr else 0)
    fea['system_risky_index'] = calculate_score(fea['is_emulator_risky'], fea['is_root_risk'], fea['is_tamper_risky'] , fea['is_proxy_risky'])
    try:
        fea['device_risky_index'] = (1 - memory_health_index) * 10 + \
                                    battery_risky_index + \
                                    cpu_risky_index + \
                                    telephone_risky_index + \
                                    fea['system_risky_index']
    except:
        fea['device_risky_index'] = 0
    return fea


odi_latest = content[0].get('content').get("other_device_info", {})

try:
    other_device_info = json.loads(odi_latest.replace('&quot;', '"'), strict=False)
except:
    try:
        other_device_info = json.loads(odi_latest.replace('&quot;', '"') + '"}', strict=False)
        print "other_device_info:2", other_device_info
    except:
        print 'error'


# print _calc_cpu_fea(other_device_info)
# print _calc_memory_fea(other_device_info)
# print _calc_telephone_fea(other_device_info)



def _calc_memory_fea(content):
    """
    计算memory特征
    """

    content = {u'cpu_info': u'\nprocessor\t: 0\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x2\nCPU part\t: 0xd05\nCPU revision\t: 0\n\nprocessor\t: 1\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x2\nCPU part\t: 0xd05\nCPU revision\t: 0\n\nprocessor\t: 2\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x2\nCPU part\t: 0xd05\nCPU revision\t: 0\n\nprocessor\t: 3\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x2\nCPU part\t: 0xd05\nCPU revision\t: 0\n\nprocessor\t: 4\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x1\nCPU part\t: 0xd41\nCPU revision\t: 1\n\nprocessor\t: 5\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x1\nCPU part\t: 0xd41\nCPU revision\t: 1\n\nprocessor\t: 6\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x1\nCPU part\t: 0xd41\nCPU revision\t: 1\n\nprocessor\t: 7\nBogoMIPS\t: 38.40\nFeatures\t: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp\nCPU implementer\t: 0x41\nCPU architecture: 8\nCPU variant\t: 0x1\nCPU part\t: 0xd41\nCPU revision\t: 1\n\nHardware\t: SM7325', u'memory_info': u'\nMemTotal:        7526712 kB\nMemFree:          106164 kB\nMemAvailable:    1855728 kB\nBuffers:            3960 kB\nCached:          2047028 kB\nSwapCached:        32004 kB\nActive:          1729664 kB\nInactive:        2442416 kB\nActive(anon):    1200032 kB\nInactive(anon):  1132056 kB\nActive(file):     529632 kB\nInactive(file):  1310360 kB\nUnevictable:      167564 kB\nMlocked:          166544 kB\nSwapTotal:       8388604 kB\nSwapFree:        5686372 kB\nZramUsed:         895124 kB\nDirty:              1716 kB\nWriteback:             0 kB\nAnonPages:       2277636 kB\nMapped:          1212080 kB\nShmem:             45636 kB\nKReclaimable:     238168 kB\nSlab:             652992 kB\nSReclaimable:     161228 kB\nSUnreclaim:       491764 kB\nKernelStack:      116320 kB\nPageTables:       158564 kB\nNFS_Unstable:          0 kB\nBounce:                0 kB\nWritebackTmp:          0 kB\nCommitLimit:    12151960 kB\nCommitted_AS:   177072872 kB\nVmallocTotal:   262930368 kB\nVmallocUsed:      100956 kB\nVmallocChunk:          0 kB\nPercpu:            12256 kB\nHardwareCorrupted:     0 kB\nCmaTotal:         438272 kB\nCmaFree:             148 kB\nCmaUsed:           67772 kB\nIonTotalCache:     50752 kB\nIonTotalUsed:     225220 kB\nGpuTotalUsed      533016 kB\nAshmemUsed        286944 kB\nRsvTotalUsed      710516 kB\nProtected:        103892 kB', u'system_info': u'_______  system message  2023-12-19 11:52:20 ______________\nID                 :HUAWEINAM-L09\nBRAND              :HUAWEI\nMODEL              :VOG-TL00\nRELEASE            :11\nSDK                :30\n_______ OTHER _______\nBOARD              :NAM\nPRODUCT            :VOG-TL00\nDEVICE             :HWVOG\nFINGERPRINT        :HUAWEI/VOG-TL00/HWVOG:10/HUAWEIVOG-TL00/10.1.0.162C01:user/release-keys\nHOST               :cn-central-hcd-2a-a7464798c1697609544165-5f87bfbbf8-vkjkc\nTAGS               :release-keys\nTYPE               :user\nTIME               :1697613197000\nINCREMENTAL        :102.0.1.304C69\n_______ CUPCAKE-3 _______\nDISPLAY            :NAM-L09 12.0.1.304(C69E11R1P2)\n_______ DONUT-4 _______\nSDK_INT            :30\nMANUFACTURER       :HUAWEI\nBOOTLOADER         :unknown\nCPU_ABI            :arm64-v8a\nCPU_ABI2           :\nHARDWARE           :qcom\nUNKNOWN            :unknown\nCODENAME           :REL\n_______ GINGERBREAD-9 _______\nSERIAL             :unknown', u'user_agent': u'Kaby;1.3.5;Android;11;NAM-L09 12.0.1.304(C69E11R1P2);HUAWEI;VOG-TL00;1080*2241;04882295e0ac638ece3d396d8064794b;WIFI;', u'telephone_info': u'_______ Phone info  2023-12-19 11:52:20 ______________null  Phone number\uff1a IMSI is\uff1aunknown\nDeviceID(IMEI)       :489498812676725\nDeviceSoftwareVersion:31\ngetLine1Number       :\nNetworkCountryIso    :mx\nNetworkOperator      :\nNetworkOperatorName  :TELCEL\nNetworkType          :18\nPhoneType            :1\nSimCountryIso        :mx\nSimOperator          :334020\nSimOperatorName      :TELCEL\nSimSerialNumber      :48949881267672530281\ngetSimState          :5\nSubscriberId         :unknown\nVoiceMailNumber      :*86'}
    fea, mem_data= {}, {}
    (memory_usage_rate, memory_pressure_index, exchangespace_usage_rate, ion_usage_rate, reserve_memory_rate,
     memory_health_index, memory_leak_risk_index) = 0, 0, 0, 0, 0, 0, 0
    key_list = ['MemTotal', 'SwapTotal', 'SwapFree', 'IonTotalUsed', 'IonTotalCache', 'SUnreclaim', 'Slab',
            'CmaFree', 'CmaTotal', 'MemAvailable', 'RsvTotalUsed', 'Active', 'Inactive']
    lists = filter(None, content.get('memory_info', '').split('\n'))
    if lists:
        # infos = {
        #     x.split(':')[0].strip().replace('(', '_').replace(')', ''): x.split(':')[1].replace('kB', '').strip()
        #     for x in lists if x != ''}
        # todo test
        try:
            infos = {
                x.split(':')[0].strip().replace('(', '_').replace(')', ''): x.split(':')[1].replace('kB',
                                                                                                    '').strip()
                for x in lists if x != '' and len(x.split(':')) == 2}
        except Exception as e:
            print e, traceback.format_exc()
            print "error"

        # fea['memory_info'] = infos
        for i in key_list:
            temp = infos.get(i, '')
            mem_data[i]= int(temp) if temp and temp.isdigit() else None
        mem_total = mem_data['MemTotal']
        iontoalused = mem_data['IonTotalUsed']
        iontotalcache = mem_data['IonTotalCache']
        if mem_total:
            fea['memory'] = math.ceil(mem_total / 1000)
            if mem_data['MemAvailable'] is not None:
                memory_usage_rate = (1 - mem_data['MemAvailable'] / mem_total)
                memory_pressure_index = (mem_data['Active'] + mem_data['Inactive']) / mem_total * 100
            if mem_data['RsvTotalUsed'] is not None:
                reserve_memory_rate = mem_data['RsvTotalUsed'] / mem_total
        fea['memory_usage_rate'] = round(memory_usage_rate * 100)
        fea['memory_pressure_index'] = round(memory_pressure_index)
        fea['reserve_memory_rate'] = round(reserve_memory_rate)
        if mem_data['SwapFree'] is not None and mem_data['SwapTotal']:
            exchangespace_usage_rate = (1 - mem_data['SwapFree'] / mem_data['SwapTotal'])
        fea['exchangespace_usage_rate'] = round(exchangespace_usage_rate)
        if iontoalused is not None and iontotalcache is not None:
            ion_usage_rate = iontoalused / (iontoalused + iontotalcache)  if iontoalused + iontotalcache != 0 else 0
        fea['ion_usage_rate'] = round(ion_usage_rate)
        memory_leak_risk_index = mem_data['SUnreclaim'] / mem_data['Slab'] if mem_data['Slab'] else 0
        fea['memory_leak_risk_index'] = round(memory_leak_risk_index)
        cma_usage_rate = mem_data['CmaFree'] / mem_data['CmaTotal'] if mem_data['CmaTotal'] else 0
        fea['cma_usage_rate'] = round(cma_usage_rate)
        memory_health_index = 0.4 * (1 - memory_usage_rate) + 0.3 * (1 - exchangespace_usage_rate) + 0.1 * (
                    1 - memory_leak_risk_index) + 0.1 * (1 - reserve_memory_rate) + 0.1 * cma_usage_rate
        fea['memory_health_index'] = round(memory_health_index)
    return fea

# print _calc_memory_fea('')
content = {u'lan_ip': u'10.192.5.60', u'other_device_info': u'{"memory_info":"{\\"MemFree\\":\\"791920640.0\\",\\"MemTotal\\":\\"5899501568.0\\"}","system_info":"{\\"MODEL\\":\\"\\",\\"BRAND\\":\\"Apple\\",\\"SDK\\":\\"16.1.1\\"}","telephone_info":"{\\"PhoneType\\":\\"\\",\\"NetworkType\\":\\"4G\\",\\"NetworkCountryIso\\":\\"mx\\",\\"DeviceSoftwareVersion\\":\\"16.1.1\\",\\"NetworkOperator\\":\\"050050\\"}","user_agent":"payrupik;1.0.3;iOS;16.1.1;Apple;428*926;0B6D8DC1-2B44-49E0-83EA-F49296E1E969;4G;"}', u'base_station_3g': u'{"radioType":"LTE","lac":"050050","systemId":"","netWorkId":"","mnc":"050","cell":"","mcc":"050"}', u'is_emulator': u'0', u'permission': u'{"privacy_cellular":"none","privacy_location":"3","privacy_microphone":"-1","privacy_contact":"-1","privacy_calendar":"2","privacy_tracking":"2","privacy_camera":"-1","privacy_reminder":"2","privacy_photo":"-1","privacy_notification":"none"}', u'battery': -100, u'is_root': u'0', u'webview_kernel': u'', u'boot_time': u'1699507917.188095', u'a_space': 127877271552, u'r_space': 111375517396, u'wifi_mac': u'', u'wifi_ssid': u''}


def _calc_battery_fea(content, battery_size):
    """
    计算battery特征
    """
    # logging.info('calc battery feature %s' % content)
    fea = {}
    battery_bytes = content.get('battery', '{}')
    try:
        if isinstance(battery_bytes, bytes):
            battery_str = battery_bytes.decode('utf-8')
            battery = json.loads(battery_str)
        else:
            battery = json.loads(battery_bytes)
    except Exception as e:
        print e, traceback.format_exc()
        battery = {}
    # battery = json.loads(content.get('battery', '{}'))


    # fea['battery_info'] = battery
    if not battery:
        return fea
    cols = {'level': 'battery_level', 'temperature': 'battery_temperature', 'voltage': 'battery_voltage',
            'status': 'battery_status', 'health': 'battery_health'}
    for col, name in cols.items():
        if col == 'temperature':
            fea[name] = round((int(battery.get('temperature', 0)) / 10))
        elif col == 'voltage':
            fea[name] = round((int(battery.get('voltage', 0)) / 1000))
        else:
            fea[name] = battery.get(col)
    if battery_size:
        charge_counter = battery.get('charge_counter', '')
        fea['charged_cycle_cnts'] = round(
            int(charge_counter) / battery_size) if charge_counter and charge_counter.isdigit() else 0
        score1 = 0 if fea['battery_health'] == 'good' else 5
        calculate_score2 = lambda charged_cycle_cnts: (
            1 if charged_cycle_cnts > 500 else
            3 if charged_cycle_cnts > 200 else
            2 if charged_cycle_cnts > 100 else
            0
        )
        fea['battery_risky_index'] = score1 + calculate_score2(fea['charged_cycle_cnts'])
    return fea

print _calc_battery_fea(content, 1)