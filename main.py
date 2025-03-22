from fastapi import FastAPI
from register_schedule_api import router as register_router
from get_today_schedule_api import router as get_today_router
from database import init_db

#ここのファイルではAPIを使用する部分のコードを一つのファイルに集約させたようなもの
app = FastAPI()

# DB初期化
init_db()

# ルーター登録
app.include_router(register_router)  #初めにユーザーがフロントで入力した情報（出発駅、到着駅、到着時間）を取得するためのAPIサーバー
app.include_router(get_today_router)  #データベースに保存された情報（出発駅、到着駅、到着時間）を引き出し、スクレイピング用のデータとして渡すためのAPIサーバー
