#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.logger import Logger
from utils.wdb import WDB
import utils.wdb

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
    raise ValueError("vali")
except:
    logger.error("error log", exc_info=True)
