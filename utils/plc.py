#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.plc
Function    : PLC通信クラス（FX3G）
How to use  : from utils.plc import PLC
              with PLC() as plc:
                plc.addQuery(...)
                plc.addParam(...)
                plc.execute()
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""

import socket

HOST = "169.254.123.100"  # <- PLCに割り振り or 設定したIP
PORT = 1025  # <- 同じくPLCに設定したポート


class PLC:
    def __init__(self):
        pass

    def connect(self):
        self.__socket_client = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM  # IPv4  # TCP接続
        )
        self.__socket_client.connect((HOST, PORT))

    def close(self):
        self.__socket_client.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__socket_client.close()

    def get_data(self):
        print("send:", b"\x01\xFF\x0A\x00\xE8\x03\x00\x00\x20\x44\x0B\x00".hex())
        self.__socket_client.send(
            b"\x01"  # サブヘッダ (00:ビット単位読出 01:ワード単位読出 02:ビット単位書込 03:ワード単位書込)
            b"\xFF"  # PC番号 (FF固定)
            b"\x0A\x00"  # 監視タイマ (単位:250ms 2500ms=000A0)
            b"\xE8\x03\x00\x00"  # デバイス番号を16進数で (1000=3E8)
            b"\x20\x44"  # 空白文字 + デバイス名(D)
            b"\x0B"  # デバイス点数(11点)
            b"\x00"  # 終了コード
        )
        result = self.__socket_client.recv(1024).hex()  # 信号を受け取る
        print("receive:", result)
        result = {
            "subhdr": result[0:2],  # サブヘッダ
            "exitcd": result[2:4],  # 終了コード
            "data": result[4:],  # データ
        }
        if result["subhdr"] == "81" and result["exitcd"] == "00":
            # print("data", result["data"])
            tmp = result["data"]
            data = {}
            for idx in range(int(len(tmp) / 4)):
                startIdx = idx * 4
                data["D" + str(1000 + idx)] = int(
                    tmp[startIdx + 2 : startIdx + 4] + tmp[startIdx : startIdx + 2], 16
                )
            # print(data)
            return data
        else:
            print("error:", result["exitcd"])


if __name__ == "__main__":
    with PLC() as plc:
        plc.get_data()
