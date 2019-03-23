#! env python
# -*- coding: utf-8 -*-

import enum
import json
import pprint
import urllib.request
import urllib.parse

# Date: 2019/03/23
# Filename: HttpAccess 

__author__ = 'yoshiaki'
__date__ = "2019/03/23"

@enum.unique
class Status(enum.IntFlag):
    GET = 1,
    POST = 2,
    PUT = 3,
    DELETE = 4


class HttpAccess(object):

    def __init__(self, url: str, status: Status, data: dict = None):
        self.status = status
        self.url = url
        self.data = data
        # 設定
        self.select_type()

    def set_url_reqest(self, send_req):
        # リクエストデータの取得
        with urllib.request.urlopen(send_req) as f:
            # decode=utf-8で情報を取得
            url_req_row = f.read().decode("utf-8")
            # dict形式に変換
            self.url_req = json.loads(url_req_row)

    def show(self):
        # 内容の確認
        pp = pprint.PrettyPrinter(indent=2, width=40, depth=3)
        pp.pprint(self.url_req)

    def select_type(self):
        # 1.GETの場合
        if (self.status == Status.GET):
            # urlの"/get"追記
            self.url = self.url + "get" if self.url[-1] == "/" else self.url + "/get"
            # 付加データがあり、かつ dictタイプである-> urlにデータ追記
            if (self.data is not None and type(self.data) is dict):
                # 付加情報をURL用に変換(key01=value01&key02=value02)
                payload = urllib.parse.urlencode(self.data)
                self.url = self.url + "?" + payload

            # リクエストデータの取得
            self.set_url_reqest(self.url)


        # 2.POST
        elif (self.status == Status.POST):
            # urlの"/post"追記
            self.url = self.url + "post" if self.url[-1] == "/" else self.url + "/post"
            payload = json.dumps(self.data).encode("utf-8")
            req = urllib.request.Request(self.url, data=payload, method="POST")
            # リクエストデータの取得
            self.set_url_reqest(req)

        # 3.PUT
        elif (self.status == Status.PUT):
            # urlの"/post"追記
            self.url = self.url + "put" if self.url[-1] == "/" else self.url + "/put"
            payload = json.dumps(self.data).encode("utf-8")
            req = urllib.request.Request(self.url, data=payload, method="PUT")
            # リクエストデータの取得
            self.set_url_reqest(req)

        # 4.delete
        elif (self.status == Status.DELETE):
            # urlの"/post"追記
            self.url = self.url + "delete" if self.url[-1] == "/" else self.url + "/delete"
            payload = json.dumps(self.data).encode("utf-8")
            req = urllib.request.Request(self.url, data=payload, method="DELETE")
            # リクエストデータの取得
            self.set_url_reqest(req)

        else:
            print("no")


if __name__ == '__main__':
    url = "http://httpbin.org"
    d = {"key01": "value01", "key02": "value02"}

    http_access1 =HttpAccess(url=url,status=Status.GET)
    http_access1.show()

    http_access2 = HttpAccess(url=url, status=Status.GET, data=d)
    http_access2.show()

    http_access3 = HttpAccess(url=url, status=Status.POST, data=d)
    http_access3.show()

    http_access4 = HttpAccess(url=url, status=Status.PUT, data=d)
    http_access4.show()

    http_access5 = HttpAccess(url=url, status=Status.DELETE, data=d)
    http_access5.show()