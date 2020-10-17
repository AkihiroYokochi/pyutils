#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module      : utils.ws
Function    : Webサーバ
How to use  : from utils.ws import WebServer
              with WebServer(port) as ws:
                ws.run()
Author      : K.Shibuya
Version     : 2020/09/21 v1.0.0
History     : 2020/09/21 v1.0.0 K.Shibuya init
              ****/**/** v*.*.* *.******* ****
"""

from utils.config import Config
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(Config["Web"]["port"])
DIRECTORY = Config["Web"]["dir"]


class HTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


class WebServer:
    def __init__(self):
        pass

    def open(self):
        pass

    def close(self):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def run(self):
        self.__httpd = HTTPServer(("", PORT), HTTPRequestHandler)
        self.__httpd.serve_forever()


if __name__ == "__main__":
    with WebServer() as ws:
        ws.run()
