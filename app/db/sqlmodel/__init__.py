from sqlmodel import SQLModel, create_engine

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": settings.DATABASE_TIMEOUT},
)


def create_db_and_tables():
    print("db created")
    SQLModel.metadata.create_all(engine)
