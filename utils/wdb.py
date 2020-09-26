#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.wdb
Function    : DB接続クラス（MySQL）
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""
from utils.config import Config
from utils.logger import Logger
import MySQLdb
import json

logger = Logger(__name__)


class WDB:
    def __init__(self, db_sec="DB"):
        self._connection = MySQLdb.connect(
            host=Config[db_sec]["host"],
            db=Config[db_sec]["db"],
            user=Config[db_sec]["user"],
            passwd=Config[db_sec]["passwd"],
        )
        self._connection.autocommit(False)
        self._cursor = self._connection.cursor()
        self._sql = ""
        self._param = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cursor.close()
        self._connection.close()

    def beginTran(self):
        self.rollbackTran()

    def addQuery(self, sql):
        self._sql += sql

    def addParam(self, key, value):
        self._param[key] = value

    def execute(self):
        logger.debug("[SQL]" + self._sql)
        logger.debug("[Parameters]" + json.dumps(self._param))
        self._cursor.execute(self._sql, self._param)
        return self._cursor.fetchall()

    def commitTran(self):
        self._connection.commit()

    def rollbackTran(self):
        self._connection.rollback()
