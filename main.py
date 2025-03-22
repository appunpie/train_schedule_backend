from fastapi import FastAPI
from register_schedule_api import router as register_router
from get_today_schedule_api import router as get_today_router
from database import init_db

app = FastAPI()

# DB初期化
init_db()

# ルーター登録
app.include_router(register_router)
app.include_router(get_today_router)
