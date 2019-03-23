import urllib.request
import urllib.parse
import json

import pprint


# --------- GET(読み込み　READ)---------------
print("------GET-------")
# HTTPリクエストとレスポンスサービスサイト
url = "http://httpbin.org/get"

# リクエストデータの取得
with urllib.request.urlopen(url) as f:
    # decode=utf-8で情報を取得
    url_req_row = f.read().decode("utf-8")
    # dict形式に変換
    url_req = json.loads(url_req_row)

    # 内容の確認
    pp = pprint.PrettyPrinter(indent=2, width=40, depth=3)
    pp.pprint(url_req)

print()

# ------ GET(読み込み READ)パラメータをつける-----------
print("------GET with payload-------")
# 付加情報
payload_row = {"key01": "value01", "key02": "value02"}

# 付加情報をURL用に変換(key01=value01&key02=value02)
payload = urllib.parse.urlencode(payload_row)

# URLにつける(URL+"?"+付加情報)
url = "http://httpbin.org/get" + "?" + payload

# リクエストデータの取得
with urllib.request.urlopen(url) as f:
    # decode=utf-8で情報を取得
    url_req_row = f.read().decode("utf-8")
    # dict形式に変換
    url_req = json.loads(url_req_row)

    # 内容の確認
    pp = pprint.PrettyPrinter(indent=2, width=40, depth=3)
    pp.pprint(url_req)

print()

# ------POST(作成 CREATE)…パラメーターを見られたくない----------
# 1. 子リソースの作成(ブログ投稿)
# 2. 子リソースの作成(データ追加)
# 3. その他(検索ワードが長いとき GETではなくPOST)
print("------POST-------")
# json形式(ダブルクオート形式)
payload = json.dumps(payload_row).encode("utf-8")
req = urllib.request.Request("http://httpbin.org/post", data=payload, method="POST")

# リクエストデータの取得
with urllib.request.urlopen(req) as f:
    # decode=utf-8で情報を取得
    url_req_row = f.read().decode("utf-8")
    # dict形式に変換
    url_req = json.loads(url_req_row)

    # 内容の確認
    pp = pprint.PrettyPrinter(indent=2, width=40, depth=3)
    pp.pprint(url_req)

print()

# ------PUT(作成,更新 CREATE,UPDATE)----------
print("------PUT-------")
# json形式(ダブルクオート形式)
payload = json.dumps(payload_row).encode("utf-8")
req = urllib.request.Request("http://httpbin.org/put", data=payload, method="PUT")

# リクエストデータの取得
with urllib.request.urlopen(req) as f:
    # decode=utf-8で情報を取得
    url_req_row = f.read().decode("utf-8")
    # dict形式に変換
    url_req = json.loads(url_req_row)

    # 内容の確認
    pp = pprint.PrettyPrinter(indent=2, width=40, depth=3)
    pp.pprint(url_req)

# ------DELETE(削除 DELETE)----------
print("------DELETE-------")
# json形式(ダブルクオート形式)
payload = json.dumps(payload_row).encode("utf-8")
req = urllib.request.Request("http://httpbin.org/delete", data=payload, method="DELETE")

# リクエストデータの取得
with urllib.request.urlopen(req) as f:
    # decode=utf-8で情報を取得
    url_req_row = f.read().decode("utf-8")
    # dict形式に変換
    url_req = json.loads(url_req_row)

    # 内容の確認
    pp = pprint.PrettyPrinter(indent=2, width=40, depth=3)
    pp.pprint(url_req)
