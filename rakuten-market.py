# -*- coding: utf-8 -*-
import requests
import pandas as pd
import csv
import time

#自動検索ツールAPIを使用
REQUEST_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
APP_ID = "発行したAPP_IDを入力"


#パラメータの指定
params={
    "applicationId":APP_ID,
    "keyword":'検索するキーワードを入力(str)',
    "hits":'検索件数を入力(int)',
    "sort":"standard"
}

res = requests.get(REQUEST_URL,params)
result = res.json()
df = pd.DataFrame()
items = result["Items"]
for item in items:
    item_info = item["Item"]
    df = df.append(item_info,ignore_index=True)

#csvを同じディレクトリ内に保存する
df[['itemName','itemCode','itemPrice','itemUrl','reviewAverage']].to_csv("market.csv")
