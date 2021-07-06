# -*- coding: utf-8 -*-
import requests
import pandas as pd
import csv
import time

#自動検索ツールAPIを使用
REQUEST_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
APP_ID = "1099237583585301106"

#起動説明
print("\r\n\r\n【楽天市場/商品検索】\r\n\r\n")
print("：注意説明：")
print("""
    ・入力内容は()内の指定に従ってください。
    ・入力内容にエラーがある場合プログラムが正常に動作しないことがあります。
    ・検索結果は同じディレクトリ内にCSVファイル(market.csv)として保存します。
""")

#APP_ID = str(input("\r\n楽天市場APIのアプリケーションID/デベロッパーIDを入力してください>>"))
#check = int(input("【確認】アプリケーションID/デベロッパーIDに間違いはありませんか？＜はい：1 / いいえ：２＞(番号を半角入力)"))
#if check == 2:
#    while True:
#        APP_ID = str(input("\r\n楽天市場APIのアプリケーションID/デベロッパーIDを入力してください>>"))
#        check = int(input("【確認】アプリケーションID/デベロッパーIDに間違いはありませんか？＜はい：1 / いいえ：２＞(番号を半角入力)"))
#        if check == 1:
#             break

#商品検索の入力
keyword = str(input("\r\n\r\n検索キーワードを入力してください(半角または全角)>>"))

#入力内容の確認
print("\r\n\r\n======================入力内容の確認======================")
print(">　検索キーワードは【",keyword,"】を指定中")
print("==========================================================")

check_menu = int(input("\r\n【確認】入力内容にお間違いないですか？＜はい：1 / いいえ：2＞(番号を半角入力)>>"))

#入力内容の不備または入力間違い
if check_menu == 2:
    while True:
        keyword = str(input("\r\n検索キーワードを入力してください(半角または全角)>>"))
        print("\r\n\r\n=============================入力内容の確認=============================")
        print(">　検索キーワードは【",keyword,"】を指定中")
        print("========================================================================")
        check_menu = int(input("\r\n【確認】入力内容にお間違いないですか？＜はい：1 / いいえ：2＞(番号を半角入力)>>"))
        if check_menu == 1:
            break

hit = int(input("\r\n\r\n検索結果を何個取得しますか？(半角:1～30で指定)>>"))

#検索件数の審査
if hit<1 or 30<hit:
    while True:
        print("\r\n\r\n検索結果は1以上30以下しか指定できません。")
        hit = int(input("検索結果を何個取得しますか？(1以上30以下：半角数字を入力)>>"))
        if 1<=hit<=30:
            break

#入力内容の確認
print("\r\n\r\n==================入力内容の確認==================")
print(">　検索件数は【",hit,"】を指定中")
print("==================================================")
check_hits = int(input("\r\n【確認】入力内容にお間違いないですか？＜はい：1 / いいえ：２＞(番号を半角入力)>>"))
if check_hits == 2:
    while True:
        hit = int(input("\r\n\r\n検索結果を何個取得しますか？(半角:1～30で指定)>>"))
        print("\r\n\r\n==================入力内容の確認==================")
        print(">　検索件数は【",hit,"】を指定中")
        print("==================================================")
        check_hits = int(input("\r\n【確認】入力内容にお間違いないですか？＜はい：1 / いいえ：2＞(番号を半角入力)>>"))
        if check_menu == 1:
            break

#パラメータの指定
params={
    "applicationId":APP_ID,
    "keyword":keyword,
    "hits":hit,
    "sort":"standard"
}

res = requests.get(REQUEST_URL,params)
result = res.json()

print("\r\n****リクエストURLを送信中****")
time.sleep(2)
print("****情報を成形中****")
time.sleep(0.5)

df = pd.DataFrame()
items = result["Items"]
for item in items:
    item_info = item["Item"]
    df = df.append(item_info,ignore_index=True)

df[['itemName','itemCode','itemPrice','itemUrl','reviewAverage']].to_csv("market.csv")

print("\r\n\r\n同じディレクトリ内にcsvファイルを生成しました")
print("\r\n【楽天市場/商品検索】を終了します")