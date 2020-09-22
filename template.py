#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : template
Function    : アプリケーション
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""

from utils.adb import ADB

with ADB("1") as adb:
    print("process")
