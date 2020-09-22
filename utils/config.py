#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.config
Function    : 設定ファイル読込
How to use  : from utils.config import Config
              value = Config["sec"]["key"]
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""

import os
import configparser

Config = configparser.ConfigParser()
Config.read(os.path.dirname(__file__) + os.sep + "app.ini", encoding="UTF-8")

for sec in Config:
    for key in Config[sec]:
        if "dir" in key:
            Config[sec][key].replace("/", os.sep)
