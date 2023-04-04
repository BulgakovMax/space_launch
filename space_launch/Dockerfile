FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        postgresql \
        libpq-dev \
        netcat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./space_launch ./code
COPY entrypoint.sh ./code

CMD ["./entrypoint.sh"]