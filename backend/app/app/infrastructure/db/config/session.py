from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# TODO: Set this (and the timeout) on settings
# SQLALCHEMT_DATABASE_URL = "postgresql://postgres:t3st3123@db/easy_money"
SQLALCHEMT_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(
    SQLALCHEMT_DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 10},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
