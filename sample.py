#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : sample
Function    : サンプル
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""


from utils.logger import Logger
from utils.wdb import WDB


logger = Logger(__name__)

logger.debug("debug log")

logger.info("info log")

if "input" == "doesn't match restriction, so ignored":
    logger.warning("warn log")

if "input" != "satifies correct conditions":
    logger.error("error log")

try:
    with WDB() as wdb:
        wdb.addQuery("select * from T_SAMPLE")
        data = wdb.execute()
        print(data)
        wdb.addQuery("insert into T_SAMPLE values (3, 'ghi')")
        data = wdb.execute()
        print(data)
        wdb.commitTran()
    # raise ValueError("vali")
except:
    logger.error("error log", exc_info=True)
