FROM python:3.11-slim

# use built-in pip to access poetry 
RUN pip install poetry

# start installing things with poetry
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-ansi -n

COPY ./scripts/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./app/gunicorn_conf.py /gunicorn_conf.py

COPY . /app
WORKDIR /app/

ENV PYTHONPATH=/app

CMD ["/start.sh"]
