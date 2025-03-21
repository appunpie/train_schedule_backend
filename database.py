from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベースの設定（SQLite）
DATABASE_URL = "sqlite:///./schedule.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 時間割を保存するテーブル
class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    departure = Column(String, index=True)  # 出発駅
    destination = Column(String, index=True)  # 到着駅
    arrival_time = Column(String)  # 到着時間（HH:MM 形式）

# テーブルを作成
def init_db():
    Base.metadata.create_all(bind=engine)

# DBセッションの取得関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
