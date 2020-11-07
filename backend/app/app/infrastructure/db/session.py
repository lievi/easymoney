from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": settings.DATABASE_TIMEOUT},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
