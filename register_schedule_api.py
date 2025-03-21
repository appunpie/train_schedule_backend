from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Schedule, get_db, init_db  # database.py からインポート

# FastAPI のインスタンス作成
app = FastAPI()

# データベースを初期化
init_db()

# Pydanticモデル（リクエストボディ用）
class ScheduleCreate(BaseModel):
    departure: str
    destination: str
    arrival_time: str  # フォーマット: HH:MM

# 時間割を登録するAPI
@app.post("/schedule/")
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = Schedule(
        departure=schedule.departure,
        destination=schedule.destination,
        arrival_time=schedule.arrival_time,
    )
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return {"message": "Schedule registered successfully", "data": db_schedule}
