#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: zhanghaiyun
@Time: 2025/7/9 14:25  
"""
from datetime import datetime, timedelta

from datetime import datetime, timedelta  # Import at the top level


def calculate_resident_changes(residence_info, current_time=None):
    if current_time is None:
        current_time = datetime.now()  # Now datetime is available here

    three_years_ago = current_time - timedelta(days=3 * 365)


    recent_addresses = set()
    all_addresses = set()

    for info in residence_info:
        if info.get("fechaResidencia"):
            fecha_residencia = datetime.strptime(info.get("fechaResidencia"), "%d%m%Y")

            if fecha_residencia:
                all_addresses.add(info["direccion1"])
                if fecha_residencia >= three_years_ago:
                    recent_addresses.add(info["direccion1"])

    return {
        "last3y_resident_change_cnt": len(recent_addresses),
        "all_resident_change_cnt": len(all_addresses)
    }


if __name__ == '__main__':
    # 测试
    residence_info = [
        {"direccion1": "MARC MOLINA INT 8", "ciudad": "VER", "estado": "VER", "cp": "91700", "tipoDomicilio": "H",
         "codPais": "MX", "fechaReporteDireccion": "28072023"},
        {"direccion1": "CUAUHTEMOC ESQ MARIO MOLINA", "ciudad": "VER", "estado": "VER", "cp": "91700",
         "tipoDomicilio": "H", "codPais": "MX", "fechaReporteDireccion": "18022019"},
        {"direccion1": "RIO PAS 94", "coloniaPoblacion": "RIO MEDIO 4 FRAC", "delegacionMunicipio": "VER",
         "ciudad": "VER", "estado": "VER", "cp": "91809", "fechaResidencia": "15082003", "numeroTelefono": "2292467400",
         "tipoDomicilio": "H", "indicadorEspecialDomicilio": "K", "codPais": "MX", "fechaReporteDireccion": "17112018"},
        {"direccion1": "C MEXIQUILLO", "coloniaPoblacion": "LOS TORRENTES", "delegacionMunicipio": "VER",
         "estado": "VER", "cp": "91808", "fechaResidencia": "01012010", "numeroTelefono": "2292467400",
         "tipoDomicilio": "C", "indicadorEspecialDomicilio": "K", "codPais": "MX", "fechaReporteDireccion": "31082017"}
    ]

    current_time = datetime(2023, 10, 1)
    # result = calculate_resident_changes(residence_info, current_time)
    # print(result)

    aa = {"last3y_resident_change_cnt": 1, "all_resident_change_cnt": 2}
    print aa.get('f')