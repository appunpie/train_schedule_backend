from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Schedule
from datetime import datetime

router = APIRouter()

@router.get("/schedule/today")
def get_today_schedule(db: Session = Depends(get_db)):
    today = datetime.today().strftime("%A")
    schedules = db.query(Schedule).filter(Schedule.day_of_week == today).all()
    return {"schedules": [s.__dict__ for s in schedules]}
