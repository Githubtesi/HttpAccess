#! env python
# -*- coding: utf-8 -*-

import os
import sys

# Date: 2019/03/23
# Filename: json_sample 

__author__ = 'yoshiaki'
__date__ = "2019/03/23"

def main():
    # 作業ディレクトリを自身のファイルのディレクトリに変更
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

    import json

    # -----------書き込み--------------------
    j = {
        "employees": [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
    }



    # ------出力-----------------------
    # シングルクォート出力
    # print(j)

    # print出力はdumps(jsonは"ダブルクオート"で囲う)
    print(json.dumps(j))

    # -----書き込み------------------
    # ファイル書き込みはdump
    with open("test.json", "w") as f:
        json.dump(j, f)


    # ----- ファイルの読み込み ---------
    with open("test.json", "r")as f:
        j = json.load(f)

    # データ化の例
    for employee in j["employees"]:
        print(employee)

    return


if __name__ == '__main__':
    main()
