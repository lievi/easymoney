import logging

from tenacity import (
    after_log,
    before_log,
    retry,
    stop_after_attempt,
    wait_fixed,
)

from app.infrastructure.db.session import SessionLocal


max_retries = 60 * 5
wait_seconds = 1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@retry(
    stop=stop_after_attempt(max_retries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN)
)
def verify_dependencies() -> None:
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Starting dependecies services")
    verify_dependencies()
    logger.info("Services started")


if __name__ == "__main__":
    main()