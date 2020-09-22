#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.adb
Function    : DB接続抽象クラス
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""


class ADB:
    def __init__(self, id):
        self.__id = id

    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("close")
