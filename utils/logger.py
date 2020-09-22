#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.logger
Function:   : ログ出力
How to use  : from utils.logger import Logger
              logger = Logger(__name__)
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""

from .config import Config
import logging

format = "%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s"

level = Config["Log"]["level"]
if level == "DEBUG":
    level = logging.DEBUG
elif level == "INFO":
    level = logging.INFO
elif level == "WARN" or level == "WARNING":
    level = logging.WARNING
elif level == "ERROR":
    level = logging.ERROR
else:
    level = logging.INFO

logging.basicConfig(
    filename=Config["Log"]["dir"] + Config["Log"]["file"],
    level=level,
    format=format,
)

Logger = logging.getLogger