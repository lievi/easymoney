FROM --platform=linux/amd64 tiangolo/uvicorn-gunicorn-fastapi:latest

WORKDIR /app/

# Copy using Pipfile.lock* in case it doesn't exist yet
COPY Pipfile Pipfile.lock* /app/

# Install Pipenv
RUN pip install pipenv

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then pipenv install --system --dev ; else pipenv install --system ; fi"

COPY . /app

ENV PYTHONPATH=/app
# ENV NEW_RELIC_CONFIG_FILE=newrelic.ini

CMD ["bash", "/start.sh"]
