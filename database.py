from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./schedule.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # ユーザーID（後で認証機能を追加する場合）
    day_of_week = Column(String, index=True)  # 曜日（例: Monday, Tuesday）
    departure = Column(String, index=True)  # 出発駅
    destination = Column(String, index=True)  # 到着駅
    departure_time = Column(String)  # 出発時間（HH:MM形式）

Base.metadata.create_all(bind=engine)
