from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# TODO: i guess this create engine should be in another place, but where?
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": settings.DATABASE_TIMEOUT},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
