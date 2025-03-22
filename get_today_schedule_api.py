from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Schedule
from datetime import datetime

router = APIRouter()

@router.get("/schedule/today")
def get_today_schedule(db: Session = Depends(get_db)):
    today = datetime.today().strftime("%A")
    schedules = db.query(Schedule).filter(Schedule.day_of_week == today).all()
    return {
        "schedules": [
            {
                **s.__dict__,
                "arrival_time": s.arrival_time.replace("-", ":")  #"9-00"を "9:00"に変換する
            }
            for s in schedules
        ]
    }
