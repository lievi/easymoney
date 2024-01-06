import logging

from sqlalchemy import text
from tenacity import (
    after_log,
    before_log,
    retry,
    stop_after_attempt,
    wait_fixed,
)

from easymoney.api.dependencies import db_session

max_retries = 10
wait_seconds = 1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@retry(
    stop=stop_after_attempt(max_retries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def verify_dependencies() -> None:
    _check_db_connection()


def _check_db_connection() -> None:
    session = db_session()
    session.exec(text("SELECT 1"))


def main() -> None:  # pragma: no cover
    logger.info("Starting dependecies services")
    verify_dependencies()
    logger.info("Services started")


if __name__ == "__main__":  # pragma: no cover
    main()
