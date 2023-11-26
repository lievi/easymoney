from app.db.sqlmodel.session import get_session


def db_session():
    return next(get_session())
