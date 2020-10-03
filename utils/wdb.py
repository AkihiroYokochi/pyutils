#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.wdb
Function    : DB接続クラス（MySQL）
How to use  : from utils.wdb import WDB
              with WDB() as wdb:
                wdb.addQuery(...)
                wdb.addParam(...)
                wdb.execute()
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
        self._db_sec = db_sec
        self._sql = ""
        self._param = {}

    def open(self, db_sec=None):
        if db_sec != None:
            self._db_sec = db_sec
        self._connection = MySQLdb.connect(
            host=Config[self._db_sec]["host"],
            db=Config[self._db_sec]["db"],
            user=Config[self._db_sec]["user"],
            passwd=Config[self._db_sec]["passwd"],
        )
        self._connection.autocommit(False)
        self._cursor = self._connection.cursor()

    def close(self):
        self._cursor.close()
        self._connection.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

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
        self._sql = ""
        self._param.clear()
        return self._cursor.fetchall()

    def commitTran(self):
        self._connection.commit()

    def rollbackTran(self):
        self._connection.rollback()


if __name__ == "__main__":
    with WDB() as wdb:
        wdb.addQuery("select sysdate()")
        print(wdb.execute()[0])
