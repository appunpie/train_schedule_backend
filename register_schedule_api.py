from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Schedule, get_db

router = APIRouter()

# リクエストボディのスキーマ
class ScheduleCreate(BaseModel):
    departure: str
    destination: str
    arrival_time: str  # 例: "08:30"
    day_of_week: str  #例: "Monday", "Tuesday"

# 登録API
@router.post("/schedule/")
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = Schedule(
        departure=schedule.departure,  #出発駅を登録
        destination=schedule.destination,  #到着駅を登録
        arrival_time=schedule.arrival_time,  #到着時間を登録
        day_of_week=schedule.day_of_week  #曜日を登録
    )
    db.add(db_schedule)  #データベースに上記のデータを追加
    db.commit()
    db.refresh(db_schedule)
    return {"message": "Schedule registered successfully", "data": db_schedule}
