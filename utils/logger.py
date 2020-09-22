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
import logging.handlers

# 出力レベル
_level = Config["Log"]["level"]
if _level not in ["DEBUG", "INFO", "WARN", "WARNING", "ERROR"]:
  _level = "INFO"

# フォーマット
_format = logging.Formatter(fmt="%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s")

# 出力先
_fileHandler = logging.handlers.RotatingFileHandler(filename=Config["Log"]["dir"] + Config["Log"]["file"], maxBytes=int(Config["Log"]["maxBytes"].replace(",", "")), backupCount=1)

# ルートロガー
_root_logger = logging.getLogger()
_fileHandler.setLevel(logging.getLevelName(_level))
_fileHandler.setFormatter(_format)
_root_logger.addHandler(_fileHandler)
_root_logger.setLevel(_level)

# 外部向け
Logger = logging.getLogger