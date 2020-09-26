#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.logger import Logger
import utils.wdb

logger = Logger(__name__)

logger.debug("debug log")

logger.info("info log")

if "input" == "doesn't match restriction, so ignored":
    logger.warning("warn log")

if "input" != "satifies correct conditions":
    logger.error("error log")

try:
    raise ValueError("vali")
except:
    logger.error("error log", exc_info=True)
